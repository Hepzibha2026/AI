# You want to simulate tea heating.
# It starts at 40degrees celsius and boils at 100degrees celsius.
# Task:
# Use a while loop
# Increase temperature by 15 until it reaches or exceeds 100.
# Print each temperature step.

temperature = 40
while temperature < 100:
    print(f"Current temperature: {temperature}°C")
    temperature += 15
print(f"Tea is ready! Temperature: {temperature}°C")