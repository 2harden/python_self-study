# 属性 （分为类属性和实例属性）
# 类属性

class Student:
    name='peter' # 属于类属性
    def __init__(self, age):
        self.age=age # 实例属性
        pass

p=Student(28)
print(p.name) # 通过对象访问类属性


print(Student.name) # 通过类对象访问name
print(Student.age) # 报错