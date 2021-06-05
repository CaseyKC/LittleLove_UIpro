# -*- coding: utf-8 -*-
import os

#项目路径
from selenium.webdriver.firefox import webdriver

BASE_PATH = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))


#元素文件路径
ELEMENTS_PATH = os.path.join(BASE_PATH, 'elements', 'UILibrary.xml')
ELEMENTS_PATH_COMMON = os.path.join(BASE_PATH, 'elements', 'common', 'UILibrary.xml')

ELEMENTS_PATH_TAIKANG = os.path.join(BASE_PATH, 'elements', 'taikang', 'UILibrary.xml')
ELEMENTS_PATH_KDETAIL = os.path.join(BASE_PATH, 'elements', 'k_detail', 'UILibrary.xml')
# case路径
#CASE_PATH = os.path.join(BASE_PATH, 'src', 'cases')

CASE_PATH = os.path.join(BASE_PATH, 'src', 'cases')

# result路径
RESULT_PATH = os.path.join(BASE_PATH, 'results')

# 截图路径
PICTURE_PATH = os.path.join(BASE_PATH, 'data')

# 日志路径
LOG_PATH = os.path.join(BASE_PATH, 'logs')

#成人
TEST_ACCOUNT = {
    "account_test": {
        "phone": "15101058923",
        "authno": "1111",
        "name": "赵世杰",
        "idCard": "622628198903151057"
    }
}
#少儿
TEST_ACCOUNT1 = {
    "account_test": {
        "phone": "15101058923",
        "authno": "1111",
        "name": "少儿",
        "idCard": "110228201308010656"
    }
}



# 设置窗口大小
WINDOW_OPTION = {
    "SCREEN_WIDTH": 250,
    "SCREEN_HEIGHT": 850
}

# 发送测试报告邮件设置
MAIL_ASCII = 'utf-8'
MAIL_HEADER = '测试报告'
MAIL_FROM = '1810358294@qq.com'
MAIL_FROM_PASSWORD = 'nsqmgskskpyfdche'
MAIL_TO = '1810358294@qq.com'

SMTP_SERVER = {"host": "smtp.qq.com", "port": 465}

MAIL_CONTENT = '您好，自动化测试执行结束，详细结果请查看附件内容，谢谢！'






