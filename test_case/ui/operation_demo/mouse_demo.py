#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep

from selenium.webdriver import ActionChains


def test_mouse_demo(base):
    base.get("打开百度",'https://www.baidu.com/')
    baidu = base.local_element("""//*[@id="su"]""")
    actions = ActionChains(base.driver)
    actions.move_to_element(baidu).double_click(baidu).perform()
    # actions.move_to_element(baidu).context_click(baidu).perform()
    sleep(2)



