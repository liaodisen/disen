rules = [["A", "C"], ["B", "D"]]




def move(a1, a2, rules):
    for rule in rules:
        for i in range(len(a1) - len(rule)):
            if a1[i:i+len(rule)] == rule[0]:
                a1 = a1.replace(rule[0], rule[1])
                if a1 == a2:
                    return "a"
                else:
                    continue
a1 = "ABBA"
a2 = "ABDA"
print(move(a1, a2, rules))        
    
        