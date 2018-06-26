#coding=utf-8

import requests
import lgn,connect_test

# 测试网络连接情况（测试能否访问lgn网关）
status = connect_test.test()
if status == False:
    print("网关访问失败\n")
    exit(0)     # 无法连接到lgn网关，程序停止运行

# 检测是否登录
status = lgn.lgn_test()
if status == True:
    print("网关已经登录")
    exit(0)                 # 自动登录程序停止运行
else:
    print("网关尚未登录") # 继续进行网关登录

# 登录lgn
status = lgn.lgn();
if status == False:
    print("网关登录失败\n")
else:
    print("网关登录成功\n")