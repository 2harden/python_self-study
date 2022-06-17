# 文件定位 返回指针当前所在的位置

# with open('test.txt', 'r') as f:
#     print(f.read(3))
#     print(f.tell()) # 返回指针当前所在的位置
#     print(f.read(4))
#     print(f.tell())

f=open('test.txt', 'r')
print(f.read())
f.close

# 截取之后的数据
print('==================truncate()')
f=open('test.txt', 'r+')
f.truncate(15) # 对源文件进行截取操作，保留前15个字符
print(f.read())
f.close

print('==================seek()')
with open('test.txt', 'r') as f: # 如果用’r‘方式打开文件，在文本文件中，没有使用二进制的选项打开文件，只允许从文件的开头计算相对位置。从文件尾部计算获知当前计算的话，就会引发异常。一般使用二进制打开文件
    print(f.read())
    f.seek(1, 0) # 光标设置到了0的位置，向右移动1个字符
    print(f.read(2))