import unittest
from time import sleep

from conf.k_detail.detail_info import DETAIL_PAGES_LINKS

from test_case.action.common import BaseTestCase
from test_case.action.common.BaseLogin import BaseLogin
from test_case.pages.k_detail.KdetailHead import KdetailHead


class UiTest(BaseTestCase.basecase):


    def test_k_detail_head(self):
        """申请筹款点击验证"""
        BaseLogin.open_page(self.driver, DETAIL_PAGES_LINKS['k_detail_head']['url'])
        k_detail_head = KdetailHead(self.driver)

        #申请筹款点击
        sleep(4)
        k_detail_head.click_fundraising()
        sleep(1)


        self.assertEqual(DETAIL_PAGES_LINKS['k_detail_head']['check_url'], k_detail_head.get_fundraising_url())








if __name__ == "__main__":
    unittest.main()

