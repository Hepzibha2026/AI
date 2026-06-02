#set

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# all_spices = essential_spices.union(optional_spices)
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

#common_spices = essential_spices.intersection(optional_spices)
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

#only_in_essential = essential_spices.difference(optional_spices)
only_in_essential = essential_spices - optional_spices
print(f"Spices only in essential: {only_in_essential}")

# member check
print(f"IS 'cloves' in essential spices? {'cloves' in essential_spices}")
print(f"IS 'cloves' in optional spices? {'cloves' in optional_spices}")

# frozenset - immutable unordered collection of unique elements
frozen_spices = frozenset(["cardamom", "ginger", "cinnamon"])
print(f"Frozen spices: {frozen_spices}")