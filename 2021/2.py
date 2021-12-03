data = []

depth = 0
horizontal = 0

for line in open('2.txt', 'r').readlines():
    data.append(line.strip())

# part one

for index, item in enumerate(data):
    position = item.split()
    direction = position[0]
    steps = int(position[1])

    if direction == 'up' :
        depth -= steps
    elif direction == 'down' :
        depth += steps
    elif direction == 'forward' :
        horizontal += steps

print('*** Part one ***')
print (f'Horizontal: {horizontal}')
print (f'Depth: {depth}')
print (f'Product: {depth * horizontal}\n')