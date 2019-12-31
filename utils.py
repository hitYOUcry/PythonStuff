# from datetime import datetime, timedelta, timezone
# import re


# timeStr = '2015-6-1 08:10:30'
# timeZone = 'UTC+7:01'

# p = re.compile('(UTC)(\+|\-)([0-9]|1[0-1]):([0-5][0-9])')

# g = p.match(timeZone)


# factor = 1
# if g.group(2) == "-":
#     factor = -1

# hour = factor * int(g.group(3))
# minute = factor * int(g.group(4))
# print("factor(%d), hour(%d), minute(%d)" % (factor, hour, minute))
# tz = timezone(timedelta(hours = hour, minutes= minute))
# print(tz)
# time = datetime.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
# timeUtc = time.replace(tzinfo=tz)

# print(timeUtc.timestamp())


# from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter

# Point = namedtuple('Ponit', ['x', 'y'])
# p = Point(1, "3")
# print("p.x is %s, p.y is %s" % (p.x, p.y))


# import base64

# import struct

# import itertools

# def pi(N):
#     g = itertools.count(1)
#     A = itertools.takewhile(lambda x: x <= N, g)
#     g = itertools.count(1)
#     B = [2*x-1 for x in itertools.takewhile(lambda x: x <= N, g)]
#     sum = 0
#     for a,b in zip(A, B):
#         delta = 1 / b
#         if a % 2 == 0:
#             delta = -1 * delta
#         sum = sum + delta
#     return 4 * sum

# def PIA(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     oddnumber=itertools.count(1,2)
#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     result=itertools.takewhile(lambda x:x<=2*N-1,oddnumber)
#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     s=[(-1)**key*4/value for key,value in enumerate(list(result))]
#     # step 4: 求和:
#     return sum(s)

# print(pi(10))
# print(pi(100))
# print(pi(1000))
# print(pi(10000))
# assert 3.04 < pi(10) < 3.05
# assert 3.13 < pi(100) < 3.14
# assert 3.140 < pi(1000) < 3.141
# assert pi(10000) == PIA(10000)
# print('ok')


# from urllib import request
# import chardet
# import gzip
# from io import BytesIO

# req = request.Request('http://www.qq.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     f_data = BytesIO(data)
#     f = gzip.GzipFile(mode = 'rb', fileobj = f_data)
#     try:
#         plain_data = f.read()
#     finally:
#         f.close()
#     print(chardet.detect(plain_data))
#     print('Data:', plain_data.decode('gbk'))

# from html.parser import HTMLParser
# from html.entities import name2codepoint
# import re


# class MyHTMLParser(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.__parsedata = ""
#         self.info = []

#     def handle_starttag(self, tag, attrs):
#         if ('class', 'event-title') in attrs:
#             self.__parsedata = "title"
#         elif tag == "time":
#             self.__parsedata = "time"
#         elif ('class', 'say-no-more') in attrs:
#             self.__parsedata = "year"
#         elif ('class', 'event-location') in attrs:
#             self.__parsedata = "location"
#         if(self.__parsedata != ""):
#             print("handle_starttag __parsedata = %s" % self.__parsedata)

#     def handle_endtag(self, tag):
#         self.__parsedata = ""

#     def handle_startendtag(self, tag, attrs):
#         pass

#     def handle_data(self, data):
#         if(self.__parsedata != ""):
#             print("handle_data __parsedata = %s, data:%s" % (self.__parsedata, data))
#         if self.__parsedata == "title":
#             self.info.append("会议名称:%s" % data)
#         elif self.__parsedata == "time":
#             self.info.append("会议时间:%s" % data)
#         elif self.__parsedata == "year":
#             p = re.compile(r'\d{4}')
#             if p.match(data):
#                 self.info.append("会议年份:%s" % data)
#         elif self.__parsedata == "location":
#             self.info.append("会议地点:%s" % data)

#     def handle_comment(self, data):
#         pass

#     def handle_entityref(self, name):
#         pass

#     def handle_charref(self, name):
#         pass


# parser = MyHTMLParser()


# with open('test.html', 'r') as f:
#     for line in f.readlines():
#         parser.feed(line)

# print(parser.info)
