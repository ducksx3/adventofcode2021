horizontalCount = 0
depth = 0
with open ("input.txt") as file:
    for line in file:
        if 'forward' in line:
            horizontalCount += int(line.split()[1])        
        if 'up' in line:
            depth -= int(line.split()[1])        
        if 'down' in line:
            depth += int(line.split()[1])
    print("Horizontal: {}\nDepth: {}\nTotal: {}".format(horizontalCount,depth,horizontalCount * depth))
            