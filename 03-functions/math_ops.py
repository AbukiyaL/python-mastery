import math


def area_of_circle(radius: int | float) -> float:
    """Calculates the area of a circle using the math library's PI."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)


def add(*numbers: int | float) -> int | float:
    """Calculates the sum of multiple integers or floats."""
    return sum(numbers)


def salary_bonus(salary: int | float, bonus: int = 200) -> int | float:
    """Calculates total pay by adding a fixed integer bonus to the salary."""
    return salary + bonus
