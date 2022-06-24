# python 垃圾回收

import sys
import psutil
import os
import gc


# 引用计数
# sys.getrefcount()
a=[]
print(sys.getrefcount(a)) # 此处引用次数为2
b=a
print(sys.getrefcount(a)) # 此处引用次数为3
c=b
d=b
e=c
f=e
print(sys.getrefcount(a)) # 此处引用次数为7

def showMemsize():
    pid=os.getpid()
    p=psutil.Process(pid)
    info=p.memory_full_info()
    memory=info.uss/1024/1024
    print('{} memory used: {} MB'.format(tag, memory))
    pass

# 验证循环引用的情况
def func():
    showMemsize('init...')
    a=[i for i in range(1000000)]
    b=[i for i in range(1000000)]
    a.append(b)
    b.append(a) //相互引用，结束不会释放内存
    showMemsize('创建列表对象a,b之后')
    print(sys.getrefcount(a)) # 3
    print(sys.getrefcount(b)) # 3
    # del a 
    # del b # 删除对象不会起作用
    pass

func() # 调用
gc.collect() # 手动释放，会清除循环引用占用的内存
showMemsize('完成的时候')