#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/5'

# 截取
a = "aaaaaghgagygbvu"
# 截取其中一段
print(a[1:5])
print(a[5:])
print(a[:7])
print (a[:-2])

# 字符串倒叙排序
print(a[::-1])

#dergakio  要求生成两个新的字符串  drai和egko
b = "dergakio"
print (b[::2])
print (b[1::2])


# 通过下标取出字符串中的字符
print (b[2])

# 重复字符串
print (b * 6)

# +字符串拼接

# in 成员判断

# 字符串切片
d = '用例名,充值金额,断言'
print (d.split(","))

# 去空格

e ='   hguiqghnh9  '
print (e.strip())
# 去左空格
print (e.lstrip())
# 去有空格
print (e.rstrip())

# 替换
f = 'ddfjjiougqjop"19898479'
print (f.replace('"',"'"))

# 查找
g ='guoyasoft'
print (g.find("ya"))

# 长度
print (len(g))

# 练习题
'''
GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1


'''
q = 'GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1'
