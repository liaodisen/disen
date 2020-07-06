p = input()
l1 = input()
l2 = input()
first = l1.split()
second = l2.split()
state = "good"
i = 0
while i < n and state == "good":
    position = first.index(second[i])
    if first[i] != second[position] or position == i:
        state = "bad"
    i = i + 1
    
print state
    