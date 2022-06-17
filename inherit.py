# # 单继承
# class Animal:
#     def eat(self):
#         print("eat...")
#     pass

#     def drink(self):
#         print("drink...")
#     pass

# class Dog(Animal):
#     def wwj(self):
#         print("dog wwj...")
#     pass
# class cat(Animal):
#     def mmj(self):
#         print("cat wwj...")
#     pass

# d=Dog()
# d.eat()
# d.wwj()

# c=cat()
# c.eat()
# c.mmj()

# 多继承
class A:
    def fly(self):
        print('a can fly')
    pass

class B:
    def swim(self):
        print('b can swim')
    pass

class C(A, B):
    pass

d=C()
d.fly()
d.swim()