# cherwell_pydantic_api
## a pythonic, asyncio connector for the Cherwell CSM API with full usage of Pydantic types

This module implements a modern, Pythonic, [asyncio](https://docs.python.org/3/library/asyncio.html) interface to the API offered by the Cherwell Service Management (CSM) ITSM solution.

It offers both a low-level interface to each API call, as well as a high-level interface that maps Cherwell Business Objects to individual [Pydantic](https://docs.pydantic.dev/) models. These models will be automatically generated for your Cherwell instance and maintained in a git repository. This makes it easy to track changes in business object definitions automatically.

![license](https://img.shields.io/github/license/dataway/cherwell_pydantic_api.svg)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cherwell-pydantic-api)](https://pypi.python.org/pypi/cherwell-pydantic-api)
