import re

sumofdirs = 0
dirs = {}
currdir = ''
prevdir = ''

def changedir(line, curr):

    dirname = line.split()[-1]
    prevdir = curr
    currdir = dirname

    try: 
        dirs[prevdir][currdir]
    except KeyError:
        if currdir != '/':
            dirs[prevdir][currdir] = {}
        else:
            dirs[currdir] = {}
    return currdir, prevdir

def assigndir(prev, curr):
    dirs[prev][curr] = {}

with open('input7.txt', encoding='utf-8') as f:
    for line in f:

        line = line.strip('\n')

        if re.findall(r'^\$ cd', line):
            currdir, prevdir = changedir(line, currdir)

        elif re.findall(r'^\$ ls', line):
            print(dirs)

        elif re.findall(r'^dir', line):
            dirname = line.split()[-1]
            try:
                dirs[currdir][dirname]
            except KeyError:
                if prevdir != '':
                    dirs[prevdir][currdir][dirname] = {}
                else:
                    dirs[currdir][dirname] = {}
        else:
            n = re.findall(r'[0-9]', line)
            filename = line.split()[-1]
            num = int(''.join(n))
            dirs[currdir][filename] = num
            
print(dirs)

