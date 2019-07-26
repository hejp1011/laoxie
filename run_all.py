#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'xuepl'
__mtime__ = '2019/7/24'
 OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@OO@@OOOOOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@\\OOO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO@@OOOOOOOOOOOO@OO@@@@@@@@@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOOOOO@@@@@@@@@@OOOO\/\O/OOOOOOOO@O@O@@@@@@O`OO@@@@@@@O@@@@@OOO@O@@@@O@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO^.,OO@@@OOOO\]OOoOOOo\OOOOOOOO/OOO@@@O@Oo*[oO@@@OO\OOO@@OOOOOOOOOOO@@@@@@@@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOO@@@@@@@@@@OO/[.....*\OOOOO/oOOOOOOOO@OOOO=o[o^,`OOOOOOO`...,O@@OO\OO`=OOOoOOOOOOOOOO@@@@O@@@@@@@@@@@@OOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOO[[\O[`......   .....,OO@OOO@@@O@@@OOOOOOo/`......,/OO*..  ..O@@@O`......[O\OO\OOOOOOOO@@@@@O@@@@OOOOo^.,OOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOO`..........   .....*[OOOO@@@OOOO@OO@OO`...      .\/*..   .=O@O\^..    ...o\OOOOO@OO@@OOO@@@OOO@Ooo`*.....,\O@@@@@@@@@OOOOOOOO
 OOOOOOOOOO`.......  ......*,/O@@@@@OOOOOOOO@@O..        ......   .=@@O/..        .*=O@@@@@@O@@@@@@@@OOO/`[*..........,[[[OOO@@@@OOOOO
 OOOOOOOOOOOO\*....... ....../O@@@@@OOOOOO@OOO\.         ......   .=@OO`.         .*oO@@@@@@@O@@@@@@@@@O`**..................*\OOOOOOO
 OOOOOOOOOOOOOo^............,O@@@@@@@@O@@@@@OO.          ...*..   .O@O^.           .OO@@@@@@@@@@@@@@@@@@O`..............***]oOOOOOOOOO
 OOOOOOOOoOOOOOO`........*oO@@@@@@@@OO@O@@@@[.            ..^o.. .=@@/.            .,O@@@@@@@@@@@@@@@@@@@O\]]`.......*]/ooOOOOOOOOOOOO
 OOOooooooOOOOOo*.......*O@@@@@@@@@@@@@@@@/`.              .OO^...O@O.              .,OO@@@@@@O@@@@@@@@@@@@OO*.......*/oOOOOOOOOOOOOOO
 ooOOooOOOOOOOO\`...../@@@@@@@@@@@@@@@@@\`...             .=@O^../@@O.              ...\o@@@@@@@@@@@@@@@@@@@@O`......*oOOOOOOOOOOOOOOO
 OooooOOooOOOOOo`...=@@@@@@@@O/[[[\O/\Oo^... . ..         .O@@O..O@@@`      .... .. ....,OOO@OO@@@@@@@@@@@@@@@@O]`..../OOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOO\*=@@@@@@O`..    .*...O\*[`]]`.`...... ../@@O`..\@@@\.   ....*,..]]]],*/O/\]\O^`....[\@@@@@@@@@@\`..,OOOOOOOOOOOOOOOO
 OOOOooOOOOOOOOOOOO@@@@@OO.       ......\@@.=@@[@@OO\*..,O@O^.  ..OO@@\...,/O@@@@O/.,\@@/`.......     .,O@@@@@@@@@OooOOOOOOOOOOOOOOOOO
 OoooOOOOOOOOOOOOO@@@O/`.         ..  ....\@@]]]@@@@//o^OOO^.    .,oOO@O]]\O@@@@\]]]@O`..........      ...\O@OOO@@@OOOOOOOOOOOOOOOOOOO
 OooOOOOOOOOOOOOOOOO^.            .... .....,`[\OO@\`,oO[....     ....[OO^`*OO/o/[`,............          ..=oOOO@@@@@@OOOOOOOOOOOOOOO
 ooOOOOOOOOOOOOOOO/..              ..   .......*^`[\/O`                .,OO\`[\.................             .*=OO@@@@@@OOOOOOOOOOOOOO
 OoOOOooOOOOOOOOO`..               ...     ......./O`.      .           ...\\....... ...........              ..*\@@@@@@@OOOOOOOOOOOOO
 OOOoOooOOOOOOOO^..                   ...     . ...              ...     ............ ........               ...,\O@@@@@OOOOOOOOOOOOOO
 OOOOOooOOOOOOO^..                                            .......... ..             ....                  ....,O@O@@@OOOOOOOOOOOOO
 OOOOOOOOOOOOOO*.                                             .  ...........                                    ...=O@@@OOOOOOOOOOOOOO
 OOOOOOOOOOOOO^*..                                                     .. ....                                  ...=OO@@@@OOOOOOOOOOOO
 OOOOOOOOOOOOO/..                                         ... .            ....                                 ....\@@@@@@OOOOOOOOOOO
 OOOOOOOOOOOOO`..                                      ..,/\o/\]]o]...       ...                                  ..O@@@@@@@@OOOOOOOOO
 OOOOOOOOOOOOOo`.                                    ./O@@@@@@@@@@@OO`..     .....                               ..*oOO@@@@@@OOOOOOOOO
 OOOOOOOOOOOOOo..                                   ,@@@@@@@@@@@@@@@@@\.      ...  ..                            ...=O@@@@@@@@@@OOOOOO
 OOOOOOOOOOO@O^..                                   /@@@@@@OOOO@@@@@@@@`.       ..  .....  ...                   ..,/O@@@@@@@@@@@@@@@@
 @OOOOOOO@@@@@O*.                                   =@@@@@@@@@@@@@@@@@@`           ..........                    ..,/O@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@O\`.                                .=@@@@@@@@@@@@@@@@@@`.        ....... ..                      ...oO@@@@@@@@@@@@@@@@
 OOOOOOOOOOOO@@@O`.                      .          =@@@@@@@@@@@@@@@@@/.        ....... ...                     ..=OO@@@@@@OOOOOOOOOOO
 OOOOOOOOOOO@@@@OO^..                    .        . .=@@@@@@@@@@@@@@@/..  .    . .........                    ...*\OOOOOO@@O@OOOOOOOOO
 OOOOOOOOOOOOOOOOO`..                              ...O@@@@@@@@@@@@@\..       .. ........                   ....]oOO@OO@OOOOOOOOOOOOOO
 OOOOOOOOOOOO@@@OO^..                      .      ...\OOO@@@@@@@@OOOOo`...  .. .........                  ....*=OOO@@@@@OOOOOOOOOOOOOO
 OOOOOOOOOOOOOO@@@OO`..                     ...    .,OO@@@@@@@@@@@@@@O/...............                 ....**\`[OO@@@@@@@OOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOO`..                    .......=[[\\\/oO\o\/OOO\`.............                  ...*,...oOOOO@@@@OOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO]]`.                     .........,OOOOOOo\o*............                    ....,oo\O@@OO@@@@OOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOO`*/O@OO\..                      ........................                       ....=OOO@O@@@@OOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO/oOOOOOOOoo[*....                      .................                       .....,]/@@O@@@OOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOoOOOOOOOOOO\]O@@O\`*.,*,*]*..                      ....                            ....OOOOOOOOOOOOOOOOOOOOOOOOOOOO@@OOOOO
 OOOOOOOOOOOOOOOOOOOOOO=@@@@@@@@@@@@@@@OOOO\..                                      ...........,`]OO@@OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO@@@@@@@@@@@@@@@@@@O@@@O]`                         ....,*]]/*,.......]]//O@@@@@@@O/\O[`*/OOOOOOOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO@@O@@@@@@@@@@@@@@@@@@@@@@@\],]....   ..    .,,]OO@OOOOOOO@O@OOOOOOO@OO@@@@@@@@/[,o/\oo\oOOOO@OOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO@@/O@@@@@@@@@O@@@@@@@@@O@OO@@OOOOOOOOOOOOO@@O@@@@@@@@OOOOOO@@@@OO@@@@@@@@@OO///]Ooo[]o//OOOO@OOOOOOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOOOOOOOO\@OO@@@@@@@OO@\=@@@@@@@@@@OO@\=@OOOOOOOOOOOOOOOOOOO^\[O/\[OOOooOOOOOOO/O[*`/\o*.,o`/Oo/\oOO@OOOOOOOOOOOOOOOOOO

"""
import pytest

'''
pytest.main(['--alluredir','reports/xml'])
    --alluredir 把生成的报告数据存到后边的文件夹内
allure generate reports/xml -o reports/html --clean
    把报告数据解析成html文件数据
    reports/xml  pytest.main生成报告数据的文件
    reports/html  存放html文件数据的文件夹
    --clean  先清空reports/html下边的文件，然后再生成报告
'''


pytest.main(['-s','-q','--alluredir','reports/xml','test_case/business_process'])