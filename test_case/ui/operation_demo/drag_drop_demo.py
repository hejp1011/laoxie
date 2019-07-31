#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'
from time import sleep

from selenium.webdriver import ActionChains


def test_drag(base):
    base.get('打开网址',"https://element.eleme.cn/2.0/#/zh-CN")
    base.click('点击取消','//span[contains(text(),"取消")]')
    base.click("点击组件","//a[contains(text(),'组件')]")
    base.click('点击滑块','''//a[contains(text(),'滑块')]''')
    sleep(3)
    sp = base.local_element('''//span[contains(text(),'默认')]/../div//div[@class="el-slider__button el-tooltip"]''')
    size = base.local_element("""//span[contains(text(),'默认')]/../div/div""").size
    print(size)
    actions = ActionChains(base.driver)
    # actions.move_to_element(sp)
    # actions.click_and_hold(sp)
    # actions.move_by_offset(200,0)
    # actions.release()
    # actions.perform()
    actions.drag_and_drop_by_offset(sp,200,0).perform()
    sleep(10)