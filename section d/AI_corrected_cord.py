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


while True:
    try:
        previous_orders = int(input("Enter number of previous orders: "))

        if previous_orders < 0:
            print("Order count cannot be negative.")
            continue

        break

    except ValueError:
        print("Invalid order count. Please enter a number.")


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