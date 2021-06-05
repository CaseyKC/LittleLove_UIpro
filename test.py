
# class test :
#
#     # _后面的字母大写
#     def reverseFirstUp (oldString):
#         newList = oldString.split('-')
#         newString = ""
#         for list in newList:
#             newString+=list.capitalize()
#         print("_后面的字母大写==>",newString)
#
#     # _分割
#     # def reverseSplit(oldString):
#
#     reverseFirstUp("huatai-health-hongfu2020")

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest, sys, os, datetime
from conf.setting import RESULT_PATH
from HTMLTestRunner import HTMLTestRunner
from test_case.utils.Tools import send_mail

from test_case.action.zhonghui import test_zhonghui_health_cancer_ganbu30Actions, test_zhonghui_health_2020Actions, \
    test_zhonghui_accident_journeyActions, test_zhonghui_health_3gActions, test_zhonghui_health_huganwuyouActions, \
    test_zhonghui_illness_2020Actions
from test_case.action.taikang import test_taikang_health_quanmin2020Actions
from test_case.action.taipingyang import test_taipingyang_health_2020Actions
from test_case.action.pingan import test_pingan_health_2020Actions
from test_case.action.zhongan import test_zhongan_health_2020_oneActions
from test_case.action.yangguang import test_yangguang_health_aiwuyou2020Actions
from test_case.action.pingan import test_pingan_accident_millionActions, test_pingan_health_childActions

BASE_PATH = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))


def get_all_case(su):
    case_path = os.path.join(BASE_PATH, 'Ebao_pro/test_case/action')
    case_suite = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    su.addTest(case_suite)
    return su


def case_json(case):
    data = {
        "test_guofu_health_huiguibao": {
            "case": test_zhonghui_health_cancer_ganbu30Actions.UiTest('zhonghui_health_cancer_ganbu30'),
            "desc": "众惠爱肝保障计划"
        },
        "test_guofu_health_huiguibao": {
            "case": test_zhonghui_health_2020Actions.UiTest('zhonghui_health_cancer_ganbu30'),
            "desc": "众惠600万"
        },
        "test_zhonghui_accident_journey": {
            "case": test_zhonghui_accident_journeyActions.UiTest('test_zhonghui_accident_journey'),
            "desc": "轻松出行"
        },
        "test_zhonghui_health_3g": {
            "case": test_zhonghui_health_3gActions.UiTest('test_zhonghui_health_3g'),
            "desc": "惠享e生·百万医疗 3高"
        },
        "test_zhonghui_health_huganwuyou": {
            "case": test_zhonghui_health_huganwuyouActions.UiTest('test_zhonghui_health_huganwuyou'),
            "desc": "众惠护肝无忧"
        },
        "test_zhonghui_illness_2020": {
            "case": test_zhonghui_illness_2020Actions.UiTest('test_zhonghui_illness_2020'),
            "desc": "众惠重疾"
        },
        "test_taikang_health_quanmin2020": {
            "case": test_taikang_health_quanmin2020Actions.UiTest('test_taikang_health_quanmin2020'),
            "desc": "泰康全民600万"
        },
        "test_taipingyang_health_2020": {
            "case": test_taipingyang_health_2020Actions.UiTest('test_taipingyang_health_2020'),
            "desc": "太平洋600万"
        },
        "test_pingan_health_2020": {
            "case": test_pingan_health_2020Actions.UiTest('test_pingan_health_2020'),
            "desc": "平安百万"
        },
        "test_zhongan_health_2020_one": {
            "case": test_zhongan_health_2020_oneActions.UiTest('test_zhongan_health_2020_one'),
            "desc": "众安百万"
        },
        "test_yangguang_health_2020": {
            "case": test_yangguang_health_aiwuyou2020Actions.UiTest('test_yangguang_health_2020'),
            "desc": "阳光百万"
        },
        "test_pingan_accident_million": {
            "case": test_pingan_accident_millionActions.UiTest('test_pingan_accident_million'),
            "desc": "平安150万"
        },
        "test_pingan_health_child": {
            "case": test_pingan_health_childActions.UiTest('test_pingan_health_child'),
            "desc": "平安少儿"
        }

    }
    return data[case]


def main():
    su = unittest.TestSuite()
    #   判断单独执行还是执行所有
    if len(sys.argv[1:]) == 0:
        get_all_case(su)
    else:
        for k in sys.argv[1:]:
            case = case_json(k)["case"]
            su.addTest(case)
    # fp = open('/var/www/report/ebao-ui.html', 'wb')
    # fp = open('./456.html', 'wb')
    # run = HTMLTestRunner.HTMLTestRunner(stream=fp, title='保险ui测试', description='用例执行情况')
    this_name = 'result_%s' % datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = this_name + '.html'
    file_name = os.path.join(RESULT_PATH, file_name)
    fp = open(file_name, 'wb')
    run = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'UI自动化测试', description=u'用例测试情况')
    run.run(su)
    fp.close()
    file_list = [file_name]
    # send_mail(file_list)


if __name__ == '__main__':
    main()





