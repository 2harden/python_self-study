import os
import shutil

# 重命名
# os.rename('test.txt', 't.txt')

# 删除
# os.remove('test.txt.bak')

# 创建文件夹
# os.mkdir('zcshen')

# 删除文件夹
# os.rmdir('zcshen') # 只能删除空目录

#创建多级文件夹
# os.makedirs('d:\zcshen\df')

# 删除非空文件夹
# shutil.retree('d:/python/java/t.txt')

# 获取当前目录
print(os.getcwd())

# 路径拼接
# print(os.path.join(os.getcwd()), 'venv')

# 获取目录列表
# listRs=os.listdir('d:/')  # 老版
# for dirname in listRs:
#     print(dirname)

# with os.scandir('d:/') as entries: # 现代版写法
#     for entry in entries:
#         print(entry.name)

# 打印指定目录所有文件
basePath='D:\Study\python_self-study'
for entry in os.listdir(basePath):
    if os.path.isfile(os.path.join(basePath, entry)):
        print(entry)