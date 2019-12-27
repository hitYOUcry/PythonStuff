# with open('module.py', 'r') as file:
#     for line in file.readlines():
#         print(line)

import os
# print(os.name)
# print(os.environ.get("PATH"))


def findStr(dirPath, targetStr):
    L = os.listdir(dirPath)
    for file in L:
        if targetStr in file:
                print(os.path.abspath(file))
        if os.path.isdir(file):
            findStr(os.path.abspath(file), targetStr)


findStr(os.path.abspath("."), "obj")