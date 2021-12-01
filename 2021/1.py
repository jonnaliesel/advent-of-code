data = []
increased = 0

for line in open('1.txt', 'r').readlines():
    data.append(int(line.strip()))

for index, item in enumerate(data) :
    if item > data[index -1]:
        increased += 1

print (increased)