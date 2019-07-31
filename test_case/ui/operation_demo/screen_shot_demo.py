#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'


def test_screen_shot_demo(base):
    base.get("打开百度", 'https://www.baidu.com/')
    base.driver.get_screenshot_as_file("e:\\baidu.jpg")