n = int(input())
village = []
d = []
for i in range(n):
    v = int(input())
    village.append(v)
x = sorted(village)
for i in range(1, len(x)-1):
    dis = (x[i+1] - x[i-1])/2
    d.append(dis)
print(min(d))