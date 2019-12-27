class Student():
    name = "name"
    def __init__(self, number):
        self.__number = number
    
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value
    
    def __str__(self):
        return "stu number(%d)" % self.number

s = Student(25)
s.number = 14

print(s)

from enum import Enum, unique

@unique
class STATE(Enum):
    INIT = 0
    DOWNLOADING = 1
    DOWNLOADED = 2
    FAILED = 3

print(STATE['FAILED'])
print(STATE(1))
print(STATE.INIT)

s = Student(12)
b = Student(1212)

print(s.name)
Student.name = "another name"
print(b.name)

try:
    print(10 /0)
except ZeroDivisionError as e:
    print("exception:", e)
finally:
    print("finally")
print("END")





