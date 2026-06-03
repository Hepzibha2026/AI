# You run an online tea store.
# If the order amount is more than $300, delivery is free;
# otherwise, delivery costs $5.

# Task:
# Input: Order_amount
# Use ternary operator to decide delivery fee.

order_amount = float(input("Enter the order amount: "))

# print(f"Order amount: {type(order_amount)}")

delivery_fees = 0 if order_amount > 300 else 5

print(f"Delivery fee: ${delivery_fees}")
