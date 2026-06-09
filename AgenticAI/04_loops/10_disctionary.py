# Dictionary
users = [
    {"id": 1, "total": 100, "coupon": "D10"},
    {"id": 2, "total": 200, "coupon": "D20"},
    {"id": 3, "total": 300, "coupon": "D30"}
]

discounts = {
    "D10": (0.1, 10),
    "D20": (0.2, 20),
    "D30": (0.3, 30)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount_amount = user["total"] * percent + fixed
    print(f"User ID: {user['id']}, Discount Amount: {discount_amount}")
    
