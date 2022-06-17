# 文件备份

def copyFile():
    # 接受用户输入的文件名
    old_flie=input('input file which need bakup: ')
    file_list=old_flie.split('.')
    # 构造新的文件名，.加上备份的后缀
    new_file=file_list[0] + '.' + file_list[1] + '.bak'
    old_f=open(old_flie, 'r') # 读方式打开需要备份的文件
    new_f=open(new_file, 'w') # 写方式打开新文件，不存在则创建
    content=old_f.read()
    new_f.write(content)
    old_f.close()
    new_f.close()
    pass

copyFile()

def copyBigFile():
    # 接受用户输入的文件名
    old_flie=input('input file which need bakup: ')
    file_list=old_flie.split('.')
    # 构造新的文件名，.加上备份的后缀
    new_file=file_list[0] + '.' + file_list[1] + '.bak'
    try:
        with open(old_flie, 'r') as old_f, open(new_flie, 'w') as new_f:
            while True:
                content=old_f.read(1024) # 一次读取1024字符
                new_f.write(content)
                if len(content) < 1024:
                    break
    except Exception as msg:
        print(msg)                
    pass

copyBigFile()