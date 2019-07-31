#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/7/31'



sql="INSERT INTO `db_game_mescal`.`game_mescal(`user_id`,`user_name`, `age`,`time`)values(`{}`,`xiao{}`,`18`,`00:00:00-00:00:00`)"
for i in range (1,201):
    s = sql.format(str(i).zfill(3),str(i).zfill(3))
    print(s)
