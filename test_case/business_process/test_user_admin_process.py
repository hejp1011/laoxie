#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/25'
        .@@\.                                   
        // ,@`                              .]. 
       ,@./O.\\                          ./@[=@.
       =/=OOO`\\.                      ./@`]^=@^
      ,@`OOOOO\=@]]@@@@@@@@@\]]]..   .//./OOO=@.
      //=OO@@@@@@@@@@@@@@@@@@@@@@@@@@@\OOOOOO=@.
     .@`=@@@@@@@@@@@@@@@[@@@@@@@@@@@@@@@@@OOO=@ 
     =@/@@@@@@@@@@@O\@@`.=@@@@@@@@@@@@@@@@@O^=@ 
     \@@@@@@@@@@@@@@\@@`,@@^,O@@@@@@@@@@@@@@`@^ 
    ,@`.=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^ 
   ,@`  ,@.   .[` .//[@@@@OO@@@@@@@@@@@@@@@@@@. 
  .@^    .[@]..,]@/.   ,`   .@`   ... ,@`..[@@^ 
  =@.        ...    =@@[[@@^  ,@\]]]@@`      =@ 
  =@                \@@@@@@@                 =@.
  =@.                ,@@@@[.                 =@ 
  .@^                    .[@`               .@^ 
   ,@^              .@@@/\^,`               //  
    .\@].             .@.=^               ,@/   
       ,\@\]`.         \`@`           .,/@/.    
           =@[[[.       ,.    ,@@@@@@[[.        
   ,@@@@].=@.                      .@^  ,]@\`   
  ,@`   =@@`  .].                   ,@]@/. ,@^  
  .\@@^   .  .@^               .\\. .@/    ./@  
      \\.   ,@@.                 =@`    ./@[.   
       ,@@@@/=@                  .@@\]]@@`      
             =@                  .@^...         
             =@                  .@^            

"""

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

#接口串联
# 1、在文件最上边创建一个空字典
# 2、把接口响应中的数据取出来，存到这个空字典中
# 3、下个接口可以从这个字典中根据key取值

# 往请求头添加数据
# 1、创建一个字典，把需要添加的数据存入字典中
# 2、请求方法中使用headers=来传入请求头数据


#请求数据在请求地址里边
# 1、使用.format进行字符串格式化

data={}
#注册

@allure.feature("后台用户管理流程")
@allure.story('注册-新用户')
def test_user_register():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'

    username = "xuepl"+random_tool.random_str_abc(7)
    req = {
  "password": "123456",
  "username": username
}
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["username"], username)
    data["id"] = body['data']["id"]
    data['username'] = username



#给用户分配角色
@allure.feature("后台用户管理流程")
@allure.story('给用户分配角色：1，商品管理员。2，商品分类管理员。3、商品类型管理员。4、品牌管理员 ')
def test_user_update_role():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +'/admin/role/update'
    req = {
        "adminId": data['id'],
        "roleIds": [1,2,3,4]
    }
    resp = request_tool.post_request(url, data=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data'], 4)


#查询用户角色信息
@allure.feature("后台用户管理流程")
@allure.story('查询用户角色信息')
def test_user_get_role():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +'/admin/role/{}'.format(data["id"])
    resp = request_tool.get_request(url)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data'][0]['id'], 1)


#登录
@allure.feature("后台用户管理流程")
@allure.story('登录')
def test_user_login():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/login'
    req = {
  "password": "123456",
  "username": data['username']
}

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']['tokenHead'], "Bearer ")
    data['token'] = body['data']['tokenHead'] + body['data']['token']
#获取当前登录用户信息
@allure.feature("后台用户管理流程")
@allure.story('获取当前登录用户信息-根据token获取用户登录信息')
def test_user_info():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/info'
    headers = {
            'Authorization':data['token'],
            'charset':'UTF-8'
    }
    resp = request_tool.get_request(url,headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["username"], data["username"])

