menu = {
    "Masala Dosa": {"price": 120, "category": "South Indian"},
    "Paneer Tikka": {"price": 180, "category": "Starter"},
    "Veg Biryani": {"price": 200, "category": "Main Course"},
    "Pizza": {"price": 250, "category": "Fast Food"},
    "Gulab Jamun": {"price": 80, "category": "Dessert"},
    "Cold Coffee": {"price": 100, "category": "Beverage"}
}


def view_all_items():
    print("\n--- Restaurant Menu ---")

    number = 1

    for dish, details in menu.items():
        print(number, dish, "-", details["price"], "-", details["category"])
        number += 1


def filter_by_category():
    category = input("Enter category: ")

    print("\n--- Items in", category, "---")

    for dish, details in menu.items():
        if details["category"].lower() == category.lower():
            print(dish, "-", details["price"])


def search_dish():
    dish_name = input("Enter dish name: ")

    for dish, details in menu.items():
        if dish.lower() == dish_name.lower():
            print("Dish:", dish)
            print("Price:", details["price"])
            return

    print("Dish not found.")


while True:
    print("\n--- Restaurant Menu Manager ---")
    print("1. View All Items")
    print("2. Filter by Category")
    print("3. Search by Dish Name")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_all_items()
    elif choice == "2":
        filter_by_category()
    elif choice == "3":
        search_dish()
    elif choice == "0":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")