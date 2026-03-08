"""
section: conditionals and logic
key concepts:
-Comparison Operators & Chaining Comparison Operators
-Conditional Statements
-Ternary Operators
-Logical Operators(and, or, not)
-Short-Circuiting
-Match-Case(python 3.10+)
"""
# >, >=, <, <=, ==, != are comparison operators
# They return boolean value
print(5 != "5")  # True
print("A" > "B")  # compares their equivalent ascii and returns False
print(10 <= 20)  # True

# we can achive clean code by chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# conditional statements Control execution flow based on boolean condition
speed = 20
if speed <= 30:
    print("Good")
elif speed < 50:
    print("Warning")
else:
    print("License suspended")

# Ternary operators
salary = 25000
status = "Rich" if salary >= 20000 else "Not Rich"
print(status)

# In python logical operators are  short circuiting meaning:
# Evaluation stops once the final outcome is determined, skipping the remaining conditions
# The program prints eligible if a person has high income or good credit and if he/she is not student
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("not Eligible")

# Match-case
user_role = "admin"
match user_role:
    case "admin":
        print("Full Access")
    case "student":
        print("Limited Access")
    case _:
        print("Guest Access")
