import unittest
import login
import ddt
import os
import openpyxl

"""
从Excel中读取的数据，期望转换为这种格式
datas = [
    {"user": "python27", "passwd": "lemonban", "check": {"code": 0, "msg": "登录成功"}},
    {"user": "python27", "passwd": "lemonban1", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python", "passwd": "lemonban", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python27", "passwd": None, "check": {"code": 1, "mag": "所有的参数不能为空"}},
    {"user": None, "passwd": "lemonban1", "check": {"code": 1, "mag": "所有的参数不能为空"}}
]
"""
# 方法一
# 获取到excel的绝对路径

getcwd = os.getcwd()
dirname = os.path.dirname(os.path.dirname(getcwd))
join = os.path.join(dirname, "excel.xlsx")
print(join)
wb = openpyxl.load_workbook(join)
sheet_login = wb["login"]


# rows = sheet_login.rows   为什么不能在这定义，给后面使用

# 得到字典的key，也就是表头
def fun1():
    titles = []
    for item in list(sheet_login.rows)[0]:
        # print(item.value)
        titles.append(item.value)
    # print(titles)
    # 把key和value组合在一起
    data_lists = []
    for item in list(sheet_login.rows)[1:]:
        value_dict = {}
        for index in range(len(item)):
            value_dict[titles[index]] = item[index].value
            # value_dict["check"]=eval(value_dict["check"])
        # print(value_dict)
        value_dict["check"] = eval(value_dict["check"])
        data_lists.append(value_dict)
    print(data_lists)


# 方法二
data_list = []
titles = []
for item in list(sheet_login.rows)[0]:
    titles.append(item.value)
# print(titles)

for item in list(sheet_login.rows)[1:]:
    values = []
    for val in item:
        values.append(val.value)
    # print(values)
    z = dict(zip(titles, values))
    z["check"] = eval(z["check"])
    # print(z)
    data_list.append(z)
# print(data_list)




@ddt.ddt
class TestLogin(unittest.TestCase):
    @ddt.data(*data_list)
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
