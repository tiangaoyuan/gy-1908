#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/4'

# for循环
'''
for i  in range(0,10):
     代码块
'''

for i  in range(10):
    print("田高远是个不错的人")

# 打印出100以内的奇数
for i  in range(1,100,2):
    print(i)

for i  in range(1,100):
    if(i%2 == 1):
        print(i)
# 求出1+2+3+...100和
a = 0
for i in range(0,100):
    a += (i+1)
print(a)

# 求出100! 1*2*3*4*...100
s =1
for i in range(1,101):
    s *= i
print(s)
#求出100以内的质数
def zhi_shu():
    for i in range(2,101):
        if(i == 2):
            print(i)
            continue
        f = 1 # 1代表这个数是质数，0代表这个数不是质数
        for j in range(2, i):
            if (i % j == 0):
                f = 0
                break
        if(f == 1):
            print(i)
# 打印九九乘法表 （循环嵌套）
# 冒烟排序

# 终止循环  break

#打印出100以内的数，遇到5就终止
for i in range(100):
    if(i == 5):
        break
    print(i)

# 跳过本次循环 continue
# 打印出100以内的数，如果可被5整除则跳过
for i in range(100):
    if(i%5 ==0):
        continue
    print(i)




# whili