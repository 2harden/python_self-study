print(abs(-32)) # 求绝对值

print(round(3.55,1)) # 近似值

print(pow(3,3)) # 求次方

print(max(23, 2354,43)) # 求最大值

print(sum(range(50) ,3 ))  # sum的使用

# eval 执行表达式
a,b,c=1,2,3
print(eval('a+b+c')) # 动态执行

# 类型转换函数
print(bin(10)) # 10进制转换二进制

print(hex(23)) # 0进制转换十六进制

# 元组转换成列表
tup=(1,2,3,4)
print(type(tup)) 
li=list(tup)
print(type(li)) 
print(li)

tupList=tuple(li)
print(type(tupList)) 
print(tupList)

# 字典操作
dic=dict(name='peter',age=23)
print(type(dic)) 
print(dic)