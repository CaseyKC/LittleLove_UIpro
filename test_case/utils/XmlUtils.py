# -*- coding: utf-8 -*-
import xml.dom.minidom
from test_case.utils.Locator import Locator
from conf.setting import ELEMENTS_PATH_COMMON
from selenium.webdriver.common.by import By


def read_xml_document(path, page_name):
    """
    读取指定文件中某个page所有的元素信息
    :param path: 文件路径
    :param page_name: page名
    :return:
    """
    locator_map = {}
    try:
        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        pages = root.getElementsByTagName('page')

        for page in pages:
            if page.getAttribute('pageName').lower() == page_name.lower():
                for loc in page.getElementsByTagName('locator'):
                    locator_map[loc.childNodes[0].nodeValue] = Locator(loc.childNodes[0].nodeValue,
                                                                       get_by_type(loc.getAttribute('type')),
                                                                       int(loc.getAttribute('timeOut')),
                                                                       loc.getAttribute('value'))
    except Exception as e:
        raise e
    return locator_map


def get_by_type(type):
    """
    by_type转换
    :param type:
    :return:
    """
    if type.lower() == 'id':
        by_type = By.ID
    elif type.lower() == 'name':
        by_type = By.NAME
    elif type.lower() == 'classname':
        by_type = By.CLASS_NAME
    elif type.lower() == 'xpath':
        by_type = By.XPATH
    elif type.lower() == 'cssselector':
        by_type = By.CSS_SELECTOR
    elif type.lower() == 'linktext':
        by_type = By.LINK_TEXT
    elif type.lower() == 'partiallinktext':
        by_type = By.PARTIAL_LINK_TEXT
    else:  # default
        by_type = By.ID
    return by_type


if __name__ == '__main__':
    lmp = read_xml_document(ELEMENTS_PATH_COMMON, 'LoginPage')
    print(ELEMENTS_PATH_COMMON)
    print('lmp==>',lmp)
    a = lmp['hotelIdInputBox']
    print(lmp['hotelIdInputBox'].value)
