## Day 5
## Advent of Code 2022

import re

# Getting the number of stacks of crates
with open('input5.txt', encoding='utf-8') as f:
    for line in f:
        match = re.findall(r'[0-9]', line)
        if len(match) > 0:
            numcols = int(max(match))
            break

# Initializing the stacks
crates = [[] for _ in range(numcols)]

### Main Loop
with open('input5.txt', encoding='utf-8') as f:
    for line in f:
        if re.findall(r'^ 1', line) != [] or line == '\n':
            # The Blank Line and the Number Line
            continue
        
        elif re.findall(r'^[^m]', line) != []:
            # The Initial Crate Arrangement
            for i in range(1, len(line), 4):
                if line[i] == ' ':
                    continue
                else:
                    crates[round(i/4)].insert(0, line[i])
        else:
            # Get moving
            moves = []
            char = 0
            while line[char] != '\n':
                if line[char].isalpha() or line[char].isspace():
                    char += 1
                    continue
                elif line[char].isdigit():
                    if line[char+1].isdigit():
                        moves.append(int(line[char:(char + 2)]))
                        char += 2
                    else:
                        moves.append(int(line[char]))
                        char += 1
            # Crate Mover 9000
           # for num in range(moves[0]):
           #     temp = crates[moves[1] - 1].pop()
           #     crates[moves[2] - 1].append(temp)

            # Crate Mover 9001
            for num in range(moves[0]):
                temp = []
                temp[num] = crates[moves[1] - 1].pop()
            for item in temp:
                crates[moves[2] - 1].append(temp[-1])


print(crates)


