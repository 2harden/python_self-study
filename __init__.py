class People:
    # def __init__(self):
    #     '''
    #         实列属性的声明
    #     '''
    #     self.name='peter'
    #     self.set='mile'
    #     self.age=23
    #     pass
    def __init__(self,name,sex,age):
        '''
            实列属性的声明
        '''
        self.name=name
        self.sex=sex
        self.age=age
        pass
    def eat(self):
        '''
            吃的行为
        '''
        print('like eat apple')
        pass


# p=People()
# p.name='df'
# p.set='mile'
# p.age=32
# print(p.name,p.set,p.age)
# p.eat()

# x=People()
# x.name='ld'
# x.set='mile'
# x.age=32
# print(x.name,x.set,x.age)

# print('===============call __init__ func')
# y=People() # 会自动调用__init__方法
# print(y.name,y.set,y.a ge)

print('===============call __init__ parameterized initialization func')
z=People('szc','mile',33) # 会自动调用有参__init__方法
print(z.name,z.sex,z.age)