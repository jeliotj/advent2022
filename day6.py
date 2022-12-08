## Day 6
## Advent of Code 2022
##

pos = 1

with open('input6.txt', encoding='utf-8') as f:
    for line in f:
        ## First Part
##        while True:
##            f.seek(pos)
##            temp = f.read(4)
##            if temp == '':
##                break
##            else:
##                for elem in temp:
##                    if temp.count(elem) > 1:
##                        break
##                    elif temp.count(elem) == 1 and temp.index(elem) == 3:
##                        print(pos+4)
##                        break
##                pos += 1
        ## Second Part
        while True:
            f.seek(pos)
            temp = f.read(14)
            if temp == '':
                break
            else:
                for elem in temp:
                    if temp.count(elem) > 1:
                        break
                    elif temp.count(elem) == 1 and temp.index(elem) == 13:
                        print(pos+14)
                        break
                pos += 1
