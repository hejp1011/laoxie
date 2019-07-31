#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

driver = webdriver.Chrome(DRIVER_PATH)
# 调整浏览器窗口大小
# 最大化(推荐使用)
driver.maximize_window()

def get_url():
    driver.get("E:\\softwaredata\\python\\gy-api-1906A\\demo.html")


def open_a():
    baidu = driver.find_element_by_partial_link_text("度娘")
    jd = driver.find_element_by_partial_link_text('京东')
    dd = driver.find_element_by_partial_link_text('当当')

    actions = ActionChains(driver)
    driver.get_screenshot_as_file()
    sleep(10)

def windows_change_demo():
    #获取所有窗口的句柄
    handles = driver.window_handles
    #使用for循环根据窗口句柄来切换窗口
    for h in handles:
        print(h)
        driver.switch_to.window(h)
        sleep(2)
        #根据窗口的title来判断当前页面，如果包含我们想要的页面title，就停止切换
        if(driver.page_source.__contains__('百度一下')):
            break


def open_alert():
    # driver.find_element_by_xpath('//input[@type="reset"]').click()
    driver.find_element_by_xpath('//input[@type="button"]').click()
def alert_alert_demo():
    a = driver.switch_to.alert
    #确认
    # a.accept()
    a.send_keys("hello")
    a.dismiss()


if __name__ == '__main__':
    get_url()
    sleep(2)
    # open_a()
    # windows_change_demo()
    open_alert()

    sleep(2)
    alert_alert_demo()
    sleep(2)
    driver.quit()