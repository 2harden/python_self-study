a=[1,2,3,'hello']
b='szc'
print(len(b))
print(type(a))
print(len(a)) # 获取list中的数据个数

# list 切片操作
listA=['adb', 89, 23.34,'df', True]
print(listA)
print(listA[2])
print(listA[1:3]) # 不包含第三个
print(listA[2:]) # 获取到最后
print(listA[::-1]) # 倒序输出
print(listA*3) # 输出多次

# list常用函数
print('=================add=================')
listA.append(['fff', 'dddddd'])
print(listA)
listA.insert(1,'sdfasdf')
print(listA)
listA.extend([22,33,33])
print(listA)
print('=================modify=================')
listA[0]='peter'
print(listA)
print('=================delete=================')
del listA[0]
print(listA)
# del listA[3,4]  # list indices must be integers or slices, not tuple
print(listA) 
listA.remove(33) # 删除指定项
print(listA)

listA.pop(4) # 按照下标移除
print(listA)
# print(listA.index(2))