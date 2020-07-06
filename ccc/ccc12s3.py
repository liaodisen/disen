sen = int(input())
l = [0]*1000
rl = [0]*1000
for i in range(sen):
    ph = int(input())
    l[ph-1] = l[ph-1] + 1
    rl[1000-ph] = rl[1000-ph] + 1
firstmin = l.index(max(l)) + 1
firstmax = -1 * rl.index(max(l)) + 1000
l[l.index(max(l))] = 0
rl[l.index(max(l))] = 0
secondmin = l.index(max(l))+1
secondmax = -1 * rl.index(max(l)) + 1000

p1 = abs(firstmax - secondmin)
p2 = abs(firstmin - secondmax)
print(max(p1,p2))
    

