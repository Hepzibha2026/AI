# Dictionary
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe liquid: {chai_recipe['liquid']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"]
print(f"Updated recipe: {chai_recipe}")

print(f"Is 'base' in recipe? {'base' in chai_recipe}")
chai_order = {"type": "Ginger Chai", "size": "Small", "sugar": 1}
print(f"Chai order: {chai_order}")
print(f"Oreder details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Remove last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

chai_size = chai_order["size"]
print(f"Chai size is: {chai_size}")

