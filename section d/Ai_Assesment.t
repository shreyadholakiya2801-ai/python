The program should accept food item names and their prices from the user and calculate the subtotal.

Then:
- Add 18% GST to the subtotal.
- Add a fixed delivery charge of Rs 30.
- Ask the user for the number of previous orders.
- If the user has more than 5 previous orders, apply a 10% loyalty discount.
- Calculate the final payable amount.
- Display a clear and properly formatted receipt showing the items, prices, subtotal, GST, delivery charge, loyalty discount, and final amount.

The program should handle invalid user inputs such as non-numeric prices and invalid order counts without crashing.

AI generated original cord:

items = []

while True:
    try:
        item_name = input("Enter food item name (or 'done' to finish): ")

        if item_name.lower() == "done":
            break

        price = float(input("Enter price: "))

        items.append((item_name, price))

    except ValueError:
        print("Invalid price. Please enter a numeric value.")


subtotal = sum(price for item, price in items)

gst = subtotal * 0.18

delivery_charge = 30

previous_orders = int(input("Enter number of previous orders: "))

if previous_orders > 5:
    loyalty_discount = subtotal * 0.10
else:
    loyalty_discount = 0


final_amount = subtotal + gst + delivery_charge - loyalty_discount


print("\n========== FOOD DELIVERY RECEIPT ==========")

for item, price in items:
    print(item, ":", f"Rs {price:.2f}")

print("-------------------------------------------")
print("Subtotal          :", f"Rs {subtotal:.2f}")
print("GST (18%)         :", f"Rs {gst:.2f}")
print("Delivery Charge   :", f"Rs {delivery_charge:.2f}")
print("Loyalty Discount  :", f"Rs {loyalty_discount:.2f}")
print("-------------------------------------------")
print("Final Amount      :", f"Rs {final_amount:.2f}")
print("===========================================")

Testing:

Bug Found:
The program handles invalid food item prices using try except but it does not handle invalid input for the number of previous orders if the user enters text such as abc instead of a number the program crashes with a ValueError

Improvement:
I added try-except around the previous orders input so that invalid values are handled without crashing the program

final:
I tested the AI generated program without using AI for debugging.
I found that invalid input for the number of previous orders caused the program to crash.
I fixed this issue by adding try-except and validation for the previous order count.
After the correction the program handles invalid input without crashing.
