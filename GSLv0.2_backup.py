from urllib import request,parse
from http import cookiejar
from datetime import datetime, date, timedelta
import re
import sys
# 创建cookiejar实例对象
cookie = cookiejar.CookieJar()
# 根据创建的cookie生成cookie的管理器
cookie_handle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handle = request.HTTPHandler()
# 创建https管理器
https_handle = request.HTTPSHandler()
# 创建求求管理器，将上面3个管理器作为参数属性
# 有了opener，就可以替代urlopen来获取请求了
opener =  request.build_opener(cookie_handle,http_handle,https_handle)

username = input("输入用户名：")
password = input("输入密码:")

# username = 'tangguofang'
# password = 'b890kl'


# date_pre = '2018-12-01'
# date_for = '2018-12-03'
# dates = ['2018-12-01','2018-12-02','2018-12-03']

date_pre = input("输入起始日期（例：2018-01-01）：")
date_for = input("输入起始日期（例：2018-01-01）：")

# date_pre = '2018-12-01'
# date_for = '2018-12-09'

date_pre_datetime = datetime.strptime(date_pre, "%Y-%m-%d")
date_for_datetime = datetime.strptime(date_for, "%Y-%m-%d")

days = []

while date_pre_datetime != date_for_datetime:
    days.append(date_pre_datetime.strftime("%Y-%m-%d"))
    date_pre_datetime = date_pre_datetime + timedelta(days=1)
days.append(date_for_datetime.strftime("%Y-%m-%d"))




def login(username,password):
    '''
    负责初次登录
    需要传递用户名和密码，来获取登录的cookie凭证
    '''
    # 登录url，需要从登录form的action属性中获取
    url = 'http://v2t.171xue.com/Login/loginCheck.html'
    # 登录所需要的数据，数据为字典形式，
    # 此键值需要从form扁担中对应的input的name属性中获取
    data = {
    'username':username,
    'passwords':password
    }
    # 将数据解析成urlencode格式
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url,data=data)
    # 正常是用request.urlopen(),这里用opener.open()发起请求
    response = opener.open(req)
    print(response.read().decode('utf-8'))
    #print(cookie)
def getInformation(day):
    '''
    获取登录后的页面
    '''
    # 此url是登录后的链接地址
    url = 'http://v2t.171xue.com/Index/day_course_detail.html'
 
    # 如果已经执行了上面的login函数，
    # 那么此时的opener已经是包含了cookie信息的一个opener对象

    #课表日期选择-字典
    dic = {'day':day}
    #字典转换成byte
    data = bytes(parse.urlencode(dic),encoding='utf8')

    res = opener.open(url,data=data)
    html = res.read().decode('utf-8')
    
    # print (html)
    # with open('renren.html','w') as f:
    #     f.write(html)
 
    # def getInformation():
    results = re.findall('<span class = "left">.*?\n.*?;(\d.{10}).*?</span>.*?<a href=".*?>(\S.*?)</a>.*?<td>\n.*?(\S.*?)\n.*?</td>.*?<td>\n.*?(\S.*?)\n.*?</td>.*?',html,re.S)
    #<td>\n.*?(\S.*?)\n.*?</td>.*?'

    #当天学生总数
    total = len(results)
    #出席人数
    attend = 0

    print ('------',day,'------')
    for result in results:
        print(result[0],result[1],result[2],result[3])
        if result[2]=='到':
            attend=attend+1
    print ('当天人数：',total)
    print ('出席人数：',attend)
    if total != 0:
        print (' 出席率：',attend/total*100,'%')

    #如果二门或三门连续的课都为正式课，则开始判断是否是1vn
    count = 0
    #if results[count][3] == '正式课' and results[count+1][3] == '正式课':
        #判断第一个时间与第二个时间是否相差十五分钟或三十分钟:
            #若是，则判断第二个时间和第三个时间是否相差十五分钟：
                #若是则 1v3 的数量+1
                #否则 1v2 的数量+1

if __name__ == '__main__':
    '''
    依次执行上面两个函数
    '''
    login(username,password)

for day in days:
    getInformation(day)

i = input('输入任意键+回车退出')