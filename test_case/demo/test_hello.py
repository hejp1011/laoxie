# # -*- coding:utf-8 -*-
# # Author : 小吴老师
# # Data ：2019/7/18 19:23
# import allure
# import json
#
#
# @allure.epic('一级归类')
# @allure.feature('二级归类')
# @allure.story('三级归类')
# def test_hello_world():
#     print('hello world !')
#     request = {
#         'pwd': 'a123456',
#         'userName': '13s32'
#     }
#     allure.attach(json.dumps(request,ensure_ascii=False,indent=4), '请求', allure.attachment_type.TEXT)
#
#     response = {
#         'code': 2000,
#         'message': '登录成功',
#         'data': {
#             'token': 'eyJ0aW1lT3V0IjoxNTYzNDUxMjg4MjY3LCJ1c2VySWQiOjQwMywidXNlck5hbWUiOiIxM3MzMiJ9',
#             'userName': '13s32'
#         }
#     }
#     allure.attach(json.dumps(response,ensure_ascii=False,indent=4), '响应', allure.attachment_type.TEXT)


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



def test_change_pwd_var(driver_data):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/user/changepwd'
    pwd = random_tool.random_pwd()
    req = {
        "newPwd": pwd,
        "oldPwd": driver_data['pwd'],
        "reNewPwd": pwd,
        "userName": driver_data['user_name']
    }
    headers = {
        'token': driver_data['token'],
        'charset': 'UTF-8'
    }
    resp = request_tool.post_request(url, json=req, headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['code'], 2000)



