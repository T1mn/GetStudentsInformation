# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 18:23:15 2018

@author: Tim
"""
from urllib import request,parse
from http import cookiejar
from datetime import datetime, date, timedelta
import re
import os
def inputSth():#获取教师端帐号密码
    usern = input('输入你的帐号名：')
    passn = input('输入你的密码：')
    date_0 = input("\n  输入起始日期（例：2018-01-01）：")
    date_1 = input("\n  输入起始日期（例：2018-11-11）：")
    date_0_dt = datetime.strptime(date_0, "%Y-%m-%d")
    date_1_dt = datetime.strptime(date_1, "%Y-%m-%d")
    days = []
    while date_0_dt != date_1_dt:
        days.append(date_0_dt.strftime("%Y-%m-%d"))
        date_0_dt = date_0_dt + timedelta(days=1)
    days.append(date_1_dt.strftime("%Y-%m-%d"))
    return usern,passn,days
def iniOpener():#初始化启动器
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
    return opener
def loginAndGetCookies(username,password):#登录并获取cookies
    url = 'http://v2t.171xue.com/Login/loginCheck.html'
    data = {
    'username':username,
    'passwords':password
    }
    # 将数据解析成urlencode格式
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url,data=data)
    # 正常是用request.urlopen(),这里用opener.open()发起请求
    response = opener.open(req)
    resTran = response.read().decode('utf-8')
#    print(resTran)
    if ('验证成功' in resTran) == True :
        print("************登录成功************")
    else:
        print("****登录失败，请检查帐号密码****")
def getCouInfo(day):#获取当日课表html
    url = 'http://v2t.171xue.com/Index/day_course_detail.html'
    #课表日期选择-字典
    dic = {'day':day}
    #字典转换成byte
    data = bytes(parse.urlencode(dic),encoding='utf8')

    res = opener.open(url,data=data)
    html = res.read().decode('utf-8')
    print(html)
if __name__ == '__main__':
    opener = iniOpener()
    #初始化启动器
    userInfo = inputSth()
    #获取教师端帐号密码
    loginAndGetCookies(userInfo[0],userInfo[1])
    #登录并获取cookies
    getCouInfo('2018-12-08')
    