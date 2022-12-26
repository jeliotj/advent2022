from math import sqrt

head_pos = [0, 0]
tail_pos = [0, 0]
visits = []
atLeastOnce = 0

def checkDist(head, tail):
    d = sqrt((head[0] - tail[0])**2 + (head[1] - tail[1])**2)
    if d >= 2.0:
        return True
    else:
        return False


with open('input9.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip('\n')
    move = int(line[2:])

    for n in range(move):
        if line[0] == "D":
            head_pos[1] -= 1
            if checkDist(head_pos, tail_pos):
                if tail_pos[0] == head_pos[0]:
                    tail_pos[1] -= 1
                elif tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] -= 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] -= 1
        elif line[0] == "U":
            head_pos[1] += 1
            if checkDist(head_pos, tail_pos):
                if tail_pos[0] == head_pos[0]:
                    tail_pos[1] += 1
                elif tail_pos[0] > head_pos[0]:
                    tail_pos[0] -= 1
                    tail_pos[1] += 1
                else:
                    tail_pos[0] += 1
                    tail_pos[1] += 1

        elif line[0] == "R":
            head_pos[0] += 1
            if checkDist(head_pos, tail_pos):
                if tail_pos[1] == head_pos[1]:
                    tail_pos[0] += 1
                elif tail_pos[1] > head_pos[1]:
                    tail_pos[1] -= 1
                    tail_pos[0] += 1
                else:
                    tail_pos[1] += 1
                    tail_pos[0] += 1

        else:
            head_pos[0] -= 1
            if checkDist(head_pos, tail_pos):
                if tail_pos[1] == head_pos[1]:
                    tail_pos[0] -= 1
                elif tail_pos[1] > head_pos[1]:
                    tail_pos[1] -= 1
                    tail_pos[0] -= 1
                else:
                    tail_pos[1] += 1
                    tail_pos[0] -= 1
        if tail_pos not in visits:
            atLeastOnce += 1
            visits.append([tail_pos[0], tail_pos[1]])


print(atLeastOnce)                    