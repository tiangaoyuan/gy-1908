#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/6'

# 作用，打开一个文件
# 参数1：文件路径
#参数2：打开方式，r读  w先清空文件内容，然后在写入 a 追加写入
f = open("test.txt","r",encoding='utf-8')
# 按行读取文件内容，返回一个列表
#print(f.readlines())
## 按行读取文件所有内容，返回一个字符串
print(f.read())
# 关闭文件
#f.close()


f = open("test.txt","a",encoding='utf-8')
f.write("eiuwhvjigwqenognvi")
f.writelines(["ghrjihvghnnn\n","iynyugjviai\n"])