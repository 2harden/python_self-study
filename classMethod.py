# 类方法

class People:
    country='china'
    # l类方法，用classmethod修饰
    @classmethod
    def getCountry(cls):
        return cls.country
        pass
    @classmethod
    def changeCountry(cls, data):
        cls.country=data
        pass
    pass

    @staticmethod
    def getData():
        return People.country
        pass
    pass

print(People.getCountry())
people=People()
print(people.getCountry())
print('------------------changeCountry')
People.changeCountry('UK')
print(People.getCountry())
print('------------------getData')
print(People.getData())
people=People()
print(people.getData()) 
print('------------------showTime')

import time
class TimeTest:
    def __init__(self, hour, min, second):
       self.hour=hour
       self.min=min
       self.second=second

    @staticmethod
    def showTime():
        return time.strftime('%H:%M:%S', time.localtime())
        pass
    pass

print(TimeTest.showTime())
