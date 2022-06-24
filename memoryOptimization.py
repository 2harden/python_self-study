# python内存优化

# a=100 # 提前创建小整数池对象【-5，256】
# b=100
# print(id(a))
# print(id(b))

# del a 
# del b
# c=100
# print(id(c))

a=10000 # 大整数池需要我们自己去创建，，创建好之后，存储到池子里，后面无需创建，直接用
b=10000
print(id(a))
print(id(b))

del a 
del b
c=10000
print(id(c))

大整数池和小整数池区别：
1