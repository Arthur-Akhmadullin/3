import random

for files in range(1,11):
    name_file = str(files) + '.txt'

    with open(name_file, 'tw', encoding='utf-8') as f:
        for j in range(0,2):
            f.write(str(random.randint(1,10)) + '\n')
        f.write(str(random.randint(1, 10)))
    f.close()



'''
file = open('file.txt', 'rt')
s = file.readline()
while s != '':
    print(s.rstrip())
    s = file.readline()
file.close()

file = open('file.txt', 'rt')
for s in file:
    print(s.rstrip())
file.close()

file = open('file.txt', 'at')
file.write('\nзатем влюбилась\n')
file.write('в дядю васю')
file.close()

file = open('file.txt', 'rt')
for s in file:
    print(s.rstrip())
file.close()
'''

