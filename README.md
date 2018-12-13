# 统计录屏信息 CountRecordNumber

## 简述

### 目的
为了方便英语组的小伙伴对录屏数量进行查缺补漏
  
为了不麻烦公司IT，自给自足的原则，东拼西凑查询资料花了两晚上写出这个爬虫
### 平台
python
### 所使用库
from urllib import request,parse

from http import cookiejar
 
from datetime import datetime, date, timedelta
  
import re
 
import sys
## 功能 
根据所提供日期信息：
 
1.获取当天应出席人数
 
2.获取当天实到人数
 
3.计算出席率
 
4.计算老师应上传录屏类型与数量
## 下载地址
https://github.com/neninee/GetStudentsInformation/releases
