#/bin/bash

# 网关信息
URL="http://lgn.bjut.edu.cn"
StuID="14024210"
Passwd="211211"

# 提取HTML的Title标签
curl $URL 2>/dev/null | iconv -f gb2312 -t utf-8 > tmp.txt
TITLE=$(awk -vRS="</title>" '/<title>/{gsub(/.*<title>|\n+/,"");print;exit}' tmp.txt)
rm tmp.txt
#echo "网关页面标题：$TITLE"

# 判断登录状态
if [ "$TITLE" = "北京工业大学上网登录窗                  " ]
then
	echo "网关尚未登录"
elif [ "$TITLE" = "北京工业大学上网信息窗                  " ]
then
	echo "网关已经登录"
	exit 0						# 网关已经登录，脚本停止运行，正常退出
else
	echo "网关状态获取失败"
	exit 1						# 网关状态异常，脚本停止运行，退出并提示异常
fi

# 若未登录，则自动登录
sleep 1
curl -d "DDDDD=$StuID&upass=$Passwd&v46s=1&v6ip=&f4serip=172.30.201.10&0MKKey=" $URL 2>/dev/null | iconv -f gb2312 -t utf-8 > tmp.txt
TITLE=$(awk -vRS="</title>" '/<title>/{gsub(/.*<title>|\n+/,"");print;exit}' tmp.txt)
rm tmp.txt
if [ "$TITLE" = "登录成功窗" ]
then
	echo "登录成功"
	exit 0						# 登录成功，正常退出
else
	echo "登录失败"				# 登录失败，退出并提示异常
	exit 1
fi
