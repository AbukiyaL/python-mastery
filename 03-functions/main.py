"""
Main Execution Script 
This module serves as the entry point for the 03-function.py
Integrates math, utility and logic modules to showcase python function fundamentals
like *args, **kwargs and modular organization. 
"""

from fizz_logic import fizz_buzz
from math_ops import area_of_circle, add, salary_bonus
from utils import car_detail


def main():

    print(fizz_buzz(15))  # FizzBuzz
    print(fizz_buzz(6))  # Fizz
    print(fizz_buzz(10))  # Buzz
    print(fizz_buzz(7))  # 7

    print(f"Area of Circle: {area_of_circle(5)}")

    print(f"sum: {add(3, 11, -1, 2)}")

    print(salary_bonus(5000))

    print(car_detail(model=2022, color="silver", transmission="manual"))
    print(car_detail(model=2010))


if __name__ == "__main__":
    main()
