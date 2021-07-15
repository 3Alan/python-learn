#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串---------------------------------------------
# 多行写法，有点类似于js的``
print('''-line1
-line2
-line3''')

# 在前面加上r表示不转义
print(r'\n')

# 布尔值 True/False----------------------------------
print('3 > 2', 3 > 2)

# 布尔值运算符 and/or/not
print('True and False->', True and False)
print('True or False->', True or False)
print('not False->', not False)


# 变量/赋值相关
a = 'a'
b = a
a = 'changedA'
print(a, b)

print(10/3)
# 整除：向下取整 
print(10//3)


# 字符串在内存中以`Unicode`表示

# 对应字符转化成字符编码
print(ord("C")) 
# 转化成对应字符
print(chr(77)) 

# 字符串前面带b表示bytes类型
# 例如：b'AC'
# 字符串可以使用encode([encoding="utf-8"][,errors="strict"])转化成对应编码格式

# 计算字符长度
print(len('CCC '))

print('python学习')


# 常用字符串占位符
# %s 字符串
# %d 整数
# %f 浮点数
print('Hello %s' % ('Alan'))
print('%02d' % 3)
print('%.3f' % 3.1415)

# format格式化字符。替代占位符{0} {1} ...
print('Hello {0}, My name is {1}'.format('everyone', 'Alan'))

# f-string非常类似于js中的字符串模板,变量后接: 可以进行格式化
name = 'Alan'
age = 24.000
print(f'My name is {name}, {age:.1f} years old')