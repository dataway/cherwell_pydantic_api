import logging
import requests
import time



class CherwellConnection(object):

    def __init__(self, urlbase, client_id, username, password):
        self.urlbase = urlbase
        self.client_id = client_id
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.token = None
        self.raise_on_error_500 = False
        self.retry_on_error_401 = False
        self.retry_on_error_401_wait = 4.0
        self.reauthentication_counter = 0


    def authenticate(self):
        r = self.session.post(self.urlbase + '/token', data={
            'grant_type': 'password',
            'client_id': self.client_id,
            'username': self.username,
            'password': self.password })
        r.raise_for_status()
        self.token = r.json()['access_token']
        self.session.headers.update({'Authorization': 'Bearer ' + self.token})
        return self.token


    def logout(self):
        return self.delete('/api/v1/logout')


    def _make_url(self, url, **kwargs):
        return self.urlbase + url + '?locale=en-GB'


    def request(self, method, url, **kwargs):
        r = self.session.request(method, self._make_url(url), **kwargs)
        self.last_result = r
        if self.retry_on_error_401 and r.status_code == 401:
            logging.debug('401, retrying')
            time.sleep(self.retry_on_error_401_wait)
            self.authenticate()
            self.reauthentication_counter += 1
            r = self.session.request(method, self.urlbase + url, **kwargs)
            self.last_result = r
        if not self.raise_on_error_500 and r.status_code == 500:
            return None
        r.raise_for_status()
        return r

    def get(self, url, **kwargs):
        r = self.request('GET', url, **kwargs)
        if r is None or r.text == '':
            return None
        return r.json()


    def post(self, url, json, **kwargs):
        r = self.request('POST', url, json=json, **kwargs)
        if r is None or r.text == '':
            return None
        return r.json()


    def delete(self, url, **kwargs):
        r = self.request('DELETE', url, **kwargs)
        if r is None or r.text == '':
            return None
        return r.json()


    def bo_name_to_id(self, name):
        r = self.get('/api/v1/getbusinessobjectsummary/busobname/' + name)
        if len(r) == 0:
            return None
        if len(r) > 1:
            raise Exception('multiple results from getbusinessobjectsummary')
        return r[0]['busObId']


    def get_bo_schema(self, busObId=None, busObName=None, relationships=False):
        if busObId is None:
            busObId = self.bo_name_to_id(busObName)
        r = self.get('/api/v1/getbusinessobjectschema/busobid/' + busObId, params={'includerelationships': relationships})
        return r


    def get_bo(self, publicId, busObId=None, busObName=None):
        if busObId is None:
            busObId = self.bo_name_to_id(busObName)
        r = self.get('/api/v1/getbusinessobject/busobid/{0}/publicid/{1}'.format(busObId, publicId))
        return r


    def get_related_bo(self, parentBusObId, parentBusObRecId, relationshipId):
        r = self.get('/api/v1/getrelatedbusinessobject/parentbusobid/{0}/parentbusobrecid/{1}/relationshipid/{2}'.format(parentBusObId, parentBusObRecId, relationshipId))
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
        r = self.get('/api/v1/linkrelatedbusinessobject/parentbusobid/{0}/parentbusobrecid/{1}/relationshipid/{2}/busobid/{3}/busobrecid/{4}'.format(parentBusObId, parentBusObRecId, relationshipId, busObId, busObRecId))
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
            op = op_dict.get(field['name'], op_dict.get(field['fieldId'], 'eq'))
            filters.append({'fieldId': field['fieldId'], 'value': field['value'], 'operator': op})
        search['pageSize'] = 100000
        self.last_search = search
        r = self.post('/api/v1/getsearchresults', search)
        return r


    def get_search_results_eq(self, bo_dict, fields=None):
        return self.get_search_results_operator(bo_dict=bo_dict, op_dict={}, fields=fields)
