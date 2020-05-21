import requests

from test_wework_api.api.BaseApi import BaseApi
from test_wework_api.api.wework import WeWork
from test_wework_api.utils.Utils import Utils


class Department(BaseApi):
    list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"

    def list(self, id=None):
        r = requests.get(self.list_url, params={"access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def create(self, name, parentid, order, id):
        r = requests.post(self.create_url,
                          params={"access_token": WeWork.get_token()},
                          json={
                              "name": name,
                              "parentid": parentid,
                              "order": order,
                              "id": id}
                          ).json()
        self.verbose(r)
        return r

    def delete(self, id):
        r = requests.get(self.delete_url, params={"access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def update(self):
        pass
