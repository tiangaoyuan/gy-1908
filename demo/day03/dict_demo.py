#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/6'

# key :velue
# key 唯一  必须是不可变的，数字， 字符串，元组，列表（不可以），字典（也不可以）

# 增
# 初次创建

d = {}
dl ={'name':'小强同学','sex':'男'}
# 新增一对数据
dl['age'] = 18
dl['班级'] = '国宝班'
#dl['age'],dl['班级'] = 18, '国宝班'
print(dl)

# 删
# 删除key
print(dl.pop('班级'))
print(dl)
#另一种方法
del dl['sex']
print(dl)

#删除整个字典
# del dl
# print(dl)
# #清空
# dl.clear()
# dl = 0
# 改
dl['name'] = '小红同学'
print(dl)

# 查
print(dl['name'])


#获取字典长度
print(len(dl))

# 成员判断，只能用key做判断
print('name' in dl)

# 字典拼接
# 在某个字典末尾加上另一个字典
# 拿着d3修改d2, d2中key有则改value，无则新增
d2 = {'1':'231','2':'456'}
d3 = {'2':'789' ,'4':'186'}
d2.update(d3)
print(d2)

#生成一个新的字典
c = dict(d2,**d3)
print(c)
