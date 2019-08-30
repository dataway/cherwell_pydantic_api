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
        r.raise_for_status()
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

