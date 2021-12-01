data = []
increased = 0

for line in open('1.txt', 'r').readlines():
    data.append(int(line.strip()))

for index, item in enumerate(data) :
    if item > data[index -1]:
        increased += 1

increased = 0

for count, value in enumerate(data) :
    if value > data[count -1]:
        increased += 1

print (f'Distance increase: {increased}')
print (f'Window increase: {increased}')