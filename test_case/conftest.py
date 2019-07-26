

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


                                                            
d = {'pwd':'123456','user_name':'admin','token':'123567'}

@pytest.fixture(scope='session')                            
def pub_dic():                                              
    data = {'token':'asdfasdfjsldkfjlsxllkj'}               
    return data                                             
                                                            
                                                            
@pytest.fixture(scope='session')                            
def pub_list():                                             
    data = ['张三','zhangsan',30,'男','aaa123']             
    return data                                             
                                                            
                                                            
@pytest.fixture(scope='session')                            
def pub_var():                                              
    token = 'xxxxsdfsdfjkllwklewe'                          
    return token                                            


@pytest.fixture(scope="session")
def token():
    url = conf.GY_API_URL + '/admin/login'
    req = {
        "password": "123456",
        "username": "admin"
    }

    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']['tokenHead'], "Bearer ")
    return body['data']['tokenHead'] + body['data']['token']
