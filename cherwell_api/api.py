import logging
import requests



class CherwellConnection(object):

    def __init__(self, urlbase, client_id, username, password):
        self.urlbase = urlbase
        self.client_id = client_id
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.token = None
        self.raise_on_error_500 = False


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


    def get(self, url, **kwargs):
        r = self.session.get(self.urlbase + url, **kwargs)
        self.last_result = r
        if not self.raise_on_error_500 and r.status_code == 500:
            return None
        r.raise_for_status()
        if r.text == '':
            return None
        return r.json()


    def post(self, url, json, **kwargs):
        r = self.session.post(self.urlbase + url, json=json, **kwargs)
        self.last_result = r
        if not self.raise_on_error_500 and r.status_code == 500:
            return None
        r.raise_for_status()
        if r.text == '':
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
        return r


    def link_related_bo(self, parentBusObId, parentBusObRecId, relationshipId, busObId, busObRecId):
        r = self.get('/api/v1/linkrelatedbusinessobject/parentbusobid/{0}/parentbusobrecid/{1}/relationshipid/{2}/busobid/{3}/busobrecid/{4}'.format(parentBusObId, parentBusObRecId, relationshipId, busObId, busObRecId))
        return r

