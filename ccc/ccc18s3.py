
def val(x, i, j):
    if x[i-1][j] == "W" and x[i+1][j] == "W" and x[i][j+1] == "W" and x[i][j-1] == "W":
        return -1
    pl = []
    if x[i][j-1] == ".": #left
        pl.append(val(x, i, j))
    if x[i+1][j] == ".": #up
        pl.append(val(x, i, j))
    if x[i][j+1] == ".":
        pl.append(val(x, i, j))
    if x[i-1][j] == ".":
        pl.append(val(x, i, j))
    return min(pl)+1
    memo[i][j] = min(pl) + 1
    if x[i][j] == "S":
        return 0

    

n = input()
nrow = int(n[0])
ncol = int(n[2])
grid = []
for i in range(nrow):
    row = list(input())
    grid.append(row)    
for p in range(nrow):
    for q in range(ncol):
        if grid[p][q] == ".":
            print(val(grid, p, q))
            grid[p][q] = val(grid, p, q)

            
        
    
