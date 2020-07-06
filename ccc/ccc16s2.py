case = int(input())
n = int(input())
x = input().split()
y = input().split()
x = [int(i) for i in x]
y = [int(i) for i in y]
if case == 1:
    x1 = sorted(x)
    y1 = sorted(y)
    s = 0
    for i in range(len(x)):
        s = s + int(max(x1[i], y1[i]))
    print(s)
if case == 2:
    x1 = sorted(x)
    y1 = sorted(y)
    s = 0
    y1.reverse()
    for i in range(len(x)):
        s = s + int(max(x1[i], y1[i]))
    print(s)
          