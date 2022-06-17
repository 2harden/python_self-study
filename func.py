def printInfo():
    '''
    打印个人信息
    :return:
    '''
    print('liudan is my gf')
    pass

# 函数的调用
# 
printInfo()

# def printInfo2(name, height, weight, hobby):
#     print('s%的身高是f%' %(name, height))
#     print('s%的体重是f%' %(name, weight))
#     print('s%的爱好是s%' %(name, hobby))
#     pass

# # 函数调用
# printInfo2('li', 182.0, 200.0, 'play games')
 
# 1,必选参数
def sum(a, b): # 形式参数
    sum=a+b
    print(sum)
    pass

sum(3, 3) # 实参

# 2, 默认参数（缺省参数）
def sum1(a=30, b=20):
    print(a+b)
    pass

sum1()

#3,可变参数 （当参数的个数不确定时使用，比较灵活）
def getComputer(*args):
    res=0
    for i in args:
        res+=i
        pass
    print(res)
    pass

getComputer(1,2,3,4,5,6)
getComputer(1,2)

# 4,关键字可变参数
def keyFunc(**kwawrgs):
    print(kwawrgs)
    pass

dictA={'name':'li', 'age':25}

# 函数调用
keyFunc(**dictA)
keyFunc(name="peter", age=25)
keyFunc() 