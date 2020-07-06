def rotate(l):
    newl = [[] for i in range(len(l[0]))]
    for i in range(len(l)):
        for j in range(len(l[0])-1, -1, -1):
            newl[len(l[0]) -1 - j].append(l[i][j])
    return newl
    
n = int(input())
rows = []
for i in range(n):
    x = input().split()
    rows.append(x)

k = 1
while k == 1:
    rows = rotate(rows)
    if int(rows[0][0]) < int(rows[0][1]) and int(rows[0][0]) < int(rows[1][0]):
        k = 0
for i in range(len(rows)):  
    print(" ".join(rows[i]))
class Test(object):
    pass