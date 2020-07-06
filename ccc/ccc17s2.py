
n = int(input())
x = input().split()
small = []
big = []
new = []
x = map(int, x)
a = sorted(x)
if n % 2 == 0:
    for i in range(int(n/2)):
        small.append(a[i])
    for i in range(int(n/2), int(n)):
        big.append(a[i])
    for j in range(len(small)-1, -1, -1):
        new.append(small[j])
        new.append(big[len(small) - 1 - j])
    strnew = [str(x) for x in new]
    print(" ".join(strnew))
else:
    for i in range(int(n/2)+1):
        small.append(a[i])
    for i in range(int(n/2)+1, int(n)):
        big.append(a[i])
    for j in range(len(small)-1, 0, -1):
        new.append(small[j])
        new.append(big[len(small) -1 - j])
    new.append(small[0])
    strnew = [str(x) for x in new]
    print(" ".join(strnew))
        


    