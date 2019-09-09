#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/4'

'''
if(条件)：
   代码块
else:
    代码块

'''

# 小明去超市买东西，如果遇到西瓜，买一个
a = 1 # 1代表有西瓜，0代表没有西瓜+

if(a == 0):
    print("买一个西瓜")
else:
    print("回家洗洗睡吧")


a = 1 # 1代表有老婆，0代表是个光棍
if(a == 1):
    print("有老婆")
else:
    print("回家洗洗睡吧")

'''
if(条件)：
     代码块
elif(条件)：
     代码块
else:
     代码块 

'''
# 80分优秀 60-80良好 60 及格  60分以下不及格 小明考试70  是什么等级
# 方法一
s = 70
if(s >= 80):
    print("小明成绩为优秀")
if(s >= 60 and s < 80):
    print("小明成绩为良好")
if(s <  60):
    print("小明成绩为不及格")
# 方法二
s = 70
if(s >= 80):
    print("小明成绩为优秀")
elif(s >= 60):
    print("小明成绩为良好")
else:
    print("小明成绩为不及格")
