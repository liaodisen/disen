times = int(input())
for i in range(times):
    x = input().split()
    num = int(x[0])
    code = x[1]
    l = []
    for j in range(num):
        l.append(code)
    print("".join(l))
        