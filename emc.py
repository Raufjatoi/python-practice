speed_of_light = 300000000  # 300 million meters per second

def main():
    mass = int(input("Enter mass in kilograms: "))
    
    # Calculate energy using E = mc^2
    energy = mass * speed_of_light ** 2
    
    # Output the energy in Joules
    print(f"Energy (in Joules): {energy}")

if __name__ == "__main__":
    main()
