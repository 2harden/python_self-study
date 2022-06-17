# 异常处理

try:
    # print(b) # 要捕获的代码
    li[1,2,34]
    print(li[10])
    pass
# except NameError as msg:
#     print(msg) # 捕获到的错误，才会在这里执行
#     pass

# except IndexError as msg:
#     print(msg) # 捕获到的错误，才会在这里执行
#     pass

except Exception as result: # 可以捕获所有异常，当对于出现的问题或者错误不确定的时候，可以用exception
    print(result) # 捕获到的错误，才会在这里执行
    pass


print('hahahaha...')

print('=================try-except-else')

try:
    print(a)
    pass
except Exception as msg:
    print(msg)
else:
    print('b...') # 当try里面的代码，没有出现异常的情况下，才执行else里面的代码
    pass
    
print('=================try-except-finally')
try:
    print(a)
    pass
except Exception as msg:
    print(msg)
finally:
    print('c...') # 不管有没有错误都会执行的代码