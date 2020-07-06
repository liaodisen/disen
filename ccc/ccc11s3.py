testcase = int(input())
for i in range(testcase):
    line = input()
    space = line.find(" ")
    m = int(line[0:space])
    line = line[space+1:]
    space = line.find(" ")
    x = int(line[0:space])
    y = int(line[space+1:])
    a = 1
    if m == 1:
        if y == 0:
            if x == 1 or x == 2 or x == 3:
                a = 0
        elif y == 1:
            if x == 2:
                a = 0
    if m > 1:
        if x >= 5*5**(m-2) and x <= 6*5**(m-2)-1 and y <= 5*5**(m-2)-1:
            a = 0
        if x >= 9*5**(m-2) and x <= 10*5**(m-2)-1 and y <= 5*5**(m-2)-1:
            a = 0
        if x >= 15*5**(m-2) and x <= 16*5**(m-2)-1 and y <= 5*5**(m-2)-1:
            a = 0
        if x >= 19*5**(m-2) and x <= 20*5**(m-2)-1 and y <= 5*5**(m-2)-1:
            a = 0
        if x >= 6*5**(m-2) and x <= 7*5**(m-2)-1 and y <= 6*5**(m-2)-1:
            a = 0
        if x >= 8*5**(m-2) and x <= 9*5**(m-2)-1 and y <= 6*5**(m-2)-1:
            a = 0
        if x >= 16*5**(m-2) and x <= 17*5**(m-2)-1 and y <= 6*5**(m-2)-1:
            a = 0
        if x >= 18*5**(m-2) and x <= 19*5**(m-2)-1 and y <= 6*5**(m-2)-1:
            a = 0
        if x >= 7*5**(m-2) and x <= 8*5**(m-2)-1 and y <= 7*5**(m-2)-1:
            a = 0
        if x >= 17*5**(m-2) and x <= 18*5**(m-2)-1 and y <= 7*5**(m-2)-1:
            a = 0
        if x >= 10*5**(m-2) and x <= 11*5**(m-2)-1 and y <= 10*5**(m-2)-1:
            a = 0
        if x >= 14*5**(m-2) and x <= 15*5**(m-2)-1 and y <= 10*5**(m-2)-1:
            a = 0
        if x >= 11*5**(m-2) and x <= 12*5**(m-2)-1 and y <= 11*5**(m-2)-1:
            a = 0
        if x >= 13*5**(m-2) and x <= 14*5**(m-2)-1 and y <= 11*5**(m-2)-1:
            a = 0
        if x >= 12*5**(m-2) and x <= 13*5**(m-2)-1 and y <= 12*5**(m-2)-1:
            a = 0
    if a == 0:
        print("crystal")
    elif a == 1:
        print("empty")

#该题与余数有关可以用余数来缩短代码长度
#注意带空格的输入数据
        # CCC 2011 Senior 3: Alice through the Looking Glass
# written by C. Robart
# March 2011

# Recursion. It's simple, once done, but
# it took a LONG while to think of it and debug :-)
#
# Consider the original configuration of blocks
#   _____
#   __X__
#   _XXX_
#
# As the grid expands, with increased m, I think of the blocks
# getting ever smaller, with the same shape of 4 blocks placed on the
# top of the existing blocks.
# So imagine that the above picture is of a 125x125 grid (m=3)
# each of those "blocks" is 25x25, the bottom left one starting at
# x = 25 and running to x = 49. Let's consider x = 35.
# If you divide x by 5^m-1 or 35 by 25, you get 1. More or less
# right back at the beginning. There is a block over x=1, two over x=2
# and a block over x = 3, nothing over x = 0 or 4.
# HOWEVER, and this is the point, we are in the world of m=3, so our "block"
# is really 25 high. Hence there are 1*power (25) blocks above x = 35 when m=3,
# PLUS all the blocks above that!
# The recursive call piles up the smaller blocks,
# with m-1 (=2) and the x in this new world is 10. (35 % 25 = 10).
# Draw a picture and you'll see it. :-)
#
# Back in the main pgm, if y is < the number of blocks above x,
# then x,y is IN the crystal! ged


def crystalSquaresatX(m,x):
    if m >= 1:
        power = 5 ** (m-1)
        location = x // power
        if location == 0 or location == 4:
            return 0
        elif location == 1 or location == 3:
            return 1 * power + crystalSquaresatX(m - 1, x % power)
        elif location == 2:
            return 2 * power + crystalSquaresatX(m - 1, x % power)
        return maxheightatx
    return 0


# file input
file = open("s3.1.in", 'r')
T = eval(file.readline())
for t in range(0,T):
    line = (file.readline())
    space = line.find(" ")
    m = eval(line[0:space])
    line = line[space+1:]
    space = line.find(" ")
    x = eval(line[0:space])
    y = eval(line[space+1:])
    if y < crystalSquaresatX(m,x):
        print "crystal"
    else:
        print "empty"
        

