import pytest                                               
                                                            
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

@pytest.fixture(scope='session')
def driver_data():
    return d