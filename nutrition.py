def main():
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwi": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plum": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    fruit = input("Fruit: ").strip().lower()
    
    if fruit in fruit_calories:
        print(f"Calories: {fruit_calories[fruit]}")
    else:
        print("Invalid fruit")
        
main()
