#Tuples () immutable ordered collection of elements
masala_spices = ("cardamom", "cinnamon", "clove", "nutmeg")
(spice1, spice2, spice3, spice4) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}, {spice4}")

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G : {ginger_ratio} and C : {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"After swapping, Ratio is G : {ginger_ratio} and C : {cardamom_ratio}")

# membership testing

print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")
print(f"Is Cinnamon in masala spices? {'Cinnamon' in masala_spices}")

