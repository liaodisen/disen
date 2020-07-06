l1 = [1,2,3,4]
l2 = [0,0,0,0]
pm = [12, 13, 14, 23, 24, 34]
t = int(input())
g = int(input())
for i in range(g):
    result = input()
    l3 = result.split(" ")
    if int(l3[0:2]) in pm:
        pm.remove(int(l3[0:2]))
    if l3[2] == l3[3]:
        l2[int(l3[0])-1] += 1
        l2[int(l3[1])-1] += 1
    elif l3[2] > l3[3]:
        l2[int(l3[0])-1] += 3
    elif l3[2] < l3[3]:
        l2[int(l3[1]) -1] += 3
    
    