#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os
import sys
import socket
from selenium import webdriver

# 封装返回路径的方法
def Base_dir():
    base_dir = str(
        os.path.dirname(os.path.abspath(__file__)))
    base_dir = base_dir.replace('\\', '/')
    return base_dir


class Config:
    # 添加chrome user_agent
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    # 以时间生成保存文件名
    name = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    function_name = sys._getframe().f_code.co_name
    INDEX_URL = "https://m.qsebao.com/"
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 690
    # 用户AGENT
    CHROME_USER_AGENT = options


def shoot_file_name(case_name):
    return './screen_shoot/' + case_name + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '.png'
