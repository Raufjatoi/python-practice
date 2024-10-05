num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
operator = input('Enter operator (+, -, *, /): ')

match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    case _:
        result = 'Error: Invalid operator'

print(f'result: {result}')
