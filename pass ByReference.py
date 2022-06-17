a=1
def func(x):
    print('x的地址：{}'.format(id(x)))
    x=2
    print('x修改后的地址：{}'.format(id(x)))
    pass

# 调用函数
print('a的地址：{}'.format(id(a)))
func(a)
print(a)

# 可变类型
li=[]
def testF(p):
    print(id(p))
    pass

print(id(li))