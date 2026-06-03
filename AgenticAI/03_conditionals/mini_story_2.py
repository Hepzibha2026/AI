# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order.
#     Oterwise, it says it's not available.

# Task:
# Take snack input
# If it's "cookies" or "samosa", confirm the order
# Else, show unavailability message

# multi ways we can get input - web interface, command line, GUI, etc.
# now just get from command line
snack = input("Enter your preferred snack:").lower()
#print(f"User said: {snack}")
if snack == "cookies" or snack == "samosa":
    print(f"Great choice! Your {snack} will be ready soon.")
else:
    print("Sorry, that snack is not available.")