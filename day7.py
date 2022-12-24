with open('input7.txt') as f:
    lines = f.readlines()

dirs = {"/root":0}
path = "/root"

for line in lines:
    if line[0] == "$":
        if line[2:4] == "ls":
            pass

        elif line[2:4] == "cd":
            if line[5:6] == "/":
                path = "/root"

            elif line[5:7] == "..":
                path = path[0:path.rfind("/")]

            else:
                name = line[5:]
                path = path + "/" + name
                dirs.update({path:0})

    elif line[0:3] == "dir":
        pass

    else:
        size = int(line[:line.find(" ")])

        d = path
        for i in range(path.count("/")):
            dirs[d] += size
            d = d[:d.rfind("/")]

total = 0

limit = 30000000 - (70000000 - dirs["/root"])
valid_dirs = []

for d in dirs:

    if dirs[d] < 100000:
        total += dirs[d]

    if limit <= dirs[d]:
        valid_dirs.append(dirs[d])

smallest = min(valid_dirs)

print(total)
print(smallest)
