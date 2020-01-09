import sys
import time
import os
from collections import namedtuple
from multiprocessing import Process
import multiprocessing
multiprocessing.freeze_support()
import threading

Point = namedtuple('Point', ['x', 'y'])

class Phone(object):
    modelName = ""
    confirmPermissionPoint = Point(0, 0)
    installConfirmPoint = Point(0, 0)
    confirmPwd = Point(0, 0)
    installPassword = "lvlf1314"

    def __str__(self):
        return "modelName:%s confirmPermissionPoint:%s installConfirmPoint:%s installPassword:%s" % (self.modelName, self.confirmPermissionPoint, self.installConfirmPoint, self.installPassword)

confirmPool = {}
p = Phone()
p.modelName = "vivo"
p.installConfirmPoint = Point(540, 1680)
p.confirmPermissionPoint = Point(318, 1280)
p.confirmPwd = Point(351, 877)
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

t = threading.Thread(target=exeCmd, args=["adb -s %s install -r -t %s" % (device, apkPath),])
t.start()
# p = Process(target=exeCmd, args=["adb -s %s install -r -t %s" % (device, apkPath),])
# p.start()
time.sleep(4)
exeCmd("adb -s %s shell input text %s " %
       (device, phone.installPassword))

exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.confirmPwd.x, phone.confirmPwd.y))
time.sleep(4)
exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.installConfirmPoint.x, phone.installConfirmPoint.y))
time.sleep(2)
exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.installConfirmPoint.x, phone.installConfirmPoint.y))


time.sleep(2)
exeCmd("adb -s %s shell am start -n %s" % (device, startComp))
time.sleep(2)

exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.confirmPermissionPoint.x, phone.confirmPermissionPoint.y))
time.sleep(2)

exeCmd("adb -s %s shell input tap %s %s" %
       (device, phone.confirmPermissionPoint.x, phone.confirmPermissionPoint.y))
time.sleep(0.5)
