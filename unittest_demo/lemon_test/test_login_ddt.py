import unittest
import login
import ddt

datas = [
    {"user": "python27", "passwd": "lemonban", "check": {"code": 0, "msg": "登录成功"}},
    {"user": "python27", "passwd": "lemonban1", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python", "passwd": "lemonban", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python27", "passwd": None, "check": {"code": 1, "mag": "所有的参数不能为空"}},
    {"user": None, "passwd": "lemonban1", "check": {"code": 1, "mag": "所有的参数不能为空"}}
]

@ddt.ddt
class TestLogin(unittest.TestCase):
    @ddt.data(*datas)
    def test_login(self, case):
        res = login.login_check(case["user"], case["passwd"])
        self.assertEqual(res, case["check"])

    # def test_login_ok(self):
    #     res = login.login_check("python27", "lemonban")
    #     # assert res == {"code": 0, "msg": "登录成功"}
    #     self.assertEqual(res, {"code": 0, "msg": "登录成功"})
    #
    # def test_login_wrong_passwd(self):
    #     res = login.login_check("python27", "lemonban1")
    #     self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
    #
    # def test_login_wrong_user(self):
    #     res = login.login_check("python", "lemonban")
    #     self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
    #
    # def test_login_no_passwd(self):
    #     res = login.login_check("python27", None)
    #     self.assertEqual(res, {"code": 1, "mag": "所有的参数不能为空"})
    #
    # def test_login_no_user(self):
    #     res = login.login_check(None, "lemonban1")
    #     self.assertEqual(res, {"code": 1, "mag": "所有的参数不能为空"})
