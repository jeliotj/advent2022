#### Part I

with open('input1.txt', encoding="utf-8") as f:
    tempsum = 0
    maxsum = 0
    for line in f:
        if str.isspace(line):
            if tempsum > maxsum:
                maxsum = tempsum
            tempsum = 0
        else:
            tempsum = tempsum + int(line)

    print("The elf with the most calories has: " + str(maxsum) + " calories.")

## Part II

with open('input1.txt', encoding="utf-8") as f:
    tempsum = 0
    highest = 0
    nexthighest = 0
    thirdhighest = 0
    for line in f:
        if str.isspace(line):
            if tempsum > highest:
                thirdhighest = nexthighest
                nexthighest = highest
                highest = tempsum
            elif tempsum < highest and tempsum > nexthighest:
                thirdhighest = nexthighest
                nexthighest = tempsum
            elif tempsum < nexthighest and tempsum > thirdhighest:
                thirdhighest = tempsum
            tempsum = 0
        else:
            tempsum = tempsum + int(line)

    sumofthree = highest + nexthighest + thirdhighest

    print("Highest: " + str(highest))
    print("2nd Highest: " + str(nexthighest))
    print("3rd Highest: " + str(thirdhighest))
    print("Sum of 3 Highest: " + str(sumofthree))



