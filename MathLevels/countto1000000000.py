import datetime
import time 

start = datetime.datetime.now()
startstr = str(start)
x = 1
while x < 10:
    x = x + 1
    print(x)
    time.sleep(1)
end = datetime.datetime.now()
endstr = str(end)
print("Started: "+ startstr)
print("Ended: "+ endstr)
    

