# 私有化方法

class Aminal:
    def __eat(self): # 私有化属性
        print('eat sth...')
        pass
    pass
    def run(self):
        self.__eat() # 类内部可以调用
        print('run sth...')
        pass
    pass

class Bird(Aminal):
    pass

bird=Bird()
# bird.eat() # 不能调用
bird.run()