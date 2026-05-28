is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling # upcasting
print(f"Total actions performed: {total_actions}")


milk_present = 0 # no milk
print(f"Is milk present? {bool(milk_present)}")

# logical operations - and, or, not
water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can we serve tea? {can_serve}")