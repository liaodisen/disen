import math
def prime(x):
    state = True
    if x % 2 == 0:
        state = False
        return state
    else:
        for a in range(2, int(math.sqrt(x)+1)):
            if x % a == 0:
                state = False
        return state


n = int(input())
for i in range(n):
    t = int(input())
    for a in range(2, 2*t+1):
        if prime(a)==True and prime(2*t - a)==True:
            break
    print(str(a) + " " + str(2*t - a))