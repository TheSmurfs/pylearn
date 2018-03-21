#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/3/13 15:10
# software: PyCharm

import copy

names = "ZhangYang Guyun Xiangpeng XuLianChen"
names = ["ZhangYang","Guyun","Xiangpeng","XuLianChen"]
print(names[0])
print(names[1:3])#切片

person=['name',['a','100']]

p1=copy.copy(person)
p2=person[:]
p3=list(person)
