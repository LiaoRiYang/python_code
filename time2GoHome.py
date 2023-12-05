# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:46:34 2022

@author: liaozz
"""

import time

#打卡時間
timeString = "08:58:00" # 時間格式為字串

################################
################################
year= "2020-09-09 "  #這是多少都沒差  
timeString2=year+timeString
struct_time = time.strptime(timeString2, "%Y-%m-%d %H:%M:%S") # 轉成時間元組
time_stamp = int(time.mktime(struct_time)) # 轉成時間戳
#print(time_stamp)

time_stamp+=33360  #加上9:15的上班時間


struct_time = time.localtime(time_stamp) # 轉成時間元組
timeString = time.strftime("%H:%M:%S", struct_time) # 轉成字串
print("下班時間:",timeString)