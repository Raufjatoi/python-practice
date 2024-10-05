list = [3, 4, 1, 2, 5, 6, 8, 7, 9, 10]

find = int(input('Enter number: '))

for n in list:
    if n == find:
        print('Found')
        break
else:
    print('Not found')
