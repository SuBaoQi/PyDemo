import unittest
import login


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        print("开始")

    def tearDown(self) -> None:
        print("结束")
    @classmethod
    def setUpClass(cls) -> None:
        print("开始执行一次")
    @classmethod
    def tearDownClass(cls) -> None:
        print("结束执行一次")

    def test_login_ok(self):
        res = login.login_check("python27", "lemonban")
        # assert res == {"code": 0, "msg": "登录成功"}
        self.assertEqual(res, {"code": 0, "msg": "登录成功"})

    def test_login_wrong_passwd(self):
        res = login.login_check("python27", "lemonban1")
        self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})

    def test_login_wrong_user(self):
        res = login.login_check("python", "lemonban")
        self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})

    def test_login_no_passwd(self):
        res = login.login_check("python27", None)
        self.assertEqual(res, {"code": 1, "mag": "所有的参数不能为空"})

    def test_login_no_user(self):
        res = login.login_check(None, "lemonban1")
        self.assertEqual(res, {"code": 1, "mag": "所有的参数不能为空"})
