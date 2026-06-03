# You are building a smart thermostat alert system.
# If the device_status is "active"
# And temperature > 35 -> Warn: "High temperature alert!"
# Else: "Temperature is normal."
# If device is off -> "Device is offline"

device_status = input("Enter device status (active/offline): ").lower()
temperature = float(input("Enter current temperature: "))

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is offline.")