#coding=utf-8

import requests
from bs4 import BeautifulSoup

def lgn_test():
    url = "https://lgn.bjut.edu.cn/"
    r = requests.get(url, timeout=5)
    r.encoding = 'gb2312'
    html = r.text   # 获取网页信息
    # print(html)   # 输出网页内容
    html = BeautifulSoup(html, 'html.parser')   # 用BeautifulSoup解析数据  python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
    title = html.title   # 读取title内容
    print(title)      # 输出title内容
    if title == '<title>北京工业大学上网信息窗                  </title>':
        print("1")
        return True
    else:
        print("2")
        return False

def lgn():
    print("\n开始登录lgn网关\n")
    url = "https://lgn.bjut.edu.cn/"                    # 设置目标url
    postdata = {                                            # post携带的字符串
        'DDDDD': '14024210',    # 用户名
        'upass': '211211',      # 密码
        'v46s': '1',        # 登录类型  0：IPV4+IPV6    1：IPV4   2：IPV6
        'v6ip': '',
        'f4serip': '172.30.201.10',
        '0MKKey': ''
    }
    r = requests.post(url, data=postdata, timeout=0.1)          # 向指定url发送post信息
    r.encoding = 'gb2312'
    print("返回信息：\n",r.text,"\n")                         # 输出返回的信息
    return True
