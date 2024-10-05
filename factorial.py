num = int(input('Enter a number: '))
value = 1

for i in range(1, num + 1):
    value *= i

print(f'Factorial of {num} is {value}')
