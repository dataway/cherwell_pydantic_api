#!/usr/bin/env python3
"""Cherwell API code generator

Generates Python models and endpoints from the Cherwell API Swagger schema.
This is NOT intended as a general purpose code generator. It will be tested only
against the Cherwell Swagger schema and may not work with other schemas.
"""


import re
from collections import defaultdict
from pathlib import Path
from typing import Tuple, Literal

import black
import datamodel_code_generator
import datamodel_code_generator.format
import isort

import cherwell_pydantic_api.types



re_fstr = re.compile(r'{([^}]+)}')
Literal  # type: ignore # used by eval


def class_name_generator(name: str) -> str:
    if name == 'Object':
        return 'CherwellObjectID'
    if name in ('Model', 'Object', 'NameValuePair', 'Link'):
        return f"Cherwell{name}"
    return name


def generate_models(input: Path, output: Path):
    # I had to patch datamodel_code_generator, will submit a PR. auk 20230316
    # PR: https://github.com/koxudaxi/datamodel-code-generator/pull/1187
    return datamodel_code_generator.generate(
        input,
        input_file_type=datamodel_code_generator.InputFileType.JsonSchema,
        output=output,
        target_python_version=datamodel_code_generator.format.PythonVersion.PY_39,
        base_class='cherwell_pydantic_api.generated_api_utils.ApiBaseModel',
        # Required so that the __root__ field is included - required for pydantic schema
        custom_template_dir=Path(
            __file__).parent.joinpath('codegen_templates'),
        field_include_all_keys=True,
        custom_class_name_generator=class_name_generator
    )


def get_endpoint_method(path: str, op: str, opspec: dict) -> Tuple[str, str]:
    opid = opspec['operationId']
    tag = opspec['tags'][0]
    if opid.startswith(f"{tag}_"):
        opid = opid[len(f"{tag}_"):]
    return (tag, opid)


def get_python_type(paramspec: dict, opspec: dict, models_module: str, import_set: set) -> str:
    if not paramspec.get('required', True):
        optional_paramspec = paramspec.copy()
        del optional_paramspec['required']
        return f"Optional[{get_python_type(optional_paramspec, opspec, models_module, import_set)}]"
    if '$ref' in paramspec:
        ref = paramspec['$ref']
        if ref.startswith('#/definitions/'):
            model = models_module + '.' + ref[len('#/definitions/'):]
            import_set.add('.'.join(model.split('.')[:-1]))
            return model
    if 'schema' in paramspec:
        schema = paramspec['schema']
        if schema.get('type', None) == 'array':
            return f"list[{get_python_type(schema['items'], opspec, models_module, import_set)}]"
        if '$ref' in schema:
            schema['from_ref'] = schema['$ref']
            return get_python_type(schema, opspec, models_module, import_set)
        if schema.get('type', '') == 'string':
            import_set.add('cherwell_pydantic_api.types')
            if paramspec.get('in', '') == 'body':
                return 'cherwell_pydantic_api.types.FileUpload'
            if schema.get('format', '') == 'binary':
                return 'cherwell_pydantic_api.types.FileDownload'
            return 'cherwell_pydantic_api.types.StringResponse'

    name = paramspec.get('name', '').lower()
    is_input = paramspec.get('in', '') in ('query', 'path',)
    if name.endswith('busobid'):
        import_set.add('cherwell_pydantic_api.types')
        return 'cherwell_pydantic_api.types.BusObIDParamType' if is_input else 'cherwell_pydantic_api.types.BusObID'
    if name.endswith('busobrecid'):
        import_set.add('cherwell_pydantic_api.types')
        return 'cherwell_pydantic_api.types.BusObRecID'
    enumvals = paramspec.get('enum', None)
    if enumvals:
        pytype = f"Literal{enumvals}"
        # TODO: see if we can do without eval
        typeval = eval(pytype)
        for tname in dir(cherwell_pydantic_api.types):
            if getattr(cherwell_pydantic_api.types, tname) == typeval:
                import_set.add('cherwell_pydantic_api.types')
                return f"cherwell_pydantic_api.types.{tname}"
        return pytype
    # if 'application/octet-stream' in opspec['consumes']:
    #    print(f"BINARY: {opspec['operationId']}: {paramspec=}")
    # if 'application/octet-stream' in opspec['consumes'] and paramspec.get('type', '') == 'string' and paramspec.get('in', '') == 'body':
    #    import_set.add('cherwell_pydantic_api.types')
    #    return 'cherwell_pydantic_api.types.FileUpload'
    if opspec['operationId'] == 'Service_Token' and name in ('client_id', 'client_secret', 'password',):
        import_set.add('pydantic')
        return 'pydantic.SecretStr'
    if 'type' in paramspec:
        return {'boolean': 'bool', 'integer': 'int', 'number': 'float', 'string': 'str',
                'array': 'list', 'object': 'dict'}.get(paramspec['type'], 'Any')
    print(f"ANY: {opspec['operationId']}: {paramspec=}")
    return 'Any'


def format_docstring(s: str) -> str:
    return re.sub('(?:<br */?>)|(?:</br *>)', '\n', s).replace('\\', '&#92;')


def generate_endpoints(output: Path):
    try:
        import cherwell_pydantic_api._generated.api.models
        schema = cherwell_pydantic_api._generated.api.models.CherwellModel.schema()
    except:
        del cherwell_pydantic_api._generated.api.models  # type: ignore
        raise
    models_module = cherwell_pydantic_api._generated.api.models.__name__
    tags = {}
    for tag in schema['tags']:
        tags[tag['name']] = tag['description']
    interfaces = defaultdict(lambda: [])
    interface_imports = defaultdict(lambda: set())
    for path, pathspec in schema['paths'].items():
        for op, opspec in pathspec.items():
            assert op in ('get', 'post', 'put', 'delete')
            interface, method = get_endpoint_method(path, op, opspec)
            if method == '':
                continue
            opspec['interface'] = interface
            opspec['method'] = method

            # Parse the parameters

            paramspecs = []
            bodyparam = None
            for paramspec in opspec['parameters']:
                # Skip lang and locale parameters. TODO: consider offering these as parameters
                if paramspec['name'] in ('lang', 'locale',):
                    continue
                pytype = get_python_type(
                    paramspec, opspec, models_module, interface_imports[interface])
                paramspec['pytype'] = pytype
                paramspec['pyvalue'] = paramspec['name']
                if 'SecretStr' in pytype:
                    paramspec['pyvalue'] = f"{paramspec['name']}.get_secret_value()"
                if paramspec['in'] == 'body':
                    assert bodyparam is None
                    bodyparam = paramspec
                paramspecs.append(paramspec)

            # Determine the return type

            if '200' in opspec['responses']:
                rtype = get_python_type(
                    opspec['responses']['200'], opspec, models_module, interface_imports[interface])
            else:
                rtype = 'None'

            # Generate method signature

            if paramspecs:
                ilines = [f" async def {method}(self,"]
                for paramspec in paramspecs:
                    if paramspec['required']:
                        ilines.append(
                            f"  {paramspec['name']}: {paramspec['pytype']},")
                    else:
                        ilines.append(
                            f"  {paramspec['name']}: {paramspec['pytype']} = None,")
                ilines.append(f" ) -> {rtype}:")
            else:
                ilines = [f" async def {method}(self) -> {rtype}:"]

            # Generate method docstring

            if 'summary' in opspec:
                ilines.append(
                    f"  \"\"\"{format_docstring(opspec['summary'])}\n")
            else:
                ilines.append('  """')
            if 'description' in opspec:
                ilines.append(format_docstring(opspec['description']))
            for paramspec in paramspecs:
                description = paramspec.get('description', '')
                if description == '' and paramspec['in'] == 'body':
                    description = 'The request body'
                description = format_docstring(description)
                ilines.append(
                    f" :param {paramspec['name']}: {description}")
            ilines.append(f" :return: {rtype}")
            ilines.append('"""')

            # Generate params to pass to the request

            qparams = []
            qparams_optional = []
            post = []
            post_optional = []
            pathparams = []
            path_fstrs = set(re_fstr.findall(path))

            for paramspec in paramspecs:
                if paramspec['in'] == 'query':
                    if not paramspec['required']:
                        qparams_optional.append(
                            f"  if {paramspec['name']} is not None: params['{paramspec['name']}'] = {paramspec['pyvalue']}")
                    else:
                        qparams.append(
                            f"'{paramspec['name']}': {paramspec['pyvalue']}")
                elif paramspec['in'] == 'formData':
                    assert op in ('post', 'post_form',)
                    assert bodyparam is None
                    op = 'post_form'
                    if not paramspec['required']:
                        post_optional.append(
                            f"  if {paramspec['name']} is not None: post['{paramspec['name']}'] = {paramspec['pyvalue']}")
                    else:
                        post.append(
                            f"'{paramspec['name']}': {paramspec['pyvalue']}")
                elif paramspec['in'] == 'path':
                    assert (paramspec['required'])
                    pathparams.append(paramspec['name'])
                    if not paramspec['pytype'].startswith('cherwell_pydantic_api.types.') and not paramspec['name'].lower().endswith('id'):
                        print(f"{method}: pathparam not typed: {paramspec['name']} - {paramspec['pytype']}")
                    if paramspec['pytype'] not in ('int', 'float'):
                        ilines.append(
                            f"  self.validate_path_param({paramspec['name']}, {paramspec['pytype']})")
                    path_fstrs.remove(paramspec['name'])
                elif paramspec is bodyparam:
                    assert op in ('post', 'put',)
                    op = 'post_body'
                else:
                    assert False, f"Unknown param type {paramspec['in']} (path: {path})"
            assert not (
                pathparams and path_fstrs), f"Unused path params: {path_fstrs}"

            # Generate params used to call request

            call_params = [f"{'f' if pathparams else ''}'{path}'"]
            if post:
                ilines.append(f"  post={{{', '.join(post)}}}")
            elif post_optional:
                ilines.append("  post={}")
            if qparams:
                ilines.append(
                    f"  params: dict[str, Any]={{{', '.join(qparams)}}}")
                call_params.append('params=params')
            elif qparams_optional:
                ilines.append("  params={}")
                call_params.append('params=params')
            if post_optional:
                ilines.extend(post_optional)
            if qparams_optional:
                ilines.extend(qparams_optional)
            if op == 'post_form':
                call_params.append('data=post')
            elif op == 'post_body' and bodyparam:
                if 'application/json' in opspec['consumes']:
                    call_params.append(
                        f"content={bodyparam['pyvalue']}.json(exclude_unset=True, by_alias=True)")
                elif 'application/octet-stream' in opspec['consumes']:
                    call_params.append(f"content={bodyparam['pyvalue']}")
                    call_params.append(
                        "content_type='application/octet-stream'")
                else:
                    assert False, "Unknown content type"

            # Call the API

            ilines.append(
                f"  response = await self.{op}({', '.join(call_params)})")
            ilines.append(f"  return self.parse_response(response, {rtype})")
            ilines.append('')

            # End of method

            interfaces[interface].extend(ilines)
    ifiles = {}
    init_lines = []
    for interface in interfaces.keys():
        ilines = interfaces[interface]
        hlines = ["from typing import Any, Literal, Optional",]
        hlines.extend([f"import {i}" for i in interface_imports[interface]])
        hlines.append(
            "from cherwell_pydantic_api.generated_api_utils import GeneratedInterfaceBase\n")
        hlines.append(f"class {interface}Interface(GeneratedInterfaceBase):")
        ifiles[interface] = '\n'.join(hlines + ilines)
        init_lines.append(f"from .{interface} import {interface}Interface")
    init_lines.append(
        f"\n\nclass GeneratedInterfaces({', '.join([f'{i}Interface' for i in interfaces.keys()])}):\n pass")
    ifiles['__init__'] = '\n'.join(init_lines)
    if not output.exists():
        output.mkdir(parents=True)
    for interface in ifiles.keys():
        file = output.joinpath(f"{interface}.py").open('wt')
        file.write(black.format_str(
            isort.api.sort_code_string(ifiles[interface]), mode=black.FileMode(preview=True)))
        file.close()
    return ifiles


def generate(base: Path):
    apipath = base.joinpath('cherwell_pydantic_api/_generated/api')
    if not base.joinpath('cherwell_pydantic_api/__init__.py').exists():
        raise Exception(
            f"Run this from the root of the cherwell_pydantic_api project")
    if not apipath.exists():
        apipath.mkdir(parents=True)
        apipath.joinpath('__init__.py').touch()
    try:
        r2 = generate_endpoints(apipath.joinpath('endpoints'))
        r1 = None
        print("Models were recycled")
    except Exception as e:
        print(
            f"Failed to generate endpoints, trying to regenerate models; {e}")
        r1 = generate_models(base.joinpath('csm_api-swagger.json'),
                             apipath.joinpath('models'))
        r2 = generate_endpoints(apipath.joinpath('endpoints'))
    return r1, r2


if __name__ == '__main__':
    r1, r2 = generate(Path('.'))
