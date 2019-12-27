from datetime import datetime, timedelta, timezone
import re


timeStr = '2015-6-1 08:10:30'
timeZone = 'UTC+7:01'

p = re.compile('(UTC)(\+|\-)([0-9]|1[0-1]):([0-5][0-9])')

g = p.match(timeZone)


factor = 1
if g.group(2) == "-":
    factor = -1    

hour = factor * int(g.group(3))
minute = factor * int(g.group(4))
print("factor(%d), hour(%d), minute(%d)" % (factor, hour, minute))
tz = timezone(timedelta(hours = hour, minutes= minute))
print(tz)
time = datetime.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
timeUtc = time.replace(tzinfo=tz)

print(timeUtc.timestamp())




