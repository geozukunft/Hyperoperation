import datetime
import time 



x = 0
endnumber = 1000000000

start = datetime.datetime.now()

while x < endnumber:
    x = x + 1

end = datetime.datetime.now()

print("No console Output has been performed")
print("Counted to: "+ str(endnumber))
print("Started: "+ str(start))
print("Ended: "+ str(end))
delta = end - start
deltasec = delta.total_seconds()
deltams = deltasec * 1000
print("Time it took: " + str(deltams)+ "ms")
print("Time it took: " + str(delta))
