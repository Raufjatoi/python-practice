ans = input("What is the Answer to the Great Question of life, the Universe, and Everything? ").lower()

match ans:
    case '42' | 'forty-two' | 'forty two':
        print('Yes')
    case _:
        print('No')
