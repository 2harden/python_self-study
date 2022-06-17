# 多态

class Animal: # 父类
    def say(self):
        print('(Animal)I am a animal')
        pass
    pass

class Duck(Animal): # 派生类
    def say(self): # 重写
        print('(Duck)I am a animal')
        pass
    pass

class Dog(Animal): 
    def say(self):
        print('(Dog)I am a animal')
        pass
    pass

class Cat(Animal): 
    def say(self):
        print('(Cat)I am a animal')
        pass
    pass

class Bird(Animal): 
    def say(self):
        print('(Bird)I am a animal')
        pass
    pass

class People(): 
    def say(self):
        print('(People)I am a people')
        pass
    pass

class Student(People): 
    def say(self):
        print('(Student)I am a student')
        pass
    pass


def commonInvoke(obj):
    obj.say()
    pass

listO=[Duck(), Dog(), Cat(), Bird(), Student()]
for i in listO:
    commonInvoke(i)
# duck=Duck()c
# duck.say()

# dog=Dog()
# dog.say()

# cat=Cat()
# cat.say()