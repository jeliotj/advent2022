with open('input8.txt') as f:
    data = f.read().splitlines()
f.close()

treerows = len(data)
treecols = len(data[0])
visible = 0
outside_trees = (treerows * 2 + treecols * 2) - 4 #minus corners
scenic_max = 0

for row in range(1, treerows - 1):
    for col in range(1, treecols - 1):
        height = data[row][col]
        scenic_list: list = []

        left = len([x for x in data[row][:col] if x >= height])
        right = len([x for x in data[row][col + 1:] if x >= height])
        up = len([y[col] for y in data[:row] if y[col] >= height])
        down = len([y[col] for y in data[row + 1:] if y[col] >= height])

        left_2 = list(reversed([x for x in data[row][:col]]))
        right_2 = [x for x in data[row][col + 1:]]
        up_2 = list(reversed([y[col] for y in data[:row] if y[col]]))
        down_2 = [y[col] for y in data[row + 1:] if y[col]]
        scenic_grid = [left_2, right_2, up_2, down_2]

        if left == 0 or right == 0 or up == 0 or down == 0:
            visible += 1

        for dir in scenic_grid:
            for d in range(len(dir)):
                if dir[d] >= height: break
            scenic_list.append(d+1)

        scenic_score = scenic_list[0] * scenic_list[1] * scenic_list[2] * scenic_list[3]
        scenic_max = max(scenic_max, scenic_score) # Find highest score P2

total = visible + outside_trees


print(total)
print(scenic_max)

    
