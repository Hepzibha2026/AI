# A tea stall offers different prices for different cup sizes.
#     Write a program that calculates the price based on size.

# Task:
# Input: "small", "medium", "large"
# Small: $10, Medium: $15, Large: $20
# If invalid: show "Unknown cup size."

cup = input("Choose your cup size (small / medium / large): ").lower()

if cup == "small":
    print("The price for a small cup is $10.")
elif cup == "medium":
    print("The price for a medium cup is $15.")
elif cup == "large":
    print("The price for a large cup is $20.")
else:
    print("Unknown cup size.")