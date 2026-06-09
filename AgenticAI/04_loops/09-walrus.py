# walrus operator (:=) allows you to assign values to variables as part of an expression.
# It is useful in situations where you want to use a value immediately after assigning it, without needing to write a separate line of code for the assignment.

# without walrus operator
# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# with walrus operator
value = 13

if(remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

# The walrus operator can also be used in loops to assign values while iterating, which can help to avoid redundant calculations.
available_sizes = ["small", "medium", "large"]
if (requested_size := input("Enter a size (small, medium, large): ")) in available_sizes:
    print(f"You selected {requested_size}.")
else:
    print(f"Size is unavailable - {requested_size}")


flavors = ["vanilla", "chocolate", "strawberry"]

print("Available flavors: ", flavors)

# while (requested_flavor := input("Enter a flavor (or 'quit' to exit): ")) != "quit":
#     if requested_flavor in flavors:
#         print(f"You selected {requested_flavor}.")
#     else:
#         print(f"Flavor is unavailable - {requested_flavor}")

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} ice cream")



