with open("input4.txt", encoding="utf-8") as f:
    subset = 0
    dis = 0
    
    for line in f:
        a = line.strip('\n')
        b = a.split(',')

        b1 = b[0].split('-')
        b1a = int(b1[0])
        b1b = int(b1[1])
        b1set = {x for x in range(b1a, b1b+1)}
        
        b2 = b[1].split('-')
        b2a = int(b2[0])
        b2b = int(b2[1])
        b2set = {x for x in range(b2a, b2b+1)}

        if b1set.issubset(b2set) or b2set.issubset(b1set):
            subset += 1
        if b1set.isdisjoint(b2set):
            dis += 1

    print(subset)
    print(1000-dis)


