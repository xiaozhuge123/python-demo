users = {
    '小红':{'name':'小红','passwd':'123','status':True},
    'jack':{'name':'jack','passwd':'123','status':True},
    'jim': {'name': 'jim', 'passwd': '123', 'status': False}
}
for i in range(3):
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if name in users and users[name]['passwd'] == pwd and users[name]['status']:
        print(name , '登录成功')
        break
    elif name in users and users[name]['passwd'] != pwd:
        print(name,'请输入正确的密码')
    elif name in users and not users[name]['status']:
        print(name,'你的账号不可用')
    else:
        print('你的账号不存在，请注册')