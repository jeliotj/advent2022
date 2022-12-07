with open("input2.txt", encoding="utf-8") as f:

    score = 0
    for line in f:

        his = line[0]
        my = line[2]
        s = his + my

    #First part of score
        if my == 'X':
            score = score + 1
        elif my == 'Y':
            score = score + 2
        elif my == 'Z':
            score = score + 3

    #Second part of score    
        if s == 'AX' or s == 'BY' or s == 'CZ':
            score = score + 3
            
        elif s == 'AY' or s == 'BZ' or s == 'CX':
            score = score + 6
    print(score)

with open('input2.txt', encoding='utf-8') as f:

    score = 0
    for line in f:

        his = line[0]
        my = line[2]

        if my == 'X':
            if his == 'A':
                score = score + 3
            elif his == 'B':
                score = score + 1
            elif his == 'C':
                score = score + 2
        elif my == 'Y':
            if his == 'A':
                score = score + 1
            elif his == 'B':
                score = score + 2
            elif his == 'C':
                score = score + 3
            score = score + 3
        elif my == 'Z':
            if his == 'A':
                score = score + 2
            elif his == 'B':
                score = score + 3
            elif his == 'C':
                score = score + 1
            score = score + 6
    print(score)
