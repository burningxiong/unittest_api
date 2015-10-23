#! /usr/bin/env python
# coding:utf8
# version:v01
__author__ = 'xiong.mingjun'

"""
Change log:
v01 for send http request
"""

import httplib
import json


def http_send_req(str_host, int_port, str_method, str_url, dict_body='', dict_header=''):
    try:
        # 需要判断body和header是否为空，根据情况在发送请求
        conn = httplib.HTTPConnection(str_host, int_port)
        if dict_body and dict_header:
            conn.request(str_method, str_url, json.dumps(dict_body), json.dumps(dict_header))
        elif (not dict_body) and (not dict_header):
            conn.request(str_method, str_url)
        elif dict_body:
            conn.request(str_method, str_url, json.dumps(dict_body))
        else:
            conn.request(str_method, str_url, '', json.dumps(dict_header))
        str_res = (conn.getresponse()).read()
        res = json.loads(str_res)
        return res
    except:
        return False
