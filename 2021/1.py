data = []
increased = 0

for line in open('1.txt', 'r').readlines():
    data.append(int(line.strip()))

for index, item in enumerate(data):
    if item > data[index -1]:
        increased += 1

print (f'Distance increase: {increased}')

increased = 0

for count, value in enumerate(data):
    if 0 < count < len(data) - 2:
        window = value + data[count + 1] + data[count + 2]
        prev_window = data[count - 1] + value + data[count + 1]

        if window > prev_window:
            increased += 1
        
print (f'Window increase: {increased}')