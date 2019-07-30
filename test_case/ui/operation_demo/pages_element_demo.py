#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/30'
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from config.conf import DRIVER_PATH



driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器窗口大小
# 最大化(推荐使用)
driver.maximize_window()

def get_url():
    driver.get("E:\\softwaredata\\python\\gy-api-1906A\\demo.html")
def text_demo():
    #文本输入框
    #操作页面元素
    #定位元素 //input[@type="text"]
    text = driver.find_element_by_xpath('//input[@type="text"]')
    text.clear()
    #输入
    text.send_keys("我是谁？我在哪？我要干什么？")
    #获取value属性的值
    print(text.get_attribute("value"))

def file_demo():
    #文件上传框
    #操作页面元素
    file = driver.find_element_by_xpath("//input[@type=\"file\"]")
    #操作页面元素
    file.clear()
    file.send_keys("D:\\1.png")
    print(file.get_attribute("value"))
def radio_demo():
    radio = driver.find_element_by_xpath('//input[@name="radio"][1]')
    radio.click()
def checkbox():
    checkbox1 = driver.find_element_by_xpath("//input[@type = 'checkbox'][1]")
    checkbox1.click()
    checkbox2 = driver.find_element_by_xpath("//input[@type = 'checkbox'][3]")
    checkbox2.click()
    sleep(2)
def button_demo():
    button = driver.find_element_by_xpath('//input[@type="button"]')

    button.click()

def password_demo():
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.clear()
    # 输入
    password.send_keys("sdfhisdhfi")

def number_demo():
    number = driver.find_element_by_xpath('//input[@type="number"]')
    number.clear()
    # 输入
    number.send_keys("12168")

def date_demo():
    js ='''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)

def time_demo():
    t = driver.find_element_by_xpath('//input[@type="time"]')
    t.clear()
    t.send_keys('17:03')
def textarea_demo():
    textarea = driver.find_element_by_xpath("//textarea")
    textarea.clear()
    textarea.send_keys("hello world")

def select_demo():
    # select= driver.find_element_by_xpath("//select/option[2]")
    # select.click()
    s = driver.find_element_by_xpath("//select")
    select1 = Select(s)
    select1.select_by_index(2)
    sleep(2)
    select1.select_by_value("z2")
    sleep(2)
    select1.select_by_visible_text("周龙1")
    sleep(2)
def a_demo():
    #通过连接文本精确定位
    # a = driver.find_element_by_link_text("当当")
    # a.click()
    # sleep(5)
    # driver.back()
    #通过连接文本模糊定位
    baidu = driver.find_element_by_partial_link_text('度娘')
    actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).click(baidu).key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.SHIFT).click(baidu).key_up(Keys.SHIFT).perform()
    sleep(2)





if __name__ == '__main__':
    get_url() #打开网址
    sleep(1)
    # text_demo()#文本框输入
    # sleep(1)
    # file_demo()#文件上传
    # sleep(2)
    # radio_demo()#单选框操作
    # sleep(2)
    # checkbox()#多选框操作
    # sleep(2)
    # # button_demo()#按钮操作
    # # sleep(2)
    # password_demo()#密码输入框操作
    # sleep(2)
    # number_demo()#数字输入框操作
    # sleep(2)
    # date_demo()#日期控件操作
    # sleep(2)
    # time_demo()#时间控件操作
    # sleep(2)
    # textarea_demo()#文本输入域操作
    # sleep(2)
    # select_demo()#下拉框操作
    a_demo()#超链接demo
    sleep(2)
    driver.quit()#关闭浏览器

