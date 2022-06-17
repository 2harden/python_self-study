# 私有化属性

class Person:
    def __init__(self):
        self.__name='peter' # 加下划线，将属性私有化
        self.age=30
        pass
    def __str__(self):
        return '{} age is {}'.format(self.__name, self.__age) # 类内部可以访问

x=Person()
print(x)
# print(x.__name) // 不能访问

class Student(Person):
    pass

stu=Student()
print(stu.age)
print(stu.__name)  # 子类不能继承父类的私有化属性，只能继承公有的