#coding=utf-8

import requests
import string

from bs4 import BeautifulSoup

# 检测网关是否登录，返回网关登录状态
def lgn_test():
    url = "https://lgn.bjut.edu.cn/"
    r = requests.get(url, timeout=5)
    r.encoding = 'gb2312'
    html = r.text   # 获取网页信息
    # print(html)   # 输出网页内容
    html = BeautifulSoup(html, 'html.parser')   # 用BeautifulSoup解析数据  python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
    title = html.title      # 读取title内容
    titlestr = str(title)   # 转换为string类型
    # print(titlestr)
    if titlestr == "<title>北京工业大学上网信息窗                  </title>":
        return True
    else:
        return False

# 登录网关，返回登录结果
def lgn():
    url = "https://lgn.bjut.edu.cn/"                    # 设置目标url
    postdata = {                                            # post携带的字符串
        'DDDDD': '14024210',    # 用户名
        'upass': '211211',      # 密码
        'v46s': '1',        # 登录类型  0：IPV4+IPV6    1：IPV4   2：IPV6
        'v6ip': '',
        'f4serip': '172.30.201.10',
        '0MKKey': ''
    }
    r = requests.post(url, data=postdata, timeout=5)          # 向指定url发送post信息
    r.encoding = 'gb2312'
    html = r.text   # 获取网页信息
    # print(html)   # 输出网页内容
    html = BeautifulSoup(html, 'html.parser')   # 用BeautifulSoup解析数据  python3 必须传入参数二'html.parser' 得到一个对象，接下来获取对象的相关属性
    title = html.title      # 读取title内容
    titlestr = str(title)   # 转换为string类型
    # print(titlestr)
    if titlestr == "<title>登录成功窗</title>":
        return True
    else:
        return False
