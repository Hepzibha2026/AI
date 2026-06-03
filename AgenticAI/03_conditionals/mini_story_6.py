# You are building a ticket info system for a railway app.
#     Based on seat type, show its features.

# Task:
# Input: "Sleeper", "AC", "General", "Luxury"
# Match using match-case
# Unknown -> show "Invalid seat type"

seat_type = input("Enter seat type (Sleeper, AC, General, Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: Basic comfort, no AC, suitable for budget travelers.")
    case "ac":
        print("AC: Comfortable seating with air conditioning, ideal for long journeys.")
    case "general":
        print("General: Standard seating, good for short to medium-distance travel.")
    case "luxury":
        print("Luxury: Premium seating with extra amenities, perfect for a comfortable journey.")
    case _:
        print("Invalid seat type")  
