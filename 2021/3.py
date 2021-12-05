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
print(f'Power consumption: {int(gamma_rate, 2) * int(epsilon_rate, 2)}\n')

# part two

oxygen = list(data)
co2 = list(data)

for i in range(len(data[0])):
    if len(oxygen) > 1:
        ox_zeros = len([x  for x in oxygen if x[i]=='0'])
        ox_ones = len([x  for x in oxygen if x[i]=='1'])
        if ox_ones >= ox_zeros:
            oxygen = [x for x in oxygen if x[i]=='1']
        else:
            oxygen = [x for x in oxygen if x[i]=='0']
    if len(co2) > 1:
        co_zeros = len([x  for x in co2 if x[i]=='0'])
        co_ones = len([x  for x in co2 if x[i]=='1'])
        if co_ones >= co_zeros:
            co2 = [x for x in co2 if x[i]=='0']
        else:
            co2 = [x for x in co2 if x[i]=='1']

print(f'Oxygen generator rating: {int(oxygen[0], 2)}')
print(f'CO2 scrubber rating: {int(co2[0], 2)}')
print(f'Life support rating: {int(oxygen[0], 2) * int(co2[0], 2)}')