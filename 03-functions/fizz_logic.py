def fizz_buzz(number: int) -> str | int:
    """
    Returns 'Fizz', 'Buzz', 'FizzBuzz', or the number based on divisibility.
    Args: 
        number: The positive integer to be evaluated
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative integer or zero.
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected int, but got {type(number).__name__}")
    if number <= 0:
        raise ValueError("Input must be a positive integer")

    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number
