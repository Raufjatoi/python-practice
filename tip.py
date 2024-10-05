def main():
    dollars = dollars_to_float(input('How much was the bill : '))
    percent = change_to_percent(input('How muuch tip you gonna give in percent : '))

    tip = dollars  * percent

    print(f'tip = ${tip:.2f}')

def dollars_to_float(d):
    return float(d.replace("$", ""))

def change_to_percent(p):
    return float(p.replace("%", "")) / 100

if __name__ == "__main__":
    main()
