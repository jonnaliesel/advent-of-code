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

# part two

'''
down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
'''
depth = 0
horizontal = 0
aim = 0

for index, item in enumerate(data):
    position = item.split()
    direction = position[0]
    steps = int(position[1])

    if direction == 'up' :
        aim -= steps
    elif direction == 'down' :
        aim += steps
    elif direction == 'forward' :
        horizontal += steps
        depth += aim * steps

print('*** Part two ***')
print (f'Horizontal: {horizontal}')
print (f'Depth: {depth}')
print (f'Aim: {aim}')
print (f'Product: {depth * horizontal}')