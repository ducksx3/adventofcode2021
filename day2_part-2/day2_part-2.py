horizontalCount = 0
aim = 0
depth = 0
with open ("input.txt") as file:
    for line in file:
        if 'forward' in line:
            horizontalCount += int(line.split()[1])        
            depth += int(line.split()[1]) * aim
        if 'up' in line:
            aim -= int(line.split()[1])        
        if 'down' in line:
            aim += int(line.split()[1])
    print("Horizontal: {}\nAim: {}\nDepth: {}\nTotal: {}".format(horizontalCount,aim,depth,horizontalCount * depth))