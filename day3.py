import string
from itertools import islice

with open('input3.txt', encoding='utf-8') as f:
    total = 0
    lines = 0
    for line in f:
        h = int((len(line))/2)
        first = set(line[0:h].strip('\n'))
        second = set(line[h:].strip('\n'))
        i = first.intersection(second)
        p = i.pop()
        letters = string.ascii_lowercase + string.ascii_uppercase
        total = total + int(letters.index(p)) + 1
        lines = lines + 1

    print(total)

with open('input3.txt', encoding='utf-8') as f:
    total = 0
    for i in range(0, (int(lines/3))):
        one = set(f.readline().strip('\n'))
        two = set(f.readline().strip('\n'))
        three = set(f.readline().strip('\n'))
        inter = one.intersection(two, three)
        p2 = inter.pop()
        total = total + int(letters.index(p2)) + 1

    print(total)
