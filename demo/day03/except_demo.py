#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/6'


def div(a,b):
    try:
        c =a/b
    except ZeroDivisionError:
        print("除数不能为0")
        return


    return c

print(div(12,0))

def operate_file():
    try:
        g = open("test.txt",'a')
        g.read()
        g.close()
        g.write("bbbbbb")
    except FileNotFoundError:
        print("文件不存在")
    except ValueError:
        print("文件已关闭")


operate_file()


