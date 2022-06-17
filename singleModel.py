# 单例模式

# 创建一个单例对象 基于__new__实现(推荐)
class DataBase(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'): # 如果不存在,开始创建
            cls._instance=super().__new__(cls, *args, **kwargs)
        return cls._instance
    pass

dataBase1=DataBase()
print(id(dataBase1))

dataBase2=DataBase()
print(id(dataBase2))