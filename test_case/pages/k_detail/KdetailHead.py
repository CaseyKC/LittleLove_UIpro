from conf.setting import ELEMENTS_PATH_KDETAIL
from test_case.utils.BasePage import BasePage


class KdetailHead(BasePage):
    def __init__(self, driver):
        """初始化
        :param driver:传入driver
        """
        BasePage.__init__(self, driver, ELEMENTS_PATH_KDETAIL)

        self.fundraisingButton = self.locator_map['fundraisingButton']


    def click_fundraising(self):
        """点击"点击筹款按钮"
        :return:
        """
        self.click(self.fundraisingButton)


    def get_fundraising_url(self):
        """获取"筹款url"
        :return:
        """
        return self.get_current_url()