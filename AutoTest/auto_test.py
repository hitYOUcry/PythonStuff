import os
import time
import re
import threading
from multiprocessing import Process

targetPkg = "com.growth.gamebox"
apkPath = "C:\\Code\\GameBox\\app\\build\\outputs\\apk\\debug\\app-debug.apk"
startComp = "com.growth.gamebox/com.growth.gamebox.splash.SplashActivity"

scriptPool = {"mi": "pipeline_mi.py", "vivo": "pipeline_vivo.py"}


def exeCmd(cmd):
    result = os.popen(cmd).read()
    print("exe cmd[%s], result[%s]" % (cmd, result))
    return result


def getScriptName(model):
    model = model.lower()
    for k in scriptPool:
        if k in model:
            return scriptPool[k]


# exeCmd("adb shell input keyevent 3")
result = exeCmd("adb devices")
p = re.compile(r"([\w\d]+)\s+device")
devices = []
for line in result.splitlines():
    matchResult = p.match(line)
    if matchResult == None:
        continue
    devices.append(matchResult.group(1))
print("devices: %s" % devices)


if __name__ == "__main__":
    for device in devices:
        phoneModel = exeCmd("adb -s %s shell getprop ro.product.model" % device)
        script = getScriptName(phoneModel)
        if script == None:
            print("Can't found script for %s which model is %s" %
                (device, phoneModel))
            continue
        cmd = "python %s %s %s %s %s" % (
            script, device, targetPkg, apkPath, startComp)
        # t = threading.Thread(target=exeCmd, args=[cmd, ])
        t = Process(target=exeCmd, args=[cmd, ])
        t.start()

