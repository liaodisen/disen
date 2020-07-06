import math

# returns a list of factors of x
def factors(x):
    f = [1, x]
    r = int(math.sqrt(x)) + 1
    for i in range (2,r):
        if x % i == 0:
            f.append(i)
            f.append(x / i)
    return f


N = int(input())
    
# m is a list of max values for each number
m = []
for i in range(N+1):
    m.append(9999999999)

m[1] = 0
for i in range(1, N+1):
    f = factors(i)
    for x in f:
        h = i + x
        cost = m[i] + (i / x)
        if h <= N and cost < m[int(h)]:
            m[int(h)] = cost
    
print(int(m[int(N)]))