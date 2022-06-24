# 模块制作

__all__=['add', 'diff'] # __all__魔术变量的作用，如在一个文件中存在__all__变量，意味着这个变量中的元素在from XXX inport * 时会被导入，__all__中没有声明的元素，不会被导入。对于import方式无所谓，全被都可以被导入

def add(x, y):
    return x + y

# 测试模块
if __name__=='__main__':
    res=add(3, 5)
    print(res)

print('module __name__: %s' %__name__)