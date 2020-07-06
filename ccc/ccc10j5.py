seen = set()
grid = [[0]*8 for i in range(8)]
p1 = input().split()
p2 = input().split()
x1, y1 = int(p1[0]), int(p1[1])
x2, y2 = int(p2[0]), int(p2[1])
queue = []
queue.append((x1,y1,0))
seen.add((x1, y1))

while queue:
    x, y, path = queue.pop(0)
    if x == x2 and y == y2:
        print(path)
        break
    else:
        if x+1<9 and y+2<9:
            if (x+1,y+2) not in seen:
                queue.append((x+1, y+2, path+1))
                seen.add((x+1,y+2,path+1))
        if x+2<9 and y+1<9:
            if (x+2, y+1) not in seen:
                queue.append((x+2, y+1, path+1))
                seen.add((x+2, y+1, path+1))
        if x-1>0 and y+2<9:
            if (x-1, y+2) not in seen:
                queue.append((x-1, y+2, path+1))
                seen.add((x-1,y+2,path+1))
        if x-2>0 and y+1<9:
            if (x-2, y+1) not in seen:
                queue.append((x-2, y+1, path+1))
                seen.add((x-2,y+1,path+1))
        if x+2<9 and y-1>0:
            if (x+2, y-1) not in seen:
                queue.append((x+2, y-1, path+1))
                seen.add((x+2,y-1,path+1))
        if x+1<9 and y-2>0:
            if (x+1, y-2) not in seen:
                queue.append((x+1, y-2, path+1))
                seen.add((x+1,y-2,path+1))
        if x-1>0 and y-2>0:
            if (x-1, y-2) not in seen:
                queue.append((x-1, y-2, path+1))
                seen.add((x-1,y-2,path+1))
        if x-2>0 and y-1>0:
            if (x-2, y-1) not in seen:
                queue.append((x-2, y-1, path+1))
                seen.add((x-2,y-1,path+1))
        