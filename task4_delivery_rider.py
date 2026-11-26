import csv
import os


FILE_NAME = "riders.csv"


class Rider:

    def __init__(self, rider_id, name):
        self.rider_id = rider_id
        self.name = name
        self.status = "Available"
        self.total_deliveries = 0

    def assign_order(self, order_id):
        self.status = "On Delivery"
        print(self.name, "has been assigned order", order_id)

    def complete_delivery(self):
        self.total_deliveries += 1
        self.status = "Available"
        print(self.name, "completed the delivery.")

    def display_info(self):
        print(
            "ID:", self.rider_id,
            "| Name:", self.name,
            "| Status:", self.status,
            "| Total Deliveries:", self.total_deliveries
        )


def save_riders(riders):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "rider_id",
            "name",
            "status",
            "total_deliveries"
        ])

        for rider in riders:
            writer.writerow([
                rider.rider_id,
                rider.name,
                rider.status,
                rider.total_deliveries
            ])


def load_riders():
    riders = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                rider = Rider(
                    row["rider_id"],
                    row["name"]
                )

                rider.status = row["status"]
                rider.total_deliveries = int(row["total_deliveries"])

                riders.append(rider)

    return riders


riders = load_riders()

if not riders:
    riders = [
        Rider("R001", "Rahul"),
        Rider("R002", "Amit"),
        Rider("R003", "Vijay")
    ]


while True:
    print("\n--- Delivery Rider System ---")
    print("1. Display All Riders")
    print("2. Assign Order")
    print("3. Complete Delivery")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for rider in riders:
            rider.display_info()

    elif choice == "2":
        rider_id = input("Enter rider ID: ")
        order_id = input("Enter order ID: ")

        found = False

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.assign_order(order_id)
                found = True
                break

        if not found:
            print("Rider not found.")

    elif choice == "3":
        rider_id = input("Enter rider ID: ")

        found = False

        for rider in riders:
            if rider.rider_id == rider_id:
                rider.complete_delivery()
                found = True
                break

        if not found:
            print("Rider not found.")

    elif choice == "0":
        save_riders(riders)
        print("Rider data saved successfully.")
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")