r = input( "Wie oft soll das ding laufen: ")
r = int(r)
g = []
j = []
for x in range(r):

    import datetime

    endnumber = 10000

    start = datetime.datetime.now()

    for x in range(endnumber): print(x)

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
    g.append(delta)


print("Die finalen Werte für for gesammelt:")
for h in g:
    print(h)

for y in range(r):

    import datetime

    endnumber = 10000
    x = 0
    start2 = datetime.datetime.now()

    while x < endnumber:
        x = x + 1
        print(x)

    end2 = datetime.datetime.now()

    print("No console Output has been performed")
    print("Counted to: "+ str(endnumber))
    print("Started: "+ str(start2))
    print("Ended: "+ str(end2))
    delta2 = end2 - start2
    deltasec2 = delta.total_seconds()
    deltams2 = deltasec2 * 1000
    print("Time it took: " + str(deltams2)+ "ms")
    print("Time it took: " + str(delta2))
    j.append(delta2)


print("Die finalen Werte für for gesammelt:")
for h in g:
    print(h)
print("")
print("Die finalen Werte für while gesammelt:")
for k in j:
    print(k)