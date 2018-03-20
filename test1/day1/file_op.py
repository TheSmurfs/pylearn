#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/3/19 15:53
# software: PyCharm

#data = open("file.txt",encoding="utf-8").read()
f = open("file.txt",'r',encoding="utf-8")#文件句柄
#data = f.read()
#print(data)
#f.write("我爱毕竟天安门")


print(f.readline())
