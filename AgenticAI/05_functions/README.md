Reducing code duplication

You're managing a busy tea stall
you receive many orders and want to print each customer's name along
with the type of chai they ordered.
Task:
Write a function print_order(name, chai_type)
Call it multiple times for different customers

Spliting Complex Tasks

You're creating a monthly report for a cafe's sales.
Instead of putting all logic in one place, break it down.

Task:
Write a function generate_report() that calls:
fetch_sales()
filter_valid_orders()
summarize_data()

Hiding Implementation Details

You're building a simple app that registers users.
You want to separate concerns:  getting input, validating it, and saving it.

Task:
Write register_user() that calls:
get_input()
validate_input()
save_to_db()


Improving Readability

You sell different chai sizes.
Instead of writing formulas everywhere, create a function.
Task:
Write calculate_bill(cups, price_per_cup)
Return total bill
Use this function for multiple orders


Improving Traceability

Your shop adds a 10% VAT on every order.
You want this to be consistent and traceable.
Task:
Write add_vat(price, vat_rate)
Use it to compute final prices for 3 orders
