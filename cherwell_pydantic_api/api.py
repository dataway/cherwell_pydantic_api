import logging
import time
from typing import Any, AsyncIterable, Iterable, Literal, Mapping, Optional, Union

import httpx

from cherwell_pydantic_api._generated.api.models.Trebuchet.WebApi.DataContracts.BusinessObject import Summary
from cherwell_pydantic_api.settings import InstanceSettingsBase

from ._generated.api.endpoints import GeneratedInterfaces
from .generated_api_utils import GeneratedInterfaceBase, Response, URLType
from .types import BusObID, BusinessObjectType



class Connection(GeneratedInterfaces, GeneratedInterfaceBase):
    def __init__(self, instance_settings: InstanceSettingsBase):
        self._settings = instance_settings
        self._base_url = self._settings.base_url
        self._client_id = self._settings.client_id
        self._username = self._settings.username
        self._password = self._settings.password
        self._client = httpx.AsyncClient(base_url=str(self._base_url),
                                         headers={
                                             'Content-Type': 'application/json'},
                                         params={'locale': 'en-150'},
                                         timeout=self._settings.timeout)
        self._token: Optional[str] = None
        # TODO: come up with a better solution for these:
        self.raise_on_error_500 = False
        self.retry_on_error_401 = False
        self.retry_on_error_401_wait = 4.0
        self.reauthentication_counter = 0


    async def authenticate(self):
        # TODO: support other grant_type values
        response = await self.Token(grant_type='password', client_id=self._client_id, username=self._username, password=self._password)
        self._token = response.access_token
        self._client.headers.update({'Authorization': f'Bearer {self._token}'})
        return True


    async def logout(self):
        return await self.delete('/api/v1/logout')


    async def request(self,
                      method: Literal['GET', 'POST', 'PUT', 'DELETE'],
                      url: URLType,
                      *,
                      content: Optional[Union[str, bytes,
                                              Iterable[bytes], AsyncIterable[bytes]]] = None,
                      data: Optional[Mapping[str, Any]] = None,
                      json: Optional[Any] = None,
                      params: Optional[Mapping[str, Any]] = None,
                      content_type: Optional[str] = None,
                      **kwargs
                      ) -> Response:
        if content_type is not None:
            kwargs.setdefault('headers', {})['Content-Type'] = content_type
        req = self._client.build_request(
            method, url=url, content=content, data=data, json=json, params=params, **kwargs)
        self.last_request = req
        response = await self._client.send(req)
        self.last_response = response
        # TODO: come up with a better solution for this
        for i in range(5):
            if self.retry_on_error_401 and response.status_code == 401:
                logging.debug('401, retry {0}'.format(i + 1))
                time.sleep(self.retry_on_error_401_wait * i)
                await self.authenticate()
                self.reauthentication_counter += 1
                response = await self._client.send(req)
                self.last_response = response
        return response


    async def get(self, url: URLType, *, params: Optional[Mapping[str, Any]] = None) -> Response:
        return await self.request('GET', url, params=params)


    async def post_body(self, url: URLType, *, content: Union[str, bytes, Iterable[bytes], AsyncIterable[bytes]], content_type: str = 'application/json', params: Optional[Mapping[str, Any]] = None) -> Response:
        return await self.request('POST', url, content=content, content_type=content_type, params=params)


    async def post_form(self, url: URLType, *, data: Optional[Mapping[str, Any]] = None, params: Optional[Mapping[str, Any]] = None) -> Response:
        return await self.request('POST', url, data=data, params=params)


    async def post(self, url: URLType) -> Response:
        return await self.request('POST', url)


    async def delete(self, url, **kwargs) -> Response:
        return await self.request('DELETE', url, **kwargs)


    async def get_bo_summary(self, *, busobid: Optional[BusObID] = None, busobname: Optional[str] = None) -> Optional[Summary]:
        if busobid is not None:
            response = await self.GetBusinessObjectSummaryByIdV1(busobid=busobid)
        elif busobname is None:
            raise TypeError(
                'get_bo_summary() missing 1 required argument: busobid or busobname')
        else:
            response = await self.GetBusinessObjectSummaryByNameV1(busobname=busobname)
        if len(response) == 0:
            return None
        assert len(response) == 1
        return response[0]


    async def get_busobid(self, busobname: str) -> Optional[BusObID]:
        summary = await self.get_bo_summary(busobname=busobname)
        if summary is None:
            return None
        return summary.busObId


    async def get_bo_summaries(self, type: BusinessObjectType) -> list[Summary]:
        return await self.GetBusinessObjectSummariesV1(type=type)


    # TODO: legacy, remove
    bo_name_to_id = get_busobid


    def get_bo(self, publicId, busObId=None, busObName=None):
        if busObId is None:
            busObId = self.bo_name_to_id(busObName)
        r = self.get(
            '/api/v1/getbusinessobject/busobid/{0}/publicid/{1}'.format(busObId, publicId))
        return r


    def get_related_bo(self, parentBusObId, parentBusObRecId, relationshipId):
        r = self.get('/api/v1/getrelatedbusinessobject/parentbusobid/{0}/parentbusobrecid/{1}/relationshipid/{2}'.format(
            parentBusObId, parentBusObRecId, relationshipId))
        return r


    def save_bo(self, bo_dict):
        req = bo_dict.save_change()
        self.last_save_bo_req = req
        if req is None:
            return None
        r = self.post('/api/v1/savebusinessobject', req)
        if r is None:
            return None
        bo_dict.clear_dirty()
        if bo_dict.busObRecId is None:
            bo_dict.busObRecId = r['busObRecId']
        if bo_dict.busObPublicId is None:
            bo_dict.busObPublicId = r['busObPublicId']
        return r


    def link_related_bo(self, parentBusObId, parentBusObRecId, relationshipId, busObId, busObRecId):
        r = self.get('/api/v1/linkrelatedbusinessobject/parentbusobid/{0}/parentbusobrecid/{1}/relationshipid/{2}/busobid/{3}/busobrecid/{4}'.format(
            parentBusObId, parentBusObRecId, relationshipId, busObId, busObRecId))
        return r


    def get_search_results_operator(self, bo_dict, op_dict, fields=None):
        change = bo_dict.save_change()
        search = {'busObId': change['busObId']}
        if fields is not None:
            field_ids = []
            for field in fields:
                if 'BO:' in field:
                    field_ids.append(field)
                else:
                    field_ids.append(bo_dict.fieldIds[field])
            search['fields'] = field_ids
        filters = []
        search['filters'] = filters
        for field in change['fields']:
            op = op_dict.get(field['name'], op_dict.get(
                field['fieldId'], 'eq'))
            filters.append(
                {'fieldId': field['fieldId'], 'value': field['value'], 'operator': op})
        search['pageSize'] = 100000
        self.last_search = search
        r = self.post('/api/v1/getsearchresults', search)
        return r


    def get_search_results_eq(self, bo_dict, fields=None):
        return self.get_search_results_operator(bo_dict=bo_dict, op_dict={}, fields=fields)
