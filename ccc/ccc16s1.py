l1 = input()
l2 = input()
state = True
a = list(l1)
b = list(l2)
n = b.count("*")
for i in range(n):
    b.remove("*")
for i in range(len(b)):
    if b[i] not in a:
        state = False
if state == True:
    print("A")
elif state == False:
    print("N")