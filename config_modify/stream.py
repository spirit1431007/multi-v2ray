#! /usr/bin/env python
# -*- coding: utf-8 -*-
import read_json
import write_json
import re
import base_util.v2ray_util as util

mul_user_conf = read_json.multiUserConf

choice=input("请输入要改传输方式的节点Group字母:")
choice=choice.upper()

if len(choice)==1 and re.match(r'[A-Z]', choice) and choice <= mul_user_conf[-1]['indexDict']['group']:
    for sin_user_conf in mul_user_conf:
        if sin_user_conf['indexDict']['group'] == choice:
            index_dict = sin_user_conf['indexDict']
            print ("当前组的传输方式为：%s" % str(sin_user_conf["net"] + " " + sin_user_conf["type"])) 
            break

    print ("")
    #选择新的传输方式
    print ("请选择新的传输方式：")
    print ("1.普通TCP")
    print ("2.HTTP伪装")
    print ("3.WebSocket流量")
    print ("4.普通mKCP")
    print ("5.mKCP + srtp")
    print ("6.mKCP + utp")
    print ("7.mKCP + wechat-video")
    print ("8.mKCP + dtls")
    print ("9.HTTP/2")

    new_stream_network=input()

    if ( not util.is_number(new_stream_network)):
        print("请输入数字！")
        exit
    else:
        if not (new_stream_network > 0 and new_stream_network < 10):
            util.choice_stream(new_stream_network, index_dict)
        else:
            print("请输入有效数字！")
            exit
else:
    print("输入有误，请检查是否为字母且范围中")