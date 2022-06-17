tupleA=()
print(id(tupleA)) # 打印元组内存地址
tupleA=('adb', 88 , 'perter' ,[33,22,11]) # 元组不能修改,只能查找
print(type(tupleA))
print(tupleA)

# 元组查询
for i in tupleA:
    print(i, end=' ')
    pass

# 元组切片操作
print('\n')
print(tupleA[2:4])
print(tupleA[::-1]) # 倒序输出
print(tupleA[::-2]) # 隔两个倒序输出
print(tupleA[-2:-1:]) # 倒着取小标为-2到-1之间的数据
print(tupleA[-4:-1:]) 

# 对元组中列表元素的修改
tupleA[3][0]=23434
print(tupleA)

# 当元组中只有一个数据的时候,必须要在第一个元素后加上逗号
tupleB=('2',)
print(type(tupleB))


tupleC=tuple(range(10))
print(tupleC)
print(tupleC.count(8)) # 包含几个8