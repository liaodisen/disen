n = int(input())
t1 = input().split()
t2 = input().split()
k1 = 0
k2 = 0
k = 0
for i in range(n):
    k1 = k1 + int(t1[i])
    k2 = k2 + int(t2[i])
    if k1 == k2:
        k = i + 1
print(k)