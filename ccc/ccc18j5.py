pages = int(input())
choices = []
way = {}
for k in range(pages):
    choice = input().split()
    choices.append(choice)
for i in range(pages):
    way[i+1] = choices[i][1:]
    
seen = set()
queue =[]
queue.append(("1", 1))
minpath = []
while queue:
    n, path = queue.pop(0)
    seen.add(n)
    next_page = way[int(n)]
    if next_page == []:
        minpath.append(path)
    else:
        for w in next_page:
            if w not in seen:
                queue.append((w, path+1))
                seen.add(w)

if len(seen) == pages:
    print("Y")
    print(min(minpath))
else:
    print("N")
    print(min(minpath))

    