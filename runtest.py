#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest, sys, os, datetime,socket,redis
from conf.setting import RESULT_PATH
from HTMLTestRunner import HTMLTestRunner
from test_case.utils.Tools import send_mail

from test_case.action.k_detail import test_k_deail_head_Action




BASE_PATH = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))


def get_all_case(su):
    case_path = os.path.join(BASE_PATH, 'LittleLove_UIpro/test_case/action')
    case_suite = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    su.addTest(case_suite)
    return su


def get_case(case):
    data = {
        "test_k_detail_head": {
            "case": test_k_deail_head_Action.UiTest('test_k_detail_head'),
            "desc": "详情页头部调整验证"
        },
        "desc": "微爱UI测试"
    }




    return data[case]

r = redis.Redis(host='127.0.0.1', port=6379, encoding='utf8', decode_responses=True)

def execute_case():

    # 生成测试报告
    if socket.gethostname() == 'cn-hangzhou-qsebao-vpc-back-aj-test-001':
        fp = open('/var/www/report/LittleLove-ui.html', 'wb')
        file_name = '/var/www/report/ebao-ui.html'
    else:
        this_name = 'result_%s' % datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = this_name + '.html'
        file_name = os.path.join(RESULT_PATH, file_name)
        fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'UI自动化测试', description=u'用例测试情况')

    # 执行用例
    su = unittest.TestSuite()
    #   判断单独执行还是执行所有
    if len(sys.argv[1:]) == 0:
        get_all_case(su)
    else:
        for k in sys.argv[1:]:
            if isinstance(get_case(k)["case"],list):
                for case in get_case(k)["case"]:
                    su.addTest(case)
            else:
                case = get_case(k)["case"]
                su.addTest(case)
    runner.run(su)
    fp.close()

    # 发送邮件
    send_mail(file_name)

def main():
    #   判断是否为服务器执行，如果是服务器执行，则写redis 记录执行状态
    if socket.gethostname() == 'cn-hangzhou-qsebao-vpc-back-aj-test-001':
        try:
            ui_state = r.get("ui-test")
            if int(ui_state) != 1:
                r.set('ui-test', 1)
                execute_case()
                r.set('ui-test', 0)
            else:
                print('working...')
        except Exception as e:
            print(e)
            r.set('ui-test', 0)
    else:
        execute_case()

if __name__ == '__main__':
    main()


