

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



@pytest.fixture(scope="session",autouse=True)
def set_token():
    url = '/admin/login'
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
    conf.HEADERS["Authorization"] = body['data']['tokenHead'] + body['data']['token']



'''
sessoin 
    每次运行脚本前只执行一次，整个用例运行期间，只执行一次
module
    可以把一个.py文件看作一个module,只要执行.py文件内的测试用例，就会先执行一次
class
    只要执行到一个类里边的测试用例，会先执行一次
function
    每个测试用例执行之前，都会执行一次
'''
@pytest.fixture(scope="session")
def session_demo():
    print('session_demo')

@pytest.fixture(scope="module")
def module_demo():
    print('module')

@pytest.fixture(scope="class")
def class_demo():
    print('class')

@pytest.fixture(scope="function")
def function_demo():
    print('function')



# 在terminal控制台输入命令：
# pip install --upgrade guoya-api-test