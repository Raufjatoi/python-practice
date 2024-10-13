def main():
    time = input('Time : ')
    
    hours = convert(time)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hour , minutes = time.split(':')

    hours = int(hour)
    minutes = int(minutes)

    return hours + minutes / 60

if __name__ == '__main__':
    main()