# 理解self (self就是实例对象本身)
class Person:
    def eat(self):
        print(self)
        print('self address is: ', id(self))
    pass

p=Person()
print('p address is: ', id(p))
p.eat()