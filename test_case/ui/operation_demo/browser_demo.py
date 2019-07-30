#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/30'

#浏览器的基本操作
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

if __name__ == '__main__':

    #打开
    driver = webdriver.Chrome(DRIVER_PATH)

    #调整浏览器窗口大小
    #最大化(推荐使用)
    driver.maximize_window()
    sleep(2)
    #自定义窗口分辨率(不推荐使用)
    #driver.set_window_size(1280,960)
    #打开网址
    driver.get("https://www.baidu.com/")
    sleep(2)
    driver.get("https://www.taobao.com/")
    sleep(2)
    driver.get("https://www.jd.com/")

    #后退
    driver.back()
    sleep(2)
    #前进
    driver.forward()
    sleep(2)
    #刷新
    driver.refresh()
    sleep(2)

    sleep(2)

    #关闭
    #关闭浏览器
    # driver.close()
    #退出驱动
    driver.quit()

