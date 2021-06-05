# @Site    :
# @File    : LoginPage.py
# @Software: PyCharm
# 封装登录方法
import sys
import time
import unittest
from test_case import base

from conf.setting import TEST_ACCOUNT
from test_case.pages.common.LoginPage import LoginPage
from test_case.utils.DriverFactory import get_firefox_driver, get_chrome_driver
import warnings


class basecase(unittest.TestCase):
    """

        :param driver:
        :return:
        """
    def setUp(self):
        print('测试开始')
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver = get_chrome_driver()
        return self.driver

    def tearDown(self):
        self.driver.quit()
