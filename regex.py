# 正则表达式

# import re
# str = 'python'

# res = re.match('p', str)
# if res:
#     print(res)
#     print(res.group())
#     print('sucess...')
# else:
#     print(res.group()) # 匹配失败，没有group，因为对象是None
#     print('fail...')

print('=========================group')
import re
str = 'python is the best language in the world'

res = re.match('(.*) is (.*?) .*', str, re.I|re.M)
if res:
    print(res)
    print(res.group()) # 返回所有
    print(res.groups()) # 按照元组返回
    print(res.group(1)) # group(num)可以获取匹配的数据，如果有多个匹配结果的话，会以元组的形式存放到group对象中，可以通过下标获取
    print(res.group(2))
    print('sucess...')
else:
    print(res.group()) # 匹配失败，没有group，因为对象是None
    print('fail...')

print('=========================.') # 匹配换行符之外的字符
import re
str = 'aaaa'

res = re.match('..', str) # 一个点匹配一个字符
print(res.group())

print('=========================[]') # 匹配中括号中的任意一个字符
import re
str = 'hello'

res = re.match('[he]', str) # 
print(res.group())

print('=========================\d') # 匹配一个数字0-9
import re
str = '53243df'

res = re.match('\d\d', str) # 一个/d代表一位
print(res.group())

print('=========================\D') # 匹配非数组
import re
str = 's53243df'

res = re.match('\D', str) # 一个\D代表一位
print(res.group())

print('=========================\s') # 匹配空白，空格或者tab键
import re
str = ' '

res = re.match('\s', str) # 一个\s代表一位
print(res.group())

print('=========================\S') # 匹配非空白
import re
str = 'p p'

res = re.match('\S', str) # 一个\S代表一位
print(res.group())

print('=========================\w') # 匹配单词a-z,A-Z,0-9,_
import re
str = 'p2p'

res = re.match('\w\w\w', str) # 一个\w代表一位
print(res.group())

print('=========================\w') # 匹配非单词
import re
str = '     p2p'

res = re.match('\W', str) # 一个\W代表一位
print(res.group())

print('=========================*') # 匹配前一个字符出现0次或者无限次，即可有可无
import re
str = 'My'
str1 = 'Any'

res = re.match('[A-Z][a-z]*', str1) # 一个[A-Z]代表一位
print(res.group())

print('=========================+') # 匹配前一个字符出现1次或者无限次，即至少1次
import re
str = 'My'
str1 = 'MYnameis'

res = re.match('[A-Z]+', str1) # 一个[A-Z]代表一位
print(res.group())

print('=========================\?') # 匹配前一个字符出现0次或者1次，即要么1次，要么没有
import re
str = 'My'
str1 = 'n3a99M_e'

res = re.match('[a-zA-Z][0-9]?', str1) # 一个[A-Z]代表一位
print(res.group())

# {min, max} min. max都是非负整数
print('========================={m}') # 匹配前一个字符出现m次
import re
str = 'My'
str1 = '1233'

res = re.match('\d{4}', str1)
print(res.group())

print('========================={m,}') # 匹配前一个字符至少出现m次
import re
str = 'My'
str1 = '12334444444534444444'

res = re.match('\d{4,}', str1)
print(res.group())

print('========================={n,m}') # 匹配前一个字符出现从n到m次
import re
str = 'My'
str1 = '12334444444534444444'

res = re.match('\d{4,8}', str1)
print(res.group())

print('=========================match mail') # 匹配邮箱
import re
str = 'My'
str1 = '1233444@163.com'

res = re.match('[a-zA-Z0-9]{6,11}@163.com', str1)
print(res.group())

print('=========================^') # 匹配字符串开头
import re
str = 'My'
str1 = 'Python is a language'

res = re.match('^P.*', str1)
print(res.group())
res = re.match('^P\w{5}', str1)
print(res.group())

print('=========================$') # 匹配字符串结尾
import re
str = 'My'
str1 = 'accountttt@qq.com'

res = re.match('[\w]{5,15}@[\w]{2,3}.com$', str1)
print(res.group())

#======================分组匹配
print('========================= |') # 匹配左右任意一个表达式，实际上是 或 的关系
import re
str1 = 'accountttt@qq.com333333'

res = re.match('(accountttt@qq.com|accountttt@qq.com333333)', str1)
print(res.group())

print('========================= (ab)') # 将括号中的字符作为一个分组
# 匹配电话号码 XXXX-123456789
# ^有两种含义，1：以XXXX开头 2：否定，取反
import re
str1 = '0355-123456789'

res = re.match('([0-9]*)-(\d*)', str1)
print(res.group())
print(res.group(1)) # 打印第一组的数据
print(res.group(2))

print('========================= \\num') # 引用分组num匹配到的字符串
import re
str1 = '<html><h1>test</h1></html>'

res = re.match(r'<(.+)><(.+)>(.+)</\2></\1>', str1)
print(res.group())
print(res.group(1)) # 打印第一组的数据
print(res.group(2))
print(res.group(3))

# 分组起别名
# 其别名 (?P)
# 引用别名(?P=name)
print('========================= (?P)') # 引用分组num匹配到的字符串
import re
str1 = '<div><h1>www.baidu.com</h1></div>'

res = re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>', str1) # r代表转义
print(res.group())
print(res.group(1)) # 打印第一组的数据
print(res.group(2))

print('========================= re.compile()') # re模块中的编译方法，可以把一个字符串编译成字节码
# 优点：在使用正则表达式进行match操作时，python会将字符串转为正则表达式对象，而如果使用complie则只需要完成一次转换即可，以后再使用模式对象的话，无需重复转换
import re

reobj=re.compile('\d{4}')
# 开始使用reobj对象
res = reobj.match('1234')
print(res.group())

print('========================= re.search()') # 在全文中匹配一次，匹配到就返回
import re

str1 = 'A is a great country'
res = re.search('country', str1)
print(res.group())

print('========================= re.findall()') # 匹配所有返回一个列表（符合正则表达式的结果列表），使用频率较高
import re

str1 = 'all roads lead to room'
res = re.findall('all.', str1)
print(res)

print('========================= re.sub()') # 将匹配到的数据进行替换
import re

str1 = 'hello world'
res = re.sub('h', 'H', str1)
resn = re.subn('h', 'H', str1) # sunb返回替换的数量
print(res)
print(resn)

print('========================= re.split()') # 实现分割字符串
import re

str1 = 'all, roads, lead, to, room'
res = re.split(',', str1)
print(res)

# 贪婪模式，非贪婪模式
print('========================= *?,+?,??,{m,n}?') # 非贪婪模式，匹配尽可能少
import re

# 贪婪模式，匹配尽可能多
str1 = '111222333'
res = re.match('\d{6,9}', str1)
print(res.group())

# 非贪婪模式，匹配尽可能少
str1 = '111222333'
res = re.match('\d{6,9}?', str1)
print(res.group())