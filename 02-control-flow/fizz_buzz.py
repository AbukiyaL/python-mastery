"""
Exercise: FizzBuzz (Procedural Version)
1. Used range() built-in function with half open interval
2. Modulo is used to determine divisibility
Note: The most restrictive condition(3 and 5) is placed first
"""
for i in range(1, 16):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
