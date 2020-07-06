number = input()
ar = []
ro = []
total = 0
for i in range(0, len(number)):
    if i % 2 == 0:
        ar.append(int(number[i]))
    else:
        if number[i] == "I":
            ro.append(1)
        if number[i] == "V":
            ro.append(5)
        if number[i] == "X":
            ro.append(10)
        if number[i] == "L":
            ro.append(50)
        if number[i] == "C":
            ro.append(100)
        if number[i] == "D":
            ro.append(500)
        if number[i] == "M":
            ro.append(1000)
for x in range(1, int(len(number)/2)):
    if ro[x] > ro[x-1]:
        total = total - ar[x-1]*ro[x-1]
    else:
        total = total + ar[x-1]*ro[x-1]
total = total + ar[int(len(number)/2-1)]*ro[int(len(number)/2-1)]
print(total)
    