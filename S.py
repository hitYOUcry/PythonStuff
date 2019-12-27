#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# print(r'\\\t\\')
# b = False
# c = True
# print(10*10)
# print(1.5e-6 * 1e100)

# print('''abv
# cgf\n
# kjie
# ''')


# print(10/3 * 3)
# print(10//3 * 3)
# print(ord('A'))
# print(ord('种'))
# print(chr(25991))



# print('%2d-%02d' % (3,1))
# print('%.2f%%-%02d' % (3,1))


# list = ['a','b','c']
# print(list[-1])
# list.append(3)
# print(list[-1])
# print(list.pop(3))

s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(s[2][1])
# print(s[1])
# print('python'[3])

# for name in s:
#     print(name)

# # s = 123*2636
# # if s % 2 == 0:
# #     print('s is even')
# # else:
# #     print('s is odd')

# s = {1,2,3}
# print(s)
# s.add(2)
# for name in s:
#     print(name)

# def isOdd(x):
#     if not isinstance(x, (int)):
#         raise TypeError('Bad type')
#     value = int(x)
#     if value % 2 == 0:
#         return False
#     else:
#         return True

# import math

# def quadratic(a, b, c):
#     if not isinstance(a, (int, float)):
#         raise TypeError('Bad type')
#     if not isinstance(b, (int, float)):
#         raise TypeError('Bad type')
#     if not isinstance(c, (int, float)):
#         raise TypeError('Bad type')

        
#     x1 = (-1 * b + math.sqrt(b * b - 4 * a * c )) / 2 / a
#     x2 = (-1 * b - math.sqrt(b * b - 4 * a * c )) / 2 / a
#     return x1, x2

# def mult(*numbers):
#     sum = 1
#     for num in numbers:
#         sum = sum * num
#     return sum

# print(mult(5, 6, 7, 9))

# a = "12543"
# # print(str(hex(a)))
# print(str(isOdd(a)))



# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])

# L = list(range(100))
# print(L[::10])


# def trim(s):
#     length = len(s)
#     i = 0
#     while(i < length and s[i] == ' '):
#         i = i + 1
#     j = length - 1
#     while(j >= 0 and s[j] == ' '):
#         j = j - 1
#     if( i >= j):
#         return ""
#     return s[i:(j + 1)]

# print(trim('hello ') == 'hello')
# print(trim(' hello ') == 'hello')
# print(trim(' hello') == 'hello')
# print(trim('  ') == '')
# print(trim('') == '')


# def findMinAndMax(L):
#     length = len(L)
#     if(length < 1):
#         return (None, None)
#     i = L[0]
#     j = L[0]
#     for value in L:
#         if(value > i):
#             i = value
#         if(value < j):
#             j = value
#     return (j, i)

# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


# L = [x + 10 for x in range(10)]

# for i, v in enumerate(L):
#     print("index:%d, value:%d" % (i, v))

# import os
# L = [d for d in os.listdir(".")]
# for i, v in enumerate(L):
#     print("index:%s, value:%s" % (i, v))

# def toLower(L):
#     return [x.lower() for x in L if isinstance(x, str)]

# L1 = ['Hello', 'World', 18, 'Apple', None]
# print(toLower(L1))

# g = (x*x for x in range(10))
# for n in g:
#     print(n)

# def triangles(n):
#     L = [1]
#     i = 0
#     while i < n:
#         yield L
#         oldLen = len(L)
#         newLen = len(L) + 1
#         N = list(range(newLen))
#         j = 0
#         while j < newLen:
#             if j - 1 < 0:
#                 N[j] = L[j]
#             elif j >= oldLen:
#                 N[j] = L[j - 1]
#             else:
#                 N[j] = L[j - 1] + L[j]
#             j = j + 1
#         i = i + 1
#         L = N
#     return 'done'

# g = triangles(10)
# for n in g:
#     print(n)
# from functools import reduce
# L = [1, 3, 5, 7, 9]

# def ff(x ,y):
#     return str(x) + str(y)

# g = map(str, L)
# print(list(g))
# print(int(reduce(ff,L)))

# def isPalindrome(n):
#     nStr = str(n)
#     nStr = nStr[::-1]
#     n_ = int(nStr)
#     return n == n_

# def gen_palindrome():
#     i = 1
#     while True:
#         yield i
#         i = i + 1
#         while(not isPalindrome(i)):
#             i = i + 1
#         if(i > 200):
#             break


# g = gen_palindrome()
# f = filter(isPalindrome, range(1,200))
# print(list(g))
# print(list(f))


# def nextNumberCreator():
#     def n_gen():
#         i = 0
#         while(True):
#             i = i + 1
#             yield i
#     g = n_gen()
#     def f():
#         return next(g)
#     return f
# nextNumber = nextNumberCreator()
# print(nextNumber(),nextNumber(),nextNumber(),nextNumber())

# odd = lambda n : n % 2 == 1
# L = list(filter(odd, range(1,10)))
# print(L)
        
# import time, functools

# def metric(func):
#     @functools.wraps(func)
#     def wrap(*args, **kw):
#         print("before %s %s" % (func.__name__, time.time()))
#         result = func(*args, **kw)
#         print("after %s %s" % (func.__name__, time.time()))
#         return result
#     return wrap


# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# fast(1,2)
# slow(1,2, 3)



