#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep


def test_windows_scroll(base):
    base.get("打开简书","https://www.jianshu.com/")
    js = "var q=document.documentElement.scrollTop=100"
    base.driver.execute_script(js)
    sleep(2)
