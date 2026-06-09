# Hiding Implementation Details

# You're building a simple app that registers users.
# You want to separate concerns:  getting input, validating it, and saving it.

# Task:
# Write register_user() that calls:
# get_input()
# validate_input()
# save_to_db()

def get_input():
    print("Getting user input...")

def validate_input():
    print("Validating user input...")

def save_to_db():
    print("Saving user to database...")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registered successfully!")
# Now, if you want to change how input is validated, you can just modify validate_input() without affecting the other parts of the code.    
register_user()