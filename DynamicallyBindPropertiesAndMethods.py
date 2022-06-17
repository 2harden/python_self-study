# 动态绑定属性和方法
import types # 添加方法的库
def dynamicMethod(self):
    print('{} weight is {}kg, study at {}'.format(self.name, self.weight, self.school))
    pass
@classmethod # 绑定类方法
def classTest(cls):
    print('this is class method')
    pass
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        pass

    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)
        pass

szc=Student('szc', 20)
szc.weight=60 # 动态绑定
szc.school='Harbin University' # 动态绑定
szc.printInfo=types.MethodType(dynamicMethod, szc)

print(szc)

Student.school='harbin university' # 动态类属性
print(szc.school)
 
print('=====================dynamic add func')
szc.printInfo()
print('=====================dynamic add class func')
Student.TestMethod=classTest
Student.TestMethod()
szc.TestMethod() # 实例对象直接调用



