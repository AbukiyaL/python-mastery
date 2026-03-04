"""
control_flow.py
---------------
control flow refers to the order in which instruction are executed
so it allows the program to make decisions
key concepts:
-comparison operators
-conditional statements
-logical operators
-short-circuit
-chaining comparison operators
-for loops & nested loops
-while loops
-infinite loops
-iterables
"""
# > >= ,  < <= , == != are comparison operators
# They return boolean value
print(5 != "5")  # returns True
print("A" > "B")  # compares their equivalent ascii and returns False

# conditional statements a
speed = 20
if speed <= 30:
    print("Good")
elif speed < 50:
    print("warning")
else:
    print("License suspended")

# eligible if high income or good credit and not student
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("not Eligible")

# In python logical operators are  short circuiting meaning

# we can achive clean code by chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# for loops allow us to repeat a task a number of times
# A program that counts & displays the number of  odd numbers b/n 1 & 10
count = 0
for number in range(1, 10):  # range() iterates beginning from 1 to 10
    if number % 2 != 0:
        print(number)
        count += 1
print(f"we have {count} odd numbers")

# nested loops: we can nest a loop inside another
for x in range(3):
    for y in range(3):
        print(f"{x}, {y}")
# while loops: used to repeat a task as long as the condition is true
# The following program echos back what the user entered until the user enters "quit"
# command = ""
# while command.lower() != "quit":
#     command = input("Enter: ")
#     print(command)

# Infinite loops run forever and might crush our program
# unless we manage to jump out of them using statements like break
# while True:
#     command = input("Enter: ")
#     print(command)
#     if command.lower() == "quit":
#         break

# In python range() object are not the only iterable object ; strings are also iterable as well as lists
for i in "course":
    print(i)  # here in each iteration we get one character printed

for x in [2, "microsoft", 5, "python"]:
    print(x)
