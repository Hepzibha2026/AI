# You are creating a tea menu board.
# Each item must be numbered.
# Task:
# Use enumerate() to print menu items with numbers.

menu = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea"]

# for m in menu:
#     print(f"Menu item is {m}")

# for i, m in enumerate(menu):
#     print(f"{i + 1}. {m}")

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")