list = [1,4,5,6,2,3,8,9,10,7]

min = list[-1]
max = list[1]

for n in list:
    if n < min:
        min=n
    elif n > max:
        max=n
        
print(f'max = {max}')
print(f'min = {min}')