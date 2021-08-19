ipv4192 = []
ipv4172 = []
ipv410 = []

for x in range(256):
    for y in range(256):
        temparray = ['192', '168']
        temparray.append(str(x))
        temparray.append(str(y))
        temparray = ".".join(temparray)
        ipv4192.append(temparray)
for x in range(16,32):
    for y in range(256):
        for z in range(256):
            temparray = ['172']
            temparray.append(str(x))
            temparray.append(str(y))
            temparray.append(str(z))
            temparray = ".".join(temparray)
            ipv4172.append(temparray)
for x in range(256):
    for y in range(256):
        for z in range(256):
            temparray = ['10']
            temparray.append(str(x))
            temparray.append(str(y))
            temparray.append(str(z))
            temparray = ".".join(temparray)
            ipv410.append(temparray)