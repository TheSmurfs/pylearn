#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2018/3/15 19:19
# software: PyCharm

'''
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

av_catalog["大陆"]["1024"][1] = "可以用爬虫爬下来"
print(av_catalog["大陆"]["1024"])
#ouput
['全部免费,真好,好人一生平安', '服务器在国外,慢,可以用爬虫爬下来']
'''

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

#方法1
for key in info:
    print(key,info[key])

#方法2
for k,v in info.items(): #会先把dict转成list,数据里大时莫用
    print(k,v)