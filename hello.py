def main():
    name = input('Enter your name: ')
    print(hello(name))

def hello(n='World'):
    return (f"hello , {n}")

if __name__ == "__main__":
    main()

