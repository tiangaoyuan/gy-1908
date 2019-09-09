#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/5'

# 打印出100以内的奇数
def iii():
    for i  in range(1,100,2):
        print(i)

def ppp():
    for i  in range(1,100):
        if(i%2 == 1):
            print(i)
# 求出1+2+3+...100和
def qiu_he():
    a = 0
    for i in range(0,100):
        a += (i+1)
    print(a)

# 求出100! 1*2*3*4*...100
def qiu_ji():
    s =1
    for i in range(1,101):
        s *= i
    print(s)
#求出100以内的质数
def zhi_shu():
    for i in range(2,100):
        for j in range(2,i):
            if(i%j  ==0):
                break
    else:
        print (i)





# 打印九九乘法表 （循环嵌套）
# 冒烟排序

# 终止循环  break
# 跳过本次循环 continue
# 打印出100以内的数，如果可被5整除则跳过
def qiu_ji3():
    for i in range(100):
        if(i%5 ==0):
            continue
        print(i)
#打印出100以内的数，遇到5就终止
def qiu_ji1():
    for i in range(100):
        if(i == 5):
            break
        print(i)

if __name__ == '__main__':
    qiu_he()
    zhi_shu()





