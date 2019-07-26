#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/26'
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



def test_change_pwd_var(token):
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/productCategory/create'
    req = {
  "description": "a",
  "icon": "http://img5.imgtn.bdimg.com/it/u=3300305952,1328708913&fm=26&gp=0.jpg",
  "keywords": "s",
  "name": "车",
  "navStatus": 0,
  "parentId": 0,
  "productAttributeIdList": [
    1
  ],
  "productUnit": "件",
  "showStatus": 0,
  "sort": 0
}
    headers = {
        'Authorization': token,
        'charset': 'UTF-8'
    }
    resp = request_tool.post_request(url, json=req, headers=headers)
    body = resp.json()
    with allure.step("断言响应状态码，实际结果：{} ,预期结果为：200".format(resp.status_code)):pass
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言code，实际结果：{} ,预期结果为：{}".format(body['code'],200)): pass
    assert_tool.assert_equal(body['code'], 200)

