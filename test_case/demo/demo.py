#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻┓ 
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻   ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗┓┓┏━┳┓┏┛
               ┃┫┫  ┃┫┫
               ┗┻┛  ┗┻┛
"""



#发送请求，用到的技术
#安装或者引入
#使用别人写好的代码。首先要导包


#发送请求的包名，工具，框架-requests
#安装包
#导入
import random

import requests
#发送post json请求
# url = "http://qa.yansl.com:8080/admin/login"
# data = {
#   "password": "123456",
#   "username": "admin"
# }
# r = requests.post(url, json=data)
# print(r.text)

# #发送post 键值对请求
# para = {"adminId":42,"roleIds":[1,2,3,4]}
# r = requests.post("http://qa.yansl.com:8080/admin/role/update", data=para)
# print(r.text)

#发送get请求，键值对格式的数据

# #get请求传数据，params
# param = {"name":"admin","pageSize":5,"pageNum":1}
#
# response = requests.get("http://qa.yansl.com:8080/admin/list", params=param)
# print(response.text)
#
#
# a = {"orderSn":44,"receiverKeyword":222,"status":222,"orderType":222,"sourceType":222,"createTime":222,"pageSize":222,"pageNum":222}
#




def random_string(length=10):
    extent="abcdefghijklmnopqrstuvwxyz1234567890"
    s = ''
    l = len(extent)
    for i in range(length):
        index = random.randint(0, l-1)
        s+=extent[index]
    print(s)
    return s
random_string()

#测试框架 pytest 控制用例的执行

#使用安装pytest
#修改pycharm中默认执行框架 file->settings->tools->python integrated Tools->default test runner修改成pytest
#文件命名 test_开头，用例名命名 test_

#pytest执行用例的方法
'''
1、执行单个用例
pytest.main(['-v','test_case/demo/test_demo2.py::test_333'])
2、执行一个python文件
pytest.main(['-v','test_case/demo/test_demo2.py'])
3、执行一个包里边所有python文件
pytest.main(['-v','test_case/demo/'])
4、执行全部用例
pytest.main(['-v'])
5、执行指定的用例
 1)、给用例打标记
 @pytest.mark.标记名
 2)、执行用例
 pytest.main(['-v','-m','标记名'])


'''

