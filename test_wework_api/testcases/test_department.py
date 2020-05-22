from test_wework_api.api.department import Department
from test_wework_api.utils.Utils import Utils


class TestDepartment:
    department = Department()

    def test_list(self):
        # 获取部门列表信息
        # self.department = Department()
        d = self.department.list("")
        # print(Utils.json_format(d))
        assert d["errcode"] == 0
        assert d["department"][0]["name"] == "不止测试"

    def test_create(self):
        r = self.department.create("1002", 1, 100000001, 7)
        assert r["errcode"] == 0
        assert r["id"] is not None
        exist = False
        for depart in self.department.list("")["department"]:
            if depart["id"] == r["id"]:
                exist = True
        assert exist == True

    def test_delete(self):
        r = self.department.delete(6)
        assert r["errcode"] == 0
        assert r["errmsg"] == "deleted"
        d = self.department.list("")
        dele = False
        for d in d["department"]:
            if d["id"] != 6:
                dele = True
        return dele == True
