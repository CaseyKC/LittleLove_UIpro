from conf.setting import ELEMENTS_PATH_TAIKANG
from test_case.utils.BasePage import BasePage
from selenium.webdriver.common.keys import Keys


class TaikangESRDGift2Page(BasePage):
    def __init__(self, driver):
        """初始化
        :param driver:传入driver
        """
        BasePage.__init__(self, driver, ELEMENTS_PATH_TAIKANG)
        # self.scroll_target_button = self.locator_map['scrollTargetButton']
        self.accept_clause = self.locator_map['acceptClause']
        self.insureButton = self.locator_map['insureButton']
        self.popup_insureButtons = self.locator_map['popup_insureButtons']
        self.accept_health_notification = self.locator_map['acceptHealthNotification']
        # self.assert_content = self.locator_map['assertContent']
        self.input_name = self.locator_map['name']
        self.input_card = self.locator_map['idcard']
        self.taikang_insurance_policy = self.locator_map['insurance_policy']
        self.taikang_insure = self.locator_map['insure']
        self.taikang_insurance_policy_content = self.locator_map['insurance_policy_content']
        self.taikang_name = self.locator_map['name']
        self.taikang_health_notification = self.locator_map['health_notification']
        self.taikang_health_notification_content = self.locator_map['health_notification_content']
        self.taikang_health_notification_insure = self.locator_map['health_notification_insure']
        self.taikang_insurance_clauses = self.locator_map['insurance_clauses']
        self.taikang_insurance_clauses_content = self.locator_map['insurance_clauses_content']
        self.taikang_insurance_clauses_insure = self.locator_map['insurance_clauses_insure']


    # def click_scroll_target(self):
    #     """点击"立即投保按钮，定位到投保模块"
    #     :return:
    #     """
    #     self.click(self.scroll_target_button)


    def input_insure_name(self,inputname):
        """输入姓名输入框"""
        self.click(self.input_name)
        self.type(self.input_name, Keys.COMMAND + 'a')
        self.type(self.input_name, Keys.BACKSPACE)
        self.type(self.input_name, inputname)

    def input_insure_idcard(self,inputcard):
        """输入身份证输入框"""
        self.click(self.input_card)
        self.type(self.input_card, Keys.COMMAND + 'a')
        self.type(self.input_card, Keys.BACKSPACE)
        self.type(self.input_card, inputcard)

    def click_accept_clause(self):
        """点击"点击条款确认按钮"
        :return:
        """
        self.click(self.accept_clause)

    def click_insure_button(self):
        """点击"点击立即投保按钮"
        :return:
        """
        self.click(self.insureButton)

    def click_popup_insure_buttons(self):
        """点击"点击立即投保按钮"
        :return:
        """
        self.click(self.popup_insureButtons)

    def click_health_button(self):
        """点击"点击建告的符合条件投保按钮"
        :return:
        """
        self.click(self.accept_health_notification)

    # def get_element_assert_content(self):
    #     """投保结果断言"""
    #     return self.get_element_text(self.assert_content)

    def click_insurance_policy(self):
        """点击投保须知"""
        self.click(self.taikang_insurance_policy)

    def get_taikang_insurance_policy_content(self):
        """获取投保须知内容"""
        return self.get_element_text(self.taikang_insurance_policy_content)

    def click_insure(self):
        """点击投保须知确定按钮"""
        self.click(self.taikang_insure)
    def click_taikang_name(self):
        """点击姓名输入框"""
        self.click(self.taikang_name)

    def get_name_attribute(self):
        """获取输入框的值"""
        return self.get_element_attribute(self.taikang_name, 'value')

    def click_health_notification(self):
        """点击健康告知"""
        self.click(self.taikang_health_notification)

    def get_taikang_health_notification_content(self):
        """获取健康告知内容"""
        return self.get_element_text(self.taikang_health_notification_content)

    def click_health_notification_insure(self):
        """点击健康告知确定按钮"""
        self.click(self.taikang_health_notification_insure)

    def click_insurance_clauses(self):
        """点击保险条款"""
        self.click(self.taikang_insurance_clauses)

    def get_taikang_insurance_clauses_content(self):
        """获取保险条款内容"""
        return self.get_element_text(self.taikang_insurance_clauses_content)

    def click_insurance_clauses_insure(self):
        """点击保险条款确定按钮"""
        self.click(self.taikang_insurance_clauses_insure)



