
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