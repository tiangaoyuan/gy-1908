#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'tiangy'
#__mtime__ = '2019/9/5'
# 新增数据
# 在列表最后新增单个数据
l = [1,2,3,4,5,6,7,8,9]
l.append(11)
print (1)
# 在列表的某个位置新增单个数据
l.insert(3,11)
print (l)

# 在列表最后新增多个数据
y = [9,9,7,7]
l.extend(y)
print(l)
print(y)

# 删除数据
print (l.pop())
print (l)
print (l.pop(11))
print (1)
print (l.pop(-2))
print (l)

# 根据内容删除数据
l.remove(2)
print (l)

# 修改列表中的数据
l[2]=12
print (l)

# index
print (l.index(1))
l[l.index(1)]=9
print (l)

# 长度
print(len(l))

#排序 reverse排序规则False升序True降序
l.sort(reverse= True)
print (l)

