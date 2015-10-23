#! /usr/bin/env python
# coding: utf8
# version: v01
__author__ = 'xiong.mingjun'

'''
Change log:
v01 To define body messages for http request
'''

from http_request import *

# define host information
HOST = '192.168.1.4'
PORT = 6100

# define api type
dict_api_type = {
    'gateways': '/v1/gateways',
    'beaconstations': '/v1/beaconstations',
    'beacontags': '/v1/beacontags',
    'cameras': '/v1/cameras',
    'readers': '/v1/readers',
    'rfidtags': '/v1/rfidtags',
    'access_controller': '/v1/access_controller',
    'pos': '/v1/pos',
    'idcard': '/v1/idcard'
}


# for gateway management
dict_gateway = {
    'Gate_name': 'gateway001',
    'Gate_type': 'beacon',
    'Gate_desc': 'good网关',
    'Connection': {
        'protocol': 'tcp',
        'host_type': 'c',
        'conn_url': '192.168.1.200:7000',
        'url': 'http://www.baidu.com'
    }
}

# for beacon station management
dict_beacon_stations = {
    'beacon_name': 'beacon001',
    'beacon_desc': 'beacon 很好',
    'Gate_code': '',
    'Connection': {
        'protocol': 'tcp',
        'host_type': 'c',
        'conn_url': '192.168.1.200:7000',
        'url': 'http://www.baidu.com'
    },
    'Building_code': '',
    'Room_code': '',
    'Company_code': '',
    'Term_code': ''
}

# for beacon tags management
dict_beacon_tags = {
    'beacontags_name': 'tags001',
    'beacontags_desc': '很好的beacontags',
    'uuid': '',
    'major': '',
    'minor': '',
    'Company_code': ''
}

# for cameras management
dict_cameras_create = {
    'camera_name': '摄像头01_04',
    'camera_desc': 'camera_description',
    'gate_code': 'gateway1000001103307809',
    'gate_name': 'TPlink xxswitch',
    'connection': {
        'protocol': 'tcp',
        'host_type': 's',
        'conn_str': '192.168.1.200:7000',
        'url': 'http://www.baidu.com'
    },
    'building_code': 'building1000001898508095',
    'building_name': 'wer',
    'room_code': 'room1000000309007785',
    'room_name': 'rz1501',
    'company_code': 'company1000002085379881',
    'company_name': 'supportall',
    'term_code': 'terminal1000000814758037',
    'term_name': 'camera001',
    'status': 0
}

dict_cameras_modify = {
    'camera_code': 'camera1000001216596945',
    'camera_name': 'abcdef',
    'camera_desc': 'camera_description',
    'gate_code': 'gateway1000001103307809',
    'gate_name': 'TPlink xxswitch',
    'connection': {
        'protocol': 'tcp',
        'host_type': 's',
        'conn_str': '192.168.1.200:7000',
        'url': 'http://sdfasfd.cn'
    },
    'building_code': 'building1000001898508095',
    'building_name': 'wer',
    'room_code': 'room1000000309007785',
    'room_name': 'rz1501',
    'company_code': 'company1000002085379881',
    'company_name': 'supportall',
    'term_code': 'terminal1000000814758037',
    'term_name': 'camera001',
    'status': 0
}

# for readers management
dict_readers_create = {
    'reader_name': 'reader_name5',
    'reader_type': 'handset',
    'reader_type_name': 'handset',
    'company_code': 'company1000001798819529',
    'company_name': 'supportall',
    'term_code': 'terminal1000001419095422',
    'term_name': 'test',
    'mac_addr': '14:DD:A9:53:6B:F5',
    'reader_desc': 'reader_description',
    'connection': {
        'protocol': 'tcp',
        'host_type': 's',
        'conn_str': '192.168.1.200:7000',
        'url': 'http://www.rztech.com'
    },
    'login_info': {
        'user': 'alien',
        'password': 'password'
    },
    'status': 2
}

dict_readers_modify = {
    'reader_code': 'reader1000000661363287',
    'reader_name': '读写器very good',
    'reader_type': 'handset',
    'reader_type_name': 'handset',
    'company_code': 'company1000001798819529',
    'company_name': 'supportall',
    'term_code': 'terminal1000001419095422',
    'term_name': 'test',
    'mac_addr': '14:DD:A9:53:6B:F5',
    'reader_desc': 'reader_description',
    'connection': {
        'protocol': 'tcp',
        'host_type': 's',
        'conn_str': '192.168.1.200:7000',
        'url': 'http://www.rztech.com'
    },
    'login_info': {
        'user': 'alien',
        'password': 'password'
    },
    'status': 2
}

# for rfid tags management
dict_tags_create = {
    'Tid': '',
    'Epc': '',
    'Userdata': '',
    'Company_code': '',
    'Term_code': ''
}

dict_tags_modify = {
    'Epc': '',
    'Userdata': '',
    'Company_code': '',
    'Term_code': ''
}

# for access_controller management
dict_access_controller = {
    'controllerName': 'testxxxx',
    'serialNumber': '1023',
    'uniqueId': '8888'
}

# for pos management
dict_pos = {
    'name': 'pos0012222222xxxxxx',
    'uniqueId': '8888'
}

# for idcard management
dict_idcard = {
    'currentCard': '8888',
    'uniqueId': 'xxxxx',
    'firstName': 'zhangsssss'
}

# define mapping between data and api type
dict_mapping = {
    'gateways': dict_gateway,
    'beaconstations': dict_beacon_stations,
    'beacontags': dict_beacon_tags,
    'cameras': dict_cameras_create,
    'readers': dict_readers_create,
    'rfidtags': dict_tags_create,
    'access_controller': dict_access_controller,
    'pos': dict_pos,
    'idcard': dict_idcard
}


# 定义测试一卡通的通用方法
def test_one_solution_card(str_api_type, str_res_expect, str_method, str_type=''):
    res = False
    if str_api_type is not 'idcard':
        if str_method == 'POST' and str_type == 'CREATE':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type],
                                json.dumps(dict_mapping[str_api_type]))
        if str_method == 'POST' and str_type == 'MODIFY':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type] + '/' +
                                dict_mapping[str_api_type]['uniqueId'], json.dumps(dict_mapping[str_api_type]))
        if str_method == 'GET':
            pass
        if str_method == 'DELETE':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type] + '/' +
                                dict_mapping[str_api_type]['uniqueId'])
    else:
        if str_method == 'POST' and str_type == 'CREATE':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type],
                                json.dumps(dict_mapping[str_api_type]))
        if str_method == 'POST' and str_type == 'MODIFY':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type] + '/' +
                                dict_mapping[str_api_type]['currentCard'], json.dumps(dict_mapping[str_api_type]))
        if str_method == 'GET':
            pass
        if str_method == 'DELETE':
            res = http_send_req(HOST, PORT, str_method, dict_api_type[str_api_type] + '/' +
                                dict_mapping[str_api_type]['currentCard'])
    if str_res_expect:
        assert str_res_expect == res['ckreturn']
    else:
        assert res