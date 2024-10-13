ans = input('Greeting: ').strip().lower()

if ans.startswith('hello'):
    print("$0")
elif ans.startswith('h'):
    print('$20')
else:
    print('$100')