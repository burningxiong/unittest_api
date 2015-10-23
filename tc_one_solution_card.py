#! /usr/bin/env python
# coding: utf8
# version: v01
__author__ = 'xiong.mingjun'

"""
Change log:
v01 新建用于测试一卡通数据接入的api，一共九个
"""


import httplib
import unittest
import json
from common_datas import *
from http_request import *


class TestOneSC(unittest.TestCase):
    """用于测试一卡通的九个api,另外包括异常情况
    """

    # 初始化测试数据
    def setUp(self):
        pass

    """
    # 开始测试门禁控制器
    """
    # 测试添加门禁控制器，结果成功，返回00
    def test_10_controller_create(self):
        test_one_solution_card('access_controller', '00', 'POST', 'CREATE')

    # 重复注册，结果失败，返回01，数据重复
    def test_11_controller_create(self):
        test_one_solution_card('access_controller', '01', 'POST', 'CREATE')

    # 测试修改门禁控制器，结果成功，返回00
    def test_12_controller_modify(self):
        test_one_solution_card('access_controller', '00', 'POST', 'MODIFY')

    # 测试删除门禁控制器，结果失败，返回00
    def test_13_controller_del(self):
        test_one_solution_card('access_controller', '00', 'DELETE')

    # 测试修改不存在的门禁控制器，结果失败，返回02
    def test_14_controller_modify(self):
        test_one_solution_card('access_controller', '02', 'POST', 'MODIFY')

    # 删除不存在的门禁控制器，结果失败，返回02
    def test_15_controller_del(self):
        test_one_solution_card('access_controller', '02', 'DELETE')

    """
    # 开始测试pos
    """
    # 测试添加门禁控制器，结果成功，返回00
    def test_16_pos_create(self):
        test_one_solution_card('pos', '00', 'POST', 'CREATE')

    # 重复注册，结果失败，返回01，数据重复
    def test_17_pos_create(self):
        test_one_solution_card('pos', '01', 'POST', 'CREATE')

    # 测试修改门禁控制器，结果成功，返回00
    def test_18_pos_modify(self):
        test_one_solution_card('pos', '00', 'POST', 'MODIFY')

    # 测试删除门禁控制器，结果失败，返回00
    def test_19_pos_del(self):
        test_one_solution_card('pos', '00', 'DELETE')

    # 测试修改不存在的门禁控制器，结果失败，返回02
    def test_20_pos_modify(self):
        test_one_solution_card('pos', '02', 'POST', 'MODIFY')

    # 删除不存在的门禁控制器，结果失败，返回02
    def test_21_pos_del(self):
        test_one_solution_card('pos', '02', 'DELETE')

    """
    # 开始测试idcard
    """
    # 测试添加门禁控制器，结果成功，返回00
    def test_22_idcard_create(self):
        test_one_solution_card('idcard', '00', 'POST', 'CREATE')

    # 重复注册，结果失败，返回01，数据重复
    def test_23_idcard_create(self):
        test_one_solution_card('idcard', '01', 'POST', 'CREATE')

    # 测试修改门禁控制器，结果成功，返回00
    def test_24_idcard_modify(self):
        test_one_solution_card('idcard', '00', 'POST', 'MODIFY')

    # 测试删除门禁控制器，结果失败，返回00
    def test_25_idcard_del(self):
        test_one_solution_card('idcard', '00', 'DELETE')

    # 测试修改不存在的门禁控制器，结果失败，返回02
    def test_26_idcard_modify(self):
        test_one_solution_card('idcard', '02', 'POST', 'MODIFY')

    # 删除不存在的门禁控制器，结果失败，返回02
    def test_27_idcard_del(self):
        test_one_solution_card('idcard', '02', 'DELETE')

    def tearDown(self):
        pass

if __name__ == '__main__':
    test = TestOneSC()
    test.run()



