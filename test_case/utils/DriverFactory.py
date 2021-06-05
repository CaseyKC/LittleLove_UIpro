from selenium import webdriver
import os,socket

from conf.setting import WINDOW_OPTION


def get_firefox_driver():
    """
    启动firefox浏览器
    :param url:
    :return:
    """
    ua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) \
                AppleWebKit/602.1.50 (KHTML, like Gecko) Mobile/14A403 \
                MicroMessenger/6.3.27 NetType/WIFI Language/zh_CN'
    webdriver.FirefoxProfile().set_preference('general.useragent.override', ua)
    #   如果是服务器执行，则用无头模式
    options = webdriver.FirefoxOptions()
    if socket.gethostname() == 'cn-hangzhou-qsebao-vpc-back-aj-test-001':
        options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(WINDOW_OPTION['SCREEN_WIDTH'], WINDOW_OPTION['SCREEN_HEIGHT'])
    # driver.get(url)
    return driver


def get_chrome_driver():
    """
    启动chrome浏览器
    :param url:
    :return:
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--kiosk') # macOS

    options.add_argument('--start-maximized')  # Windows

    driver = webdriver.Chrome(chrome_options=options)
    driver.set_window_size(WINDOW_OPTION['SCREEN_WIDTH'], WINDOW_OPTION['SCREEN_HEIGHT'])
    # driver.maximize_window()
    # driver.get(url)
    return driver



