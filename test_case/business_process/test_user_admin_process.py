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

data={}

#注册

def test_user_register():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'

    username = "xuepl33457"
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



#给用户分配角色

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

#登录

#获取当前登录用户信息
