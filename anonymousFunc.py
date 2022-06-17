# 没有名字的函数
M = lambda x,y:x+y # 定义函数
print(M(2,3)) # 调用匿名函数


N=lambda a,b,c:a*b*c
print(N(3,3,3))

age=28
print('可以参军' if age>18 else '继续上学')

# 匿名函数改法
rs=(lambda x,y:x if x>y else y)(15, 12) # 直接调用
print(rs)