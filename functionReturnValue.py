# 函数返回值
def sum(a, b):
    sum=a+b
    return sum # 将计算的结果返回
    pass

a=sum(10, 10)
print(a)

# 计算累加和
def cal(num):
    res=0
    i=1
    while i<num:
        res+=i
        i+=1
        pass
    return res
    pass

print(cal(10))