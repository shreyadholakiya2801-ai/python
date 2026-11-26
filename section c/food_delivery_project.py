import json
import os


FILE_NAME = "section_c_orders.json"


class Order:

    next_id = 1

    def __init__(self, customer_name, items, total_amount):
        self.order_id = Order.next_id
        Order.next_id += 1

        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = "Pending"

    def display_order(self):
        print(
            self.order_id,
            "|",
            self.customer_name,
            "|",
            len(self.items),
            "|",
            self.total_amount,
            "|",
            self.status
        )


def load_orders():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_orders(orders):
    with open(FILE_NAME, "w") as file:
        json.dump(orders, file, indent=4)


def place_new_order():
    customer_name = input("Enter customer name: ").strip()

    if customer_name == "":
        print("Customer name cannot be empty.")
        return

    items_input = input("Enter items separated by comma: ").strip()

    if items_input == "":
        print("Items cannot be empty.")
        return

    items = [item.strip() for item in items_input.split(",")]

    try:
        total_amount = float(input("Enter total amount: "))

        if total_amount < 0:
            print("Total amount cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    order = Order(customer_name, items, total_amount)

    orders = load_orders()

    order_data = {
        "order_id": order.order_id,
        "customer_name": order.customer_name,
        "items": order.items,
        "total_amount": order.total_amount,
        "status": order.status
    }

    orders.append(order_data)

    save_orders(orders)

    print("Order placed successfully.")
    print("Order ID:", order.order_id)


def view_all_orders():
    orders = load_orders()

    if not orders:
        print("No orders found.")
        return

    print("\n--- All Orders ---")
    print("ID | Customer | Items | Total | Status")
    print("-" * 55)

    for order in orders:
        print(
            order["order_id"],
            "|",
            order["customer_name"],
            "|",
            len(order["items"]),
            "|",
            order["total_amount"],
            "|",
            order["status"]
        )


def search_order():
    try:
        order_id = int(input("Enter order ID: "))
    except ValueError:
        print("Please enter a valid order ID.")
        return

    orders = load_orders()

    for order in orders:
        if order["order_id"] == order_id:
            print("\nOrder Found")
            print("Order ID:", order["order_id"])
            print("Customer Name:", order["customer_name"])
            print("Items:", ", ".join(order["items"]))
            print("Total Amount:", order["total_amount"])
            print("Status:", order["status"])
            return

    print("Order not found.")


while True:
    print("\n--- Food Delivery Order Management ---")
    print("1. Place New Order")
    print("2. View All Orders")
    print("3. Search Order by ID")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        place_new_order()

    elif choice == "2":
        view_all_orders()

    elif choice == "3":
        search_order()

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
        