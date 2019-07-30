import random
import re

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


d = {
  "code": "自动生成 数字 20,80",
  "message": "自动生成 字符串 3,8 中文 xuepl",
  "data": {
    "total": "自动生成 地址",
    "totalPage": "自动生成 姓名",
    "pageSize": "自动生成 手机号",
    "list": [
      {
        "id": "自动生成 邮箱",
        "memberId": 1,
        "couponId": 2,
        "orderSn": "201809150101000001",
        "createTime": 1537014267000,
        "memberUsername": "test",
        "totalAmount": 18732,
        "payAmount": 16377.75,
        "freightAmount": 20,
        "promotionAmount": 2344.25,
        "integrationAmount": 0,
        "couponAmount": 10,
        "discountAmount": 10,
        "payType": 0,
        "sourceType": 1,
        "status": 4,
        "orderType": 0,
        "deliveryCompany": "",
        "deliverySn": "",
        "autoConfirmDay": 15,
        "integration": 13284,
        "growth": 13284,
        "promotionInfo": "单品促销,打折优惠：满3件，打7.50折,满减优惠：满1000.00元，减120.00元,满减优惠：满1000.00元，减120.00元,无优惠",
        "billType": None,
        "billHeader": None,
        "billContent": None,
        "billReceiverPhone": None,
        "billReceiverEmail": None,
        "receiverName": "大梨",
        "receiverPhone": "18033441849",
        "receiverPostCode": "518000",
        "receiverProvince": "江苏省",
        "receiverCity": "常州市",
        "receiverRegion": "天宁区",
        "receiverDetailAddress": "自动生成 字符串 3,8 数字",
        "note": "xxx",
        "confirmStatus": 0,
        "deleteStatus": 0,
        "useIntegration": None,
        "paymentTime": None,
        "deliveryTime": None,
        "receiveTime": None,
        "commentTime": None,
        "modifyTime": 1540910629000
      }
    ],
    "pageNum": 1
  }
}
en = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
num = [ str(i) for i in range(10)]
zf = list(str(bytes([0x60, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d,
                                  0x2e, 0x2f, 0x3c, 0x3e, 0x3f, 0x40, 0x5b, 0x5c, 0x5d, 0x5e, 0x5f, 0x7b, 0x7c, 0x7d,
                                  0x7e, 0x60])))
zw = [bytes.fromhex(f'{head:x}{body:x}').decode('gb2312') for head in range(0xb0, 0xf7,0x01) for body in range(0xa1, 0xf9,0x01)]
def get_length(s):
    length = 1
    l = s.split(",")
    if (len(l) == 1):
        length = int(l[0])
    elif (len(l) == 2 and (l[0] != '' or l[1] != '')):
        if (l[0] != '' and l[1] != ''):
            length = random.randint(int(l[0]), int(l[1]))

        elif (l[0] == ''):
            length = random.randint(1, int(l[1]))
        else:
            length = random.randint(int(l[0]), 9999)
    else:
        pass
    return length
def get_str(length,ll):
    l = []
    limits = ll[0]
    if (limits.find("字母") != -1):
        l += en
    if (limits.find("数字") != -1):
        l += num
    if (limits.find("特殊字符") != -1):
        l += zf
    if (limits.find("中文") != -1):
        l += zw
    value = ''
    if (len(l) != 0):
        for i in range(length):
            value +=  l[random.randint(0, len(l) - 1)]
    if len(ll) == 2:
        value = ll[1] + value
    return value

def replace_data(s):
    value = ""
    s_l = s.split(" ")
    if(s_l[1].find('字符') != -1 or s_l[1].find('string') != -1):
        s_l[2] = s_l[2].replace('，',',')
        length = get_length(s_l[2])
        value = get_str(length,s_l[3:])
    elif (s_l[1].find("地址") != -1):
        value = random_tool.random_addr()
    elif (s_l[1].find("手机") != -1):
        value = random_tool.random_tell()
    elif (s_l[1].find("邮箱") != -1):
        value = random_tool.random_email()
    elif (s_l[1].find("姓名") != -1):
        value = random_tool.random_name()
    elif (s_l[1].find("数字") != -1):
        s_l[2] = s_l[2].replace('，', ',')
        value = get_length(s_l[2])
    elif (s_l[1].find("身份证") != -1):
        value = random_tool.random_id_num()
    else:
        value = None
    return value







def update_dict(d):
    if(d is None):
        return None
    if(isinstance(d,dict)):
        for key in d:
            if(isinstance(d[key],str) and d[key].startswith("自动生成")):
                d[key] = replace_data(d[key])
            if(isinstance(d[key],dict)):
                update_dict(d[key])
            if(isinstance(d[key],list)):
                update_dict(d[key])
    if (isinstance(d, list)):
        for i in range(len(d)):
            if (isinstance(d[i], str) and d[i].startswith("自动生成")):
                d[i] = replace_data(d[i])
            if (isinstance(d[i], dict)):
                update_dict(d[i])
            if (isinstance(d[i], list)):
                update_dict(d[i])
    return d



if __name__ == '__main__':
    print(update_dict(d))


