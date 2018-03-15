#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/3/14 15:41
# software: PyCharm

salary = input("请输入工资:")

product_list = [
    ('Iphone',5800),
    ('mac',9800),
    ('bike',800),
    ('watch',5800),
    ('coffee',31),
    ('alex',100)
]

shopping_list = []

if salary.isdigit() :
    salary = int(salary)
    while True:
        for item in product_list:
            print(product_list.index(item),item)
        user_choice = input("选择要买吗>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -=p_item[1]
                    print("added %s into shopping cart ,your current balance is %s" %(p_item,salary))
        elif user_choice =='q':
            print('exit......')
        else:
            print("invalid option")