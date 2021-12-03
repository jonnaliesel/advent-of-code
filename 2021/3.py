data = []
modified_data = {}

gamma_rate = ''
epsilon_rate = ''

for line in open('3.txt', 'r').readlines():
    data.append(str(line.strip()))

# part one

for item in data:
    for index, character in enumerate(item):
        try:
            modified_data[index]
        except KeyError:
            modified_data[index] = character
        else:
            modified_data[index] += character

for report in modified_data.values():
    zeros = report.count('0')
    ones = report.count('1')

    if zeros > ones:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(f'Gamma rate: {int(gamma_rate, 2)}')
print(f'Epsilon date: {int(epsilon_rate, 2)}')
print(f'Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')