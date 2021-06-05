import unittest
from time import sleep
from selenium import webdriver
from conf.info import LANDING_PAGES_LINKS
from conf.setting import TEST_ACCOUNT
from test_case.action.common import BaseTestCase
from test_case.action.common.BaseLogin import BaseLogin
from test_case.pages.taikang.TaikangESRDGift2Page import TaikangESRDGift2Page


class UiTest(BaseTestCase.basecase):
    def no_test_taikang_ESRD_gift_2(self):
        """泰康尿毒症赠险"""
        BaseLogin.login(self.driver)
        BaseLogin.open_page(self.driver, LANDING_PAGES_LINKS['taikang']['taikang_ESRD_gift_2']['url'])
        taikang_cmp = TaikangESRDGift2Page(self.driver)
        sleep(3)
        # taikang_cmp.click_scroll_target()
        # sleep(1)
        taikang_cmp.input_insure_name(TEST_ACCOUNT['account_test']['name'])
        sleep(3)
        taikang_cmp.input_insure_idcard(TEST_ACCOUNT['account_test']['idCard'])
        sleep(1)
        taikang_cmp.click_insure_button()  # 落地页的立即领取保障按钮
        sleep(1)
        taikang_cmp.click_popup_insure_buttons()  #二次弹窗内的领取保障按钮
        sleep(1)
        taikang_cmp.click_accept_clause()  # 同意条款
        sleep(1)
        taikang_cmp.click_health_button()

    def no_test_taikang_insurance_policy(self):
        """投保须知条款校验"""
        BaseLogin.open_page(self.driver, LANDING_PAGES_LINKS['taikang']['taikang_ESRD_gift_2']['url'])
        taikang_cmp = TaikangESRDGift2Page(self.driver)
        sleep(2)
        # taikang_cmp.click_scroll_target()
        # sleep(1)
        taikang_cmp.click_insurance_policy()
        sleep(1)
        taikang_toubaoxuzhi = taikang_cmp.get_taikang_insurance_policy_content()
        sleep(2)
        # print(taikang_toubaoxuzhi)
        sleep(1)
        taikang_cmp.click_insure()
        self.assertIn(LANDING_PAGES_LINKS['taikang']['taikang_ESRD_gift_2']['toubao_content'], taikang_toubaoxuzhi)

        # 健康告知校验
        sleep(1)
        taikang_cmp.click_health_notification()
        sleep(1)
        taikang_health_notification_content = taikang_cmp.get_taikang_health_notification_content()
        # print(taikang_health_notification_content)
        sleep(1)
        taikang_cmp.click_health_notification_insure()
        self.assertIn(LANDING_PAGES_LINKS['taikang']['taikang_ESRD_gift_2']['health_notification'],taikang_health_notification_content)

        #保险条款校验
        sleep(1)
        taikang_cmp.click_insurance_clauses()
        sleep(1)
        taikang_insurance_clauses_content = taikang_cmp.get_taikang_insurance_clauses_content()
        # print(taikang_insurance_clauses_content)
        sleep(1)
        taikang_cmp.click_insurance_clauses_insure()
        self.assertIn(LANDING_PAGES_LINKS['taikang']['taikang_ESRD_gift_2']['insurance_clauses'], taikang_insurance_clauses_content)








if __name__ == "__main__":
    unittest.main()

