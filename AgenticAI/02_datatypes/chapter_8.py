ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"chai-insert: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"chai-pop: {chai_ingredients}, last added: {last_added}")

# reverse the list
chai_ingredients.reverse()
print(f"chai-reverse: {chai_ingredients}")
# sort the list
chai_ingredients.sort()
print(f"chai-sorted: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")


# operator overloading

base_liquid = ["water", "milk"]
spices = ["ginger"]

full_liquid_mix = base_liquid + spices
print(f"full_liquid_mix: {full_liquid_mix}")

strong_brew = ["black tea"] * 3
print(f"strong_brew: {strong_brew}")

# bytearray
raw_spice_data = bytearray(b"CINNAMON")
new_raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes- raw_spice_data: {raw_spice_data}")
print(f"Bytes- new_raw_spice_data: {new_raw_spice_data}")
