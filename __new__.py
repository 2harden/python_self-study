# 

class Aminal:
    def __init__(self):
        self.color='red'
        pass

    # 在py中,如果不重写__new__默认结构如下
    def __new__(cls, *args, **kwargs):
            return super().__new__(cls, *args, **kwargs)
            return object().__new__(cls, *args, **kwargs)
        pass

tigger=Aminal() # 实例化过程会自动取调用__new__去创建实例

'''
说明:

'''