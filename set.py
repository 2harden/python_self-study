# 无序且不重复的容器

# 创建集合
dic1={1:3}
set1={1,2,3}
set2={3,2,4}
print(type(set1))
print(type(dic1))

print('===============add')
set1.add('python')
print(set1)

print('===============clear')
# 清除
# set1.clear()
print(set1)

print('===============difference')
# 取差集
print(set1.difference(set2))
print(set1)
