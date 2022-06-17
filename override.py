# 重写
class GrandFather:
    def eat(self):
            print("GrandFather eat...")
    pass
    


class Father:
    def eat(self): # 重写GrandFather的eat方法
            print("Father eat...")
    pass
    

class Son(Father):

    pass

son=Son()
son.eat()