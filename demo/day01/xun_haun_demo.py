#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/5'
'''
i =1
while(判断条件)：
     循环体
     i =i+1

'''
for i in range(1,101,1):
    print (i)


i = 1
while(i < 101):
    print (i)
    i = i +1


# for 循环
'''
range(0,10,1) = [1,2,3,4,5,6,7,8,9]
range(0,10,2) = [1,3,5,7,9]
for i in range(0,10,1):
    代码块

'''
for i in range(10):
    print(i)

# while

for i in range(1,10,2):
    print(i)

for i in range(1,100,2):
    print(i)

# 求出100以内的奇数
for i in range(1,100):
    if(i%2 == 1):
        print(i)

# 终止循环 break


# 跳过本次循环 continue

# 100以内 到5就终止
for i in range(100):
    if(i == 5):
        break
    print(i)

# 100以内 到5就跳过
for i in range(100):
    if(i%5 == 0):
        continue
    print(i)

# 1000以内 到3就终止
for i in range(50):
    if(i == 3):
        break
    print(i)



# 求出 1+2+3+...100 的和
# 方法一
a = 0
for i in range(1,101):
    a = a + i
    print(a)

# 方法二



# 求出 100! 1*2*3*4...*100


# 打印出九九乘法表(循环嵌套)


# 冒泡排序