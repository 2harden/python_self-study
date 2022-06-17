dictA={}
# 添加
print('===========add==============')
dictA={"pro":'art' , 'school':'harbin.u'}
dictA['name']='szc' # key:value
dictA['age']=30

print(type(dictA))
print(dictA)
print('===========find==============')
print(dictA['name'])

print('===========modify==============')
dictA['name']='dlh'
dictA['school']='hongkong.u'
dictA.update({'age' : 18}) # 修改
dictA.update({'height' : 1.80}) # 添加
print(dictA)

# 获取所有的键   
print(dictA.keys())

# 获取所有的值
print(dictA.values())

# 获取所有的键值对
print(dictA.items())

print('===========delete==============')
del dictA['name']
dictA.pop('age')
print(dictA)

print('===========sort==============')
print(sorted(dictA.items(), key=lambda d:d[0])) # 按照Key排序

print(sorted(dictA.items(), key=lambda d:d[1])) # 按照value排序 ,会报错,改age类型

