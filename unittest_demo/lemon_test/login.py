def login_check(username=None, password=None):
    if username != None and password != None:
        if username == 'python27' and password == 'lemonban':
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "mag": "所有的参数不能为空"}
