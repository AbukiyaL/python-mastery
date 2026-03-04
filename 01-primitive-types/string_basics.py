"""
string_basics.py
----------------
Strings are immutable sequence of unicode characters
key concepts:
-string creation using double("), single(') and triple
- built-in functions
-indexing and slicing: strings have 0 based indexes
-methods that are specific to strings
-formatted strings
-Type conversion
-Escape sequences
"""
fruit = "apple"
fruit = 'apple'
message = """
Hi smith, 
...
"""  # we use triple quotes to format a long string
print(len(fruit))  # built-in function len returns the number of characters

print(fruit[-1])  # takes us back to end of string so it returns e
# slices the string and returns appl , character at last index is not included

print(fruit[0:4])
print(fruit[:2])  # returns ap , by default python set the unknown to 0

# In python string is an object so we can access its methods using dot notation
print(fruit.lower())
print(fruit.replace("a", "ma"))
print(fruit.strip())  # removes whitespace at the left and right

print(f"I love {fruit}")  # we can concatenate strings using formatted strings

x = "3"  # here x is string so it can't be stored in y
y = int(x) + 1  # using type conversion this converts x in to an integer
print(y)

print("\"python is great!\"")  # we can escape characters using back slash
