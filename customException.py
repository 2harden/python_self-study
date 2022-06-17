# 自定义异常

class myException(Exception):
    def __init__(self, len):
        self.len=len
        pass

    def __str__(self):
        return 'Name your input length is' + str(self.len) + 'over the length'
        pass

def name_test():
    name=input('pls input name: ')
    try:
        if len(name) > 5:
            raise myException(len(name))
        else:
            print(name)
            pass
        pass
    except myException as msg:
        print(msg)
        pass
    finally:
        print('over...')