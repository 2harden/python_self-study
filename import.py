# 模块导入

# 方式一
# import time
# print(time.ctime())

# 方式二
from time import ctime, time
print(ctime()) # 不需要加模块名了，也可以加

# as给模块取别名
import time as myTime
print(myTime.ctime())

