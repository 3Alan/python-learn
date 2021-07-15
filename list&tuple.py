# list 可以理解为js中的数组
# .len() 获取长度
array = [1, '2']
print(array[0])

# 与js不同的是， -1表示倒数第一个元素，-2表示倒数第二个...
print(array[-1], array [-2])

# append(element)在末尾追加元素
# insert(index, element) 在指定索引处添加元素
# pop([index]) 删除[指定索引处元素]/末尾元素
array.append('append')
print(array, 'append')

array.insert(1, 'insert')
print(array, 'insert')

array.pop()
print(array, 'pop')



# ---------------------------------------------------------
# tuple:用()包裹，一但初始化就不能改变
# (1)只是代表1，(1,)才是tuple

print((1, 2, '3'))