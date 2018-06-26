#coding=utf-8

import requests

def lgn_test():
    return True

def lgn():
    print("\n开始登录lgn网关\n")
    url = "https://lgn.bjut.edu.cn/"                    # 设置目标url
    postdata = {                                            # post携带的字符串
        'DDDDD': '14024210',    # 用户名
        'upass': '211211',      # 密码
        'v46s': '1',        # 登录类型  0：IPV4+IPV6    1：IPV4     2：IPV6
        'v6ip': '',
        'f4serip': '172.30.201.10',
        '0MKKey': ''
    }
    r = requests.post(url, data=postdata, timeout=0.1)          # 向指定url发送post信息
    print("返回信息：\n",r.text)                                               # 输出返回的信息
    return True