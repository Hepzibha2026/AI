# You are preparing an order summary with customer names and
# their total bills.
# Task:
# Use two lists: one for names and one for bills
#     print: "[Name] paid $[amount]"

names = ["Alice", "Bob", "Charlie"]
bills = [25.50, 40.00, 15.75]

for name, bill in zip(names, bills):
    print(f"{name} paid ${bill:.2f} USD")