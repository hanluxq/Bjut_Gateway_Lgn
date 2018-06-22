#coding=utf-8

import requests

# 设置目标url
url = "https://lgn.bjut.edu.cn"

# post携带的字符串
postdata = {
    'DDDDD':'14024210', # 用户名
    'upass':'211211',   #  密码
    'v46s':'1',     # 登录类型 0：IPV4+IPV6    1：IPV4     2：IPV6
    'v6ip':'',
    'f4serip':'172.30.201.10',
    '0MKKey':''
}

# 向指定url发送post信息
r = requests.post(url,data=postdata)

# 输出返回的信息
print(r.text)