#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_key_demo(base):
    base.get("打开百度", 'https://www.baidu.com/')
    baidu = base.local_element("""//*[@id="kw"]""")
    baidu.click()
    actions = ActionChains(base.driver)
    actions.send_keys("a",'b').key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).pause(2).send_keys(Keys.BACKSPACE).perform()
    sleep(3)