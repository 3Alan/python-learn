# 函数可以返回多个结果，使用def关键字定义函数
def sayHello(age, sex):
  if age > 18:
    return 'adult', 'man'
  else:
    return 'minor', 'woman'

# 返回的是一个元组tuple
res = sayHello(24, '男')
print(res)

identity, sex = sayHello(16, '女')
print(identity, sex)