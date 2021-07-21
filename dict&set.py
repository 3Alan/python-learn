# dict 类似js中的对象
dic = {'Alan': 24, 'Bob': 25, 'Jay': 23}
print(dic['Bob'])
dic['Jay'] = 26
print(dic)
print('Mary' in dic)

# 获取对应key的值，没有则返回None,也可以指定第二个参数（在为None时才会生效）
print(dic.get('Jack', 'sorry'))

# 删除key对应的值
dic.pop('Bob')
print(dic)


# ---------------------------------------------------------------------
# set：接受一个list作为参数，且key值不会重复
s = set([1,2,3,3])
print(s)

# 添加元素：add(key)，移除元素：remove(key)