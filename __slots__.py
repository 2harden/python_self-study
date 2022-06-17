# __slots__属性限制
class Student(object):
    __slots__ = ('name', 'age')
    def __str__(self):
        return '{}...{}'.format(self.name, self.age)
    pass

szc=Student()
szc.name='szc'
szc.age=20
# szc.score=96 # 动态添加属性会报错
# print(szc.__dict__)
print(szc)

class SubStudent(Student):
    # __slots__ = () # 子类声明__slots__，不能再修改父类属性
    __slots__ = ('gender')
    pass

dlh=SubStudent()
dlh.gender='mile'
print(dlh.gender)