# -*- coding: utf-8 -*-
# @Site    :
# @File    : LoginPage.py
# @Software: PyCharm
from conf.setting import ELEMENTS_PATH_COMMON
from test_case.utils.BasePage import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, driver):
        """初始化
        :param driver:传入driver
        """
        BasePage.__init__(self, driver, ELEMENTS_PATH_COMMON)
        self.login_phone_input_box = self.locator_map['loginPhoneInputBox']
        self.login_verification_code_input_box = self.locator_map['loginVerificationCodeInputBox']
        self.login_button = self.locator_map['loginButton']
        self.check_select_account = self.locator_map['checkSelectAccount']

    def enter_phone(self, id):
        """输入手机号
        :param phone:手机号
        :return:
        """
        self.clear_web(self.login_phone_input_box)
        self.type(self.login_phone_input_box, id)

    def enter_username(self, verification_code):
        """输入验证码
        :param verification_code: 验证码
        :return:
        """
        self.clear_web(self.login_verification_code_input_box)
        self.type(self.login_verification_code_input_box, verification_code)

    def login(self):
        """点击登录按钮
        :return:
        """
        self.click(self.login_button)

    def get_account(self):
        """
        获取多账户
        :return:
        """
        # print("check_select_account==>",self.check_select_account)
        return self.get_elements(self.check_select_account)

