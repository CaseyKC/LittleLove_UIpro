# -*- coding: utf-8 -*-
from test_case.utils.XmlUtils import read_xml_document
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
from aip import AipOcr



class BasePage(object):

    def __init__(self, driver, element_path):
        """初始化Page，从xml文档中读取元素，得到locator_map，
        格式为{"locator_name_a":locator_a,"locator_name_b":locator_b}
        :param driver:传入的driver
        """
        self.driver = driver
        self.locator_map = read_xml_document(element_path, self.__class__.__name__)
        print("+++++++++",self.__class__.__name__)

    def type(self, locator, values):
        """输入框输入内容
        :param locator: 元素定位信息
        :param values: 输入内容
        :return:
        """
        self.find_element(self.driver, locator).send_keys(values)

    def get_current_url(self):
        """获取当前页面的url；

        :return:
        """
        str1=self.driver.current_url
        return str1


    def clear(self, locator):
        """
        清除输入框内容,android
        :param locator:
        :return:
        """
        self.click(locator)
        time.sleep(2)
        self.click(locator)
        text = self.get_text(locator)
        self.driver.keyevent(123)
        for i in range(0, len(text)):
            self.driver.keyevent(67)

    def clear_web(self, locator):
        """
        清除输入框内容,web
        :param locator:
        :return:
        """
        self.find_element(self.driver, locator).clear()

    def send_tab_key(self, locator):
        """
        定位到某个元素发送TAB键，用于带有滚动条的对话框，定位到下一项
        :param locator:
        :return:
        """
        self.find_element(self.driver, locator).send_keys(Keys.TAB)

    def send_enter_key(self, locator):
        """
        定位某个元素发送回车键，用于某些场景，例如输入下拉提示选择框等
        :param locator:
        :return:
        """
        self.find_element(self.driver, locator).send_keys(Keys.ENTER)

    def send_space_key(self, locator):
        """
        定位某个元素发送空格键，某些选中效果无法使用click时
        :param locator:
        :return:
        """
        self.find_element(self.driver, locator).send_keys(Keys.SPACE)

    def click(self, locator):
        """点击
        :param locator: 元素定位信息
        :return:
        """
        # try:
        #     self.find_element(self.driver, locator).click()
        # # 处理element <x> is not clickable at point (x,y)
        # except ElementClickInterceptedException as e:
        #     time.sleep(2)
        #     print(repr(e))
        #     self.click(locator)
        self.find_element(self.driver, locator).click()

    def get_text(self, locator):
        """
        获取文本内容
        :param locator:
        :return:
        """
        return self.find_element(self.driver, locator).get_attribute('text')

    def select_by_value(self, locator, value):
        """按照value选择
        :param locator:
        :param value:
        :return:
        """
        select = Select(self.find_element(self.driver, locator))
        select.select_by_value(value)

    def select_by_text(self, locator, text):
        """按照text选择
        :param locator:
        :param text:
        :return:
        """
        select = Select(self.find_element(self.driver, locator))
        select.select_by_visible_text(text)

    def select_by_id(self, locator, index):
        """按照id选择
        :param locator:
        :param index:
        :return:
        """
        select = Select(self.find_element(self.driver, locator))
        select.select_by_index(index)

    def is_selected(self, locator):
        """
        判断复选框是否被选中
        :param locator:
        :return:
        """
        return self.find_element(self.driver, locator).is_selected()

    def get_element(self, locator):
        """获取元素，无等待
        :param locator:元素定位信息
        :return:返回元素
        """
        return self.get_element_driver(self.driver, locator)

    def get_elements(self, locator):
        """获取元素，无等待
        :param locator:元素定位信息
        :return:返回元素
        """
        return self.get_elements_driver(self.driver, locator)

    def is_element_present(self, locator, time_out):
        """判断元素在指定超时时间内是否出现
        :param locator: 元素定位信息
        :param time_out: 指定超时时间
        :return: 是否存在
        """
        try:
            is_existed = self.is_element_present_driver(self.driver, locator, time_out)
        except:
            is_existed = False
        return is_existed

    def find_element(self, driver, locator):
        """自定义查找元素的方法，显性等待元素加载，超过元素timeout时间后仍未加载抛出TimeoutException
        :param driver:传入的driver
        :param locator:元素定位信息
        :return:返回元素
        """
        try:
            elem = WebDriverWait(driver, locator.wait_sec).until(lambda x: self.get_element_driver(x, locator))
            return elem
        except Exception as e:
            sms = '%s页面查找%s元素失败，定位信息为%s' % (self.__class__.__name__, locator.name, locator.value)
            print(sms)
            e.args += (sms,)

            filename = '%s页面查找%s元素失败' % (self.__class__.__name__, locator.name)
            # snapshot(driver, filename)
            raise e


    def get_element_driver(self, driver, locator):
        """根据元素定位信息的by_type和value值查找元素
        查询一组元素
        :param driver: 传入的driver
        :param locator: 元素定位信息
        :return: 返回元素
        """
        by = locator.by_type
        if by == By.ID:
            elem = driver.find_element_by_id(locator.value)
        elif by == By.NAME:
            elem = driver.find_element_by_name(locator.value)
        elif by == By.CLASS_NAME:
            elem = driver.find_element_by_class_name(locator.value)
        elif by == By.XPATH:
            elem = driver.find_element_by_xpath(locator.value)
        elif by == By.CSS_SELECTOR:
            elem = driver.find_element_by_css_selector(locator.value)
        elif by == By.LINK_TEXT:
            elem = driver.find_element_by_link_text(locator.value)
        elif by == By.PARTIAL_LINK_TEXT:
            elem = driver.find_element_by_partial_link_text(locator.value)
        else:  # default
            elem = driver.find_element_by_id(locator.value)
        return elem


    def get_elements_driver(self, driver, locator):
        """根据元素定位信息的by_type和value值查找元素
        查询一组元素
        :param driver: 传入的driver
        :param locator: 元素定位信息
        :return: 返回元素
        """
        by = locator.by_type
        if by == By.ID:
            elem = driver.find_elements_by_id(locator.value)
        elif by == By.NAME:
            elem = driver.find_elements_by_name(locator.value)
        elif by == By.CLASS_NAME:
            elem = driver.find_elements_by_class_name(locator.value)
        elif by == By.XPATH:
            elem = driver.find_elements_by_xpath(locator.value)
        elif by == By.CSS_SELECTOR:
            elem = driver.find_elements_by_css_selector(locator.value)
        elif by == By.LINK_TEXT:
            elem = driver.find_elements_by_link_text(locator.value)
        elif by == By.PARTIAL_LINK_TEXT:
            elem = driver.find_elements_by_partial_link_text(locator.value)
        else:  # default
            elem = driver.find_elements_by_id(locator.value)
        return elem

    def is_element_present_driver(self, driver, locator, time_out):
        """判断元素在指定超时时间内是否出现
        :param driver: 传入的dirver
        :param locator: 元素定位信息
        :param time_out: 指定超时时间
        :return: 是否存在
        """
        try:
            is_present = WebDriverWait(driver, time_out).until(lambda x: self.get_element_driver(x, locator)).is_displayed()
            return is_present
        except Exception as e:
            sms = '%s页面查找%s元素失败，定位信息为%s' % (self.__class__.__name__, locator.name, locator.value)
            e.args += (sms,)
            raise e

    def get_element_attribute(self, locator, key):
        """
        :param locator:
        :param key:
        :return:
        """
        return self.find_element(self.driver, locator).get_attribute(key)

    def get_element_text(self, locator):
        """

        :param locator:
        :return:
        """
        return self.find_element(self.driver, locator).text

    def switch_frame_element(self, locator):
        """

        :param locator:
        :return:
        """
        self.driver.switch_to.frame(self.find_element(self.driver, locator))

    def switch_default_frame(self):
        """

        :return:
        """
        self.driver.switch_to.default_content()

    def move_to(self, locator):
        """

        :return:
        """
        ActionChains(self.driver).move_to_element(self.find_element(self.driver, locator)).perform()

    def mouse_left_click(self, locator):
        """
        鼠标左击
        :return:
        """
        ActionChains(self.driver).click(self.find_element(self.driver, locator)).perform()

     # 截图 图片转文字
    def screenshot_to_text(self,APP_ID, API_KEY, SECERT_KEY, *args):
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        str = os.getcwd()
        str1 = str.split("Ebao_pro")[0]
        url= str1 + 'Ebao_pro/screen_shoot/' + tm + ".png"
        self.driver.save_screenshot(url)
        print("截图成功")
        # APP_ID = "20454072"
        # API_KEY = "0plxGsSzXmBesO29QTnyi2DW"
        # SECERT_KEY = "DrkIkyLrSkLrsMoTftCrQ8N0oIMMRxOf"
        client = AipOcr(APP_ID, API_KEY, SECERT_KEY)
        i = open(url, "rb")
        image = i.read()
        message = client.basicGeneral(image)
        list_a = []
        for i in message.get('words_result'):
            list_a.append(i.get('words'))
        # 获取的是图片上的文字
        str1 = ''.join(list_a)
        print(str1)
        for content in args:
            if content in str1:
                print(content + ":" + "文案展示正确")
                return True
            else:
                print(content + ":" + "文案展示错误")
                return False


if __name__ == '__main__':
    page = BasePage('123')
    print(page.__class__.__name__)
