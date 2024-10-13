while True:
    try:
        ans = input('Ans: ').strip().lower()
        if ans != 'yes':
            raise ValueError()
        else:
            print(": )")
            break
    except ValueError as e:
        pass