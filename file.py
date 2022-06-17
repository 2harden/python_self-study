# 文件读写

# 写
# print('=================open file')
# f=open('./test.txt', 'w', encoding='utf-8') # 文件不存在，自动创建

# print('=================write file')
# f.write('i love python')
# f.write('i love c++')
# f.close()

# print('=================write with binary') # 二进制写
# f=open('./test.txt', 'wb')
# f.write('i love java\r'.encode('utf-8'))
# f.close()

# f=open('./test.txt', 'a') # 追加写
# f.write('i love javaScrip\r')
# f.close()

# f=open('./test.txt', 'ab') # 二进制形式追加写
# f.write('i love bat\r'.encode('utf-8'))
# f.close()

# 读
# f=open('./test.txt', 'r')
# print(f.read()) # 读取所有
# print(f.read(20)) # 读20个字符
# print(f.read())  # 继续读
# print(f.readline()) # 读一行
# print(f.readlines())  # 读所有行,列表形式返回
# f.close()

f=open('./test.txt', 'rb') # 以二进制读
print(f.read())
f.close()

# with 上写文管理，自动关闭打开的文件句柄
print('=================with')
def main():
    with open('./test.txt', 'r') as f:
        print(f.read())

main()