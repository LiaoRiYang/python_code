# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 21:53:11 2021

@author: liaozz
"""
import os
path1 = "D:\\change_name\\img\\"
path2 = "D:\\change_name\\lab\\"
#import random
# 獲取該目錄下所有檔案，存入列表中
f = os.listdir(path1)
#print(len(f))
#random.shuffle(f)
#print(f[0])

high = "140"
angle = "90"

longth =500   #50~500

n = 0
i = 0
number =1  #起始序號
for i in f:
    # 設定舊檔名（就是路徑+檔名）
    oldname1 = f[n]
    oldname2 = oldname1.split(".")[0] + ".txt"
    print(oldname2)

    # 設定新檔名
    
    newname1 = "SQVm500_Low_" + high + "_" + angle+"_" + "%03d"%longth +"_" +"%03d"%number+".jpg"
    # 用os模組中的rename方法對檔案改名
    os.rename(path1+oldname1, path1+newname1)
    print(oldname1, '======>', newname1)
    newname2 = "SQVm500_Low_" + high + "_" + angle+"_" + "%03d"%longth +"_" +"%03d"%number+".txt"
    # 用os模組中的rename方法對檔案改名
    os.rename(path2+oldname2, path2+newname2)
    print(oldname2, '======>', newname2)
    number=number+1
    n+=1
print("end-OK")