import os

GY_API_URL = 'http://qa.yansl.com:8080'#相当于jmeter中的http请求默认值

GY_WEB_URL = "http://qa.yansl.com" #web首页的网址

GY_DB_URL = {                               
    'host': 'qa.guoyasoft.com',             
    'port': 3306,                           
    'db': 'guoya_virtual_mall_1811',
    'user': 'root',                         
    'passwd': 'Guoya006',                   
    'charset': 'utf8'                       
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}

#设置driver的绝对路径
DRIVER_PATH = os.path.join(os.path.dirname(__file__), "../chrome_driver_v75/chromedriver.exe")