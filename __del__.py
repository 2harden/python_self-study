# 析构方法
class Animal:
    def __init__(self,name): # 自动调用
        print("__init__ is called")
    pass
    def __del__(self): # 自动调用
        print("__del__ is called")
    pass

cat=Animal('cat')
# input('input sth...')

# 删除对象的时候也会自动调用__del__()
del cat
print(cat.name) # 被删除，无法打印