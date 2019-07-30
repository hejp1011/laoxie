#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf




@allure.feature('后台用户管理')
@allure.story("给用户分配角色")
def test_product_category_add():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    #接口地址
    uri = '/admin/role/update'
    #请求数据，字典格式
    req = {"adminId":40,"roleIds":[1,2,3,4]}
    header = {}
    resp = request_tool.post_request(uri,headers=header,data=req)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果：{} ,预期结果为：200".format(resp.status_code)):pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    #预期结果  字符串或者数字
    expect = 4
    #实际结果，从字典body中取值例：body['data']
    actual = body['data']
    with allure.step("断言code，实际结果：{} ,预期结果为：{}".format(actual,expect)): pass
    assert_tool.assert_equal(actual, expect)


@allure.feature('后台用户管理')
@allure.story("用户登录")
def test_product_category_add():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    #接口地址
    uri = '/admin/login'
    #请求数据，字典格式
    req = {
  "password": "string",
  "username": "string"
}
    header = {}
    resp = request_tool.post_request(uri,headers=header,json=req)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果：{} ,预期结果为：200".format(resp.status_code)):pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    #预期结果  字符串或者数字
    expect = 200
    #实际结果，从字典body中取值例：body['code']
    actual = body['code']
    with allure.step("断言code，实际结果：{} ,预期结果为：{}".format(actual,expect)): pass
    assert_tool.assert_equal(actual, expect)



@allure.feature('后台用户管理')
@allure.story("修改指定用户信息")
def test_product_category_add():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    #接口地址  value替换uri中的{}
    uri = '/admin/update/{}'.format(40)
    #请求数据，字典格式
    req = {
  "createTime": "2019-07-27T13:03:22.970Z",
  "email": "string",
  "icon": "string",
  "id": 0,
  "loginTime": "2019-07-27T13:03:22.970Z",
  "nickName": "string",
  "note": "string",
  "password": "string",
  "status": 0,
  "username": "string"
}
    header = {}
    resp = request_tool.post_request(uri,headers=header,json=req)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果：{} ,预期结果为：200".format(resp.status_code)):pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    #预期结果  字符串或者数字
    expect = 500
    #实际结果，从字典body中取值例：body['code']
    actual = body['code']
    with allure.step("断言code，实际结果：{} ,预期结果为：{}".format(actual,expect)): pass
    assert_tool.assert_equal(actual, expect)



###########excel模板填写说明################
# test_case	用例名称
# uri	    接口地址
# datas	    请求数据，不管什么请求统一用json格式
# headers	请求头中需要添加的内容，json格式，不用添加直接给{}
# expect    预期结果
#############################################
#文件路径样例：data/demo/excel_demo.xlsx
data = excel_tool.get_test_case('data/demo/add_product_category.xlsx')
@pytest.mark.parametrize('uri,datas,headers,expect',data[1],ids=data[0])
@allure.feature('商品分类')
@allure.story("添加商品分类")
def test_product_category_add(uri,datas,headers,expect):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    req = json.loads(datas)
    if (headers != ''):
        header = json.loads(headers)
    else:
        header = {}
    resp = request_tool.post_request(uri,headers=header,json=req)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果：{} ,预期结果为：200".format(resp.status_code)):pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    #实际结果，从字典body中取值例：body['code']
    actual = body['code']
    with allure.step("断言code，实际结果：{} ,预期结果为：{}".format(actual,expect)): pass
    assert_tool.assert_equal(actual, expect)

