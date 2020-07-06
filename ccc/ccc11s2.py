line = int(input())
l = []
count = 0
for i in range(2*line):
    letter = input()
    l.append(letter)
for i in range(line):
    if l[i] == l[i+line]:
        count += 1
print(count)
    
    