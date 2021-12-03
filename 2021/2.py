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
        print(f'{depth}')
    elif direction == 'down' :
        depth += steps
        print(f'{depth}')
    elif direction == 'forward' :
        horizontal += steps
        print(f'{horizontal}')

print (f'Horizontal: {horizontal}')
print (f'Depth: {depth}')
print (f'Product: {depth * horizontal}')
