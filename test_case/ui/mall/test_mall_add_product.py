#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep


def test_login(base):
    #打开登录界面 http://qa.yansl.com/#/login
    base.get("打开登录界面",'http://qa.yansl.com/#/login')
    #输入用户名 //input[@name="username"]
    base.send_keys("输入用户名",'''//input[@name="username"]''',"admin")
    #输入密码 //input[@name="password"]
    base.send_keys("输入密码",'''//input[@name="password"]''',"123456")
    #点击登录 (//span[contains(text(),'登录')])[1]
    base.click("点击登录","(//span[contains(text(),'登录')])[1]")
    try:
        #点击残忍拒绝 //span[text()='残忍拒绝']
        base.click("点击残忍拒绝",'''//span[text()='残忍拒绝']''')
        # 点击登录 (//span[contains(text(),'登录')])[1]
        base.click("点击登录", "(//span[contains(text(),'登录')])[1]")
    except:
        pass
    sleep(5)
    #断言 页面跳转至首页


