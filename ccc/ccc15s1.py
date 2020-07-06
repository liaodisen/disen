n = int(input())
k = 0
l = []
for i in range(n):
    m = int(input())
    if m != 0:
        l.append(m)
    else:
        l.pop()
sum(l)