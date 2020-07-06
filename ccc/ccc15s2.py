a = int(input())
b = int(input())
js = []
count = 0
for i in range(a):
    size = input()
    js.append(size)
for k in range(b):
    w = input()
    si = w[0]
    num = int(w[2])-1
    if js[num] != 'T':
        if si == 'S' or \
            si == js[num] or \
               (si == 'M' and js[num] == 'L'):
            count = count + 1
            js[num] = 'T'

print(count)