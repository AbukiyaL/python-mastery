"""
Section: Loops and Iterables
Key Concepts:
- For Loops & Nested Loops
- While Loops & Infinite Loops
- Iterables (Strings, Lists, etc.)
- Logic breaks and state counting
"""
# for loops allow us to repeat a task a number of times
# A program that counts & displays the number of  odd numbers b/n 1 & 10
count = 0
for number in range(1, 10):  # range() iterates beginning from 1 to 10
    if number % 2 != 0:
        print(number)
        count += 1
print(f"we have {count} odd numbers")

# nested loops: we can nest a loop inside another
# Generates a 2D coordinate system (x, y)
for x in range(3):
    for y in range(3):
        print(f"{x}, {y}")

# while loops: used to repeat a task as long as the condition is true
# The following program echos back what the user entered until the user enters "quit"
command = ""
while command.lower() != "quit":  # Case-insensitive termination using the 'quit' sentinel
    command = input("Enter: ")
    print(command)

# Infinite loops run forever and might crush our program
# unless we manage to jump out of them using statements like break
while True:
    command = input("Enter: ")
    print(command)
    if command.lower() == "quit":
        break

# In python range() object are not the only iterable object ; strings are also iterable as well as lists
for i in "course":
    print(i)  # here in each iteration we get one character printed

for x in [2, "microsoft", 5, "python"]:
    print(x)
