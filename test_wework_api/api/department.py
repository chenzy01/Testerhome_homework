import requests

from test_wework_api.api.base_api import BaseApi
from test_wework_api.api.wework import WeWork
from test_wework_api.utils.Utils import Utils


class Department(BaseApi):
    list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def list(self, id=None):
        self.json_data = requests.get(self.list_url, params={"access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(self.json_data)
        return self.json_data

    def create(self, name, parentid, order, id=None):
        self.json_data = requests.post(self.create_url,
                          params={"access_token": WeWork.get_token()},
                          json={
                              "name": name,
                              "parentid": parentid,
                              "order": order,
                              "id": id}
                          ).json()
        self.verbose(self.json_data)
        return self.json_data

    def delete(self, id):
        r = requests.get(self.delete_url, params={"access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def update(self):
        pass
