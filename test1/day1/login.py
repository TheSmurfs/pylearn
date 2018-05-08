_author_ = "Alex Li"
import getpass

_username = 'alex'
_password = '123'
# 将用户输入的内容赋值给 name 变量
user = input("请输入用户名:")
#
pwd = input("请输入密码:")
if user == _username and pwd == _password:
    print("welcome user %s login"% user)
else:
    print("Wrong username or password")



print(user,pwd)
