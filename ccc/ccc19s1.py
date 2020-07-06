n = input()
list0 = list(n)
h = int(list0.count("H"))
v = int(list0.count("V"))
if h % 2 == 0 and v % 2 == 0:
    print("1 2\n"
          "3 4")
if h % 2 != 0 and v % 2 == 0:
    print("3 4\n"
          "1 2")
if h % 2 == 0  and v % 2 != 0:
    print("2 1\n"
          "4 3")
if h % 2 != 0 and v % 2 != 0:
    print("4 3\n"
          "2 1")