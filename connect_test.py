#coding=utf-8

import requests
from requests.exceptions import ReadTimeout,ConnectionError,RequestException

def test():
    print("\n=========网站访问测试=========\n")
    status = True   # 连接状况指示
    try:
        r = requests.get('https://lgn.bjut.edu.cn/')
        print("状态码：", r.status_code, "\n")      # 如果能获得状态码，则会显示状态码
    except ReadTimeout:
        print("连接超时！\n")
        status = False
    except ConnectionError:
        print("连接异常！\n")
        status = False
    except RequestException:
        print("其他异常！\n")
        status = False
    else :
        print("网站访问正常，无异常出现。\n")
    print("==============================\n")
    return status