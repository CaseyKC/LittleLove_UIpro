# -*- coding: utf-8 -*- 
# @Time : 2021/1/23 10:41 下午 
# @Author : gc
# @File : BaseLogin.py 
# @Software: PyCharm
from time import sleep

from conf.info import LANDING_PAGES_LINKS
from conf.setting import TEST_ACCOUNT
from test_case.pages.common.LoginPage import LoginPage
# from test_case.pages.zhonghui.ZhonghuiHealth3gPage import ZhonghuiHealth3gPage
from test_case.utils.DriverFactory import get_chrome_driver
from selenium import webdriver


class BaseLogin:
    def login(driver):
        print("eeeeeeee")
        driver.get(LANDING_PAGES_LINKS['passportLogin'])
        driver.implicitly_wait(10)

        # 从配置文件中获取配置信息
        phone = TEST_ACCOUNT['account_test']['phone']  # 从配置文件中按照当前测试环境和账号类型取得账号信息
        authno = TEST_ACCOUNT['account_test']['authno']
        lgp = LoginPage(driver)
        lgp.enter_phone(phone)
        lgp.enter_username(authno)
        sleep(3)
        lgp.login()

        # 取出所有li元素
        liList = lgp.get_account()
        # 取出所有li元素
        for value in liList:
            # print(value.text)
            # print(liList.index(value))
            # 判断元素name等于小杰，选中
            print("小杰" in value.text)
            if "小杰" in value.text:
                # print(liList.index(value)+1)
                driver.find_element_by_xpath(
                    "//ul[@class='ls-userlist']/li[%d]" % (liList.index(value) + 1)).click()
                driver.find_element_by_xpath("//button[contains(@class,'ls-btn-next')]").click()
                break
            else:
                continue
        sleep(5)
    def open_page(driver, url):
        driver.get(url)
        sleep(8)
        # op = page(driver)
        # op.click_scroll_target()
        # return op