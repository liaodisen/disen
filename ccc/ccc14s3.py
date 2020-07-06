def case1test(list0):
    test = False
    list0.remove(1)
    if list0 == sorted(list0):
        test = True
    return test
def case2test(list0):
    test = False
    n = 0
    if list0[0] > list0[1]:
        while n + 1 < len(list0) -1 and list0[n] > list0[n + 1]:
            n += 1
        sub2 = list0[n+1:]
        sub0 = list0[0:n+1]
        if sub2 == sorted(sub2) or n == len(list0) -2:
            test = True
    return test
test = int(input())
l1 = []
n1 = int(input())
while True:
    try:
        for t in range(test):
            for i in range(n1):
                x = int(input())
                l1.append(x)
            if case1test(l1) or case2test(l1) == True:
                print("Y")
            else:
                print("N")
            n1 = int(input())
            l1 = []
    except EOFError:
        break