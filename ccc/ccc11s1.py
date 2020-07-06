lines = int(input())
numbert = 0
numbers = 0
for i in range(lines):
    cont = input()
    contl = cont.lower()
    numbert += contl.count("t")
    numbers += contl.count("s")
if numbert > numbers:
    print("English")
else:
    print("French")
    