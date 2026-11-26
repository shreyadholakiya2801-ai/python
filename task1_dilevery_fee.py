order_value = float(input("Enter order value: "))
distance = float(input("Enter delivery distance: "))

if order_value < 0 or distance < 0:
    print("Order value and distance cannot be negative.")
    exit()

if order_value >= 500:
    delivery_fee = 0
elif distance <= 5:
    delivery_fee = 30
else:
    delivery_fee = 60

final_amount = order_value + delivery_fee

print("Item Total:", order_value)
print("Delivery Fee:", delivery_fee)
print("Final Amount Payable:", final_amount)