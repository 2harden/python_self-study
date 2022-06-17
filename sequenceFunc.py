# 序列操作 （字符串，元组，list）

print('==============all() func')
# 元素除了0 空 False外都算true
print(all([]))
print(all(()))
print(all([1,2,4]))
print(all([1,2,4,0]))

print('==============any() func')
#类似与逻辑运算符or的判断，有一个元素为真就返回true
print(any((3,3,0)))

print('==============sorted() func')
#对所有可迭代对象进行排序操作,对list进行操作
li=[2,3,33,1,23,20]
print(sorted(li))
print(li)

print('==============range() func')
# 函数可创建一个整数列表，一般用在for循环中


print('==============zip() func')
# 就是用来打包的，会把序列中对应的索引位置的元素存储为一个元组，然后再输出
# 如果元素对应不少，按照最少的压缩
s1=['a','b','c']
s2=['he','she','me']
s3=['l','m','s','d','s']
print(list(zip(s1)))  # 实际上已经打包
print(list(zip(s1,s2))) # 两个参数
print(list(zip(s1,s3))) 

print('==============enumerate() func')
# enumerate函数用于将一个可遍历的数据对象（如列表、元组、字符串）组合为一个索引序列，同时列出数据和数据下标
# 一般用在for循环中
listO=['a','b','c']
for i in enumerate(listO):
    print(i)
    
for index,item in enumerate(listO,5): # 下标从5开始
    print(index,item)