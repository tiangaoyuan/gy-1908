#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/5'
# 无参数， 无返回值方法
#方法的定义
def jia_fa():
    a = 1
    b = 2
    print (a+b)

# 方法调用
jia_fa()


# 无参数， 无返回值方法
# 方法的定义
def jia_fa(a,b):
    print (a + b)


# 方法调用
jia_fa(3,5)
jia_fa(200,50)

# 无参数， 有返回值方法
#方法的定义
def jia_fa():
    a = 1
    b = 2
    return a +b

c = jia_fa()
print (c)

# 有参数  有返回值
def jia_fa(a,b):
    return a + b

c = jia_fa(8,5)
print (c)


def bbb(a,b=12):
    return  a + b

print (bbb(11))
print (bbb(11,30))
print (bbb(1,b=20))

def aaa(*args,**kwargs):
    print (args)
    print(kwargs)

aaa({'name':'田高远'},4,5,6,7,8,b=100,c=101)


if __name__ == '__main__':
    #程序的入口
    print ("志存高远诚信赢天下")