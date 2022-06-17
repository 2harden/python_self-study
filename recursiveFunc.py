# 求阶乘
def func(n):
    res=1
    for i in range(1, n+1):
        res*=i
        pass
    return res
pass
print('{}'.format(func(10)))

'''
递归函数
'''
def func2(n):
    if n==1:
        return 1
    else:
        return n*func2(n-1)
    pass

print(func2(10))