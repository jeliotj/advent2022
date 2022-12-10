trees = []
visible = 0
tallest_in_row = []
tallest_in_col = []

with open('input8.test', encoding='utf-8') as f:
    for line in f:
        line = line.strip('\n')
        trees.append(line)

    for row in range(len(trees)):
        tallest = 0
        for col in range(len(trees[row])):
            if row == 0 or col == 0 or row == (len(trees) - 1) or col == (len(trees[row]) - 1):
                visible += 1
            if int(trees[row][col]) > tallest:
                tallest = int(trees[row][col])

        if trees[row].count(str(tallest)) == 1:
           tallest_in_row.append([row, trees[row].index(str(tallest)), tallest])

print(visible)
