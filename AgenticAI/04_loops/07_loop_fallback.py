# Some chai flavors are out of stock.
# You want to skip those and stop entirely 
# if someone requests a restricted flavor.
# Task:
# Skip if flavor is "Out of stock"
# Break if flavor is "Discontinued"

flavors = ["Vanilla", "Chocolate", "Strawberry", "Out of stock", "Mint", "Discontinued", "Coffee"]
for flavor in flavors:
    if flavor == "Out of stock":
        continue
    if flavor == "Discontinued":
        break
    print("Discontinued item found: " + flavor)
          
print(f"Out side of loop")