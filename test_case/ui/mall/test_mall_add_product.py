#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep
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

@allure.feature("添加商品流程")
@allure.story('登录')
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
    # f = False
    # try:
    #     base.local_element("//span[text()='首页']")
    #     f = True
    # except:
    #     pass
    # assert_tool.assert_equal(f,True)
    #获取页面源代码
    sleep(2)
    page_source = base.driver.page_source
    with allure.step("登录界面跳转断言"):
        allure.attach(page_source,"实际结果",allure.attachment_type.TEXT)
        allure.attach('首页', "预期结果", allure.attachment_type.TEXT)


    assert_tool.assert_in(page_source,'首页')

    #断言 页面跳转至首页
@allure.feature("添加商品流程")
@allure.story('打开添加商品页面-添加商品信息')
def test_add_product(base):
    # 点击商品 (//span[contains(text(),'商品')])[1]
    base.click("点击商品",'''(//span[contains(text(),'商品')])[1]''')
    # 点击添加商品 //span[contains(text(),'添加商品')]
    base.click("点击添加商品",'''//span[contains(text(),'添加商品')]''')
    # 点击商品分类 //label[contains(text(),'商品分类')]/../div//input
    base.click("点击商品分类","""//label[contains(text(),'商品分类')]/../div//input""")
    # 点击下拉框第一个选项 //ul[@role='menu' and contains(@id,'cascader-menu')]/li[1]
    base.click("点击下拉框第一个选项","//ul[@role='menu' and contains(@id,'cascader-menu')]/li[1]")
    # 点击二级下拉菜单第一个选项  //li[@role='menuitem' and contains(@id,'menu-')][1]
    base.click("点击二级下拉菜单第一个选项",'''//li[@role='menuitem' and contains(@id,'menu-')][1]''')
    # 填写商品名称 //label[contains(text(),'商品名称')]/../div//input
    base.send_keys("填写商品名称","//label[contains(text(),'商品名称')]/../div//input","小米11")
    # 填写副标题 //label[contains(text(),'副标题')]/../div//input
    base.send_keys("填写副标题",'''//label[contains(text(),'副标题')]/../div//input''','手机')
    # 点击商品品牌 //label[contains(text(),'商品品牌')]/../div//input
    base.click("点击商品品牌","""//label[contains(text(),'商品品牌')]/../div//input""")
    # 点击下拉菜单中第一个选项 (//ul[@class="el-scrollbar__view el-select-dropdown__list"])[2]/li[1]
    base.click("点击下拉菜单中第一个选项","""(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[2]/li[1]""")
    # 滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品促销 //span[text()='下一步，填写商品促销']
    base.click("点击下一步，填写商品促销",'''//span[text()='下一步，填写商品促销']''')
    #滚动窗口
    base.scroll_screen("滚动窗口")
    #点击下一步，填写商品属性//span[text()='下一步，填写商品属性']
    base.click("点击下一步，填写商品属性", '''//span[text()='下一步，填写商品属性']''')
    #滚动窗口
    base.scroll_screen("滚动窗口")
    # # #切换窗口至iframe
    # base.switch_to_frame("切换窗口至iframe ",'(//iframe)[1]')
    #
    # #输入电脑端详情   //body/p
    # base.send_keys("#输入电脑端详情 ","//body",'测试数据')
    # #切出iframe
    # base.switch_to_content("切出iframe")

    # 点击下一步，选择商品关联
    base.click("点击下一步，选择商品关联", '''//span[text()='下一步，选择商品关联']''')
    base.click("点击完成，提交商品",'''//span[text()='完成，提交商品']''')
    base.click("点击确定",'''//span[contains(text(),'确定')]/..''')

    sleep(10)


    pass


