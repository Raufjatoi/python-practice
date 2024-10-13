cost = 50

amount_inserted = 0

while amount_inserted < cost:
    coin = int(input('insert coin (5, 10, 25 cents): '))

    if coin in [5, 10, 25]:
        amount_inserted += coin

        if amount_inserted < cost:
            print(f'amount due: {cost - amount_inserted} cents')
    else:
        print('invalid coin. Please insert 5, 10, or 25 cents.')

change = amount_inserted - cost
print(f"change owed: {change} cents")
