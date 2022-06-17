# property属性函数

class Person(object):
    # 方式一
    # def __init__(self):
    #     self.__age=10
    # def getAge(self):
    #     return self.__age
    # def setAge(self, age):
    #     if age < 0:
    #         print('age can not less than 0')
    #     else:
    #         self.__age=age
    #         pass
    #     pass
    # # 定义一个类属性，实现通过直接访问的形式去访问私有的属性
    # age=property(getAge, setAge) # 传入get,set方法
    
    # 方式二
    @property # 用装饰器修饰,添加属性标志,提供一个getter方法
    def age(self):
        return self.__age
    pass
    @ age.setter # 提供一个setter方法
    def age(self, params):
        if params < 0:
            print('age can not less than 0')
        else:
            self.__age=params
            pass
    pass

    
p=Person()
p.age=30 # 可以修改
print(p.age)
