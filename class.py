# 定义类和对象
# 类结构 （类名、属性、方法）

class Person:
    # 对应人的特质
    name='ming' # 类属性
    age=11 # 类属性


    def __init__(self):
        self.name='hua' # 实例属性
    
    # 人的行为
    def eat(self): # 实例方法，self可以随便换名字
        print('eat')
        pass

    def run(self): # 实例方法，self可以随便换名字
        print('run')
        pass

# 创建对象(类的实例化)
p=Person()
p.eat() # 调用函数
p.run()
print("{} age is : {}".format(p.name,p.age))