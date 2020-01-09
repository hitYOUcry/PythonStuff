import threading
import sys
import time
import os
from collections import namedtuple
from multiprocessing import Process
import multiprocessing
multiprocessing.freeze_support()

Point = namedtuple('Point', ['x', 'y'])

class Phone(object):
    modelName = ""
    confirmPermissionPoint = Point(0, 0)

confirmPool = {}
p = Phone()
p.modelName = "mi"
p.confirmPermissionPoint = Point(980, 1820)
confirmPool[p.modelName] = p

def getConfirmPos(model):
    model = model.lower()
    for k in confirmPool:
        if k in model:
            return confirmPool[k]
    return "NotFound"

def exeCmd(cmd):
    print("BEGIN exe cmd[%s]" % (cmd))
    try:
        result = os.popen(cmd).read()
    except Exception as e:
        pass
    print("END exe cmd[%s], result[%s]" % (cmd, result))
    return result

print("args= %s" % sys.argv)
device = sys.argv[1]
targetPkg = sys.argv[2]
apkPath = sys.argv[3]
startComp = sys.argv[4]

phoneModel = exeCmd("adb -s %s shell getprop ro.product.model" % device)
phone = getConfirmPos(phoneModel)
print("phone=" + str(phone))
if "NotFound" == phone:
    print("Get confirmPos Error")

exeCmd("adb -s %s shell input keyevent 3" % (device))
exeCmd("adb -s %s uninstall %s" % (device, targetPkg))
exeCmd("adb -s %s install -r -t %s" % (device, apkPath))
time.sleep(2)
exeCmd("adb -s %s shell am start -n %s" % (device, startComp))
time.sleep(2)
exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.confirmPermissionPoint.x, phone.confirmPermissionPoint.y))
time.sleep(2)
exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.confirmPermissionPoint.x, phone.confirmPermissionPoint.y))
time.sleep(0.5)
