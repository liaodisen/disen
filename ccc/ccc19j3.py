n = int(input())
for i in range(n):
    l = input()
    for x in range(len(l)):
        symbol = l[x]
    newl = {}
    for symbol in l:
        print(symbol)
        if symbol not in newl:
            newl[symbol] = 1
        else:
            newl[symbol] = newl[symbol] + 1
    pl = []
    for keys, values in newl.items():
        pl.append(str(values))
        pl.append(keys)
    print(" ".join(pl))
        
            
