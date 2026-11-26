import json
import os


FILE_NAME = "orders.json"


def load_orders():
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        else:
            return []

    except FileNotFoundError:
        return []


def save_orders(orders):
    with open(FILE_NAME, "w") as file:
        json.dump(orders, file, indent=4)


def add_order():
    customer_name = input("Enter customer name: ")

    items_input = input("Enter items separated by comma: ")
    items = [item.strip() for item in items_input.split(",")]

    try:
        total_amount = float(input("Enter total amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    order_status = input("Enter order status: ")

    order = {
        "customer_name": customer_name,
        "items": items,
        "total_amount": total_amount,
        "order_status": order_status
    }

    orders = load_orders()
    orders.append(order)
    save_orders(orders)

    print("Order saved successfully.")


def view_orders():
    orders = load_orders()

    if not orders:
        print("No orders found.")
        return

    print("\n--- Order History ---")

    for number, order in enumerate(orders, start=1):
        print("\nOrder", number)
        print("Customer Name:", order["customer_name"])
        print("Items:", ", ".join(order["items"]))
        print("Total Amount:", order["total_amount"])
        print("Status:", order["order_status"])


while True:
    print("\n--- Order History Manager ---")
    print("1. Add New Order")
    print("2. View Orders")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        view_orders()
    elif choice == "0":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Please try again.")