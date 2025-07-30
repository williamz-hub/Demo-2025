"""
Math Utilities Module

This module provides basic mathematical utility functions for the Demo-2025 project.
Useful for calculations in games, demos, and other applications.
"""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
    
    Returns:
        int|float: Sum of a and b
    """
    return a + b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
    
    Returns:
        int|float: Product of a and b
    """
    return a * b


def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base (int|float): Base number
        exponent (int|float): Exponent
    
    Returns:
        int|float: Result of base^exponent
    """
    return base ** exponent


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n):
    """
    Check if a number is even.
    
    Args:
        n (int): Integer to check
    
    Returns:
        bool: True if n is even, False otherwise
    """
    return n % 2 == 0


def max_of_three(a, b, c):
    """
    Find the maximum of three numbers.
    
    Args:
        a (int|float): First number
        b (int|float): Second number
        c (int|float): Third number
    
    Returns:
        int|float: Maximum of the three numbers
    """
    return max(a, b, c)


if __name__ == "__main__":
    # Simple demonstration of the utility functions
    print("Math Utilities Demo")
    print("===================")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(4, 7) = {multiply(4, 7)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"factorial(5) = {factorial(5)}")
    print(f"is_even(8) = {is_even(8)}")
    print(f"is_even(7) = {is_even(7)}")
    print(f"max_of_three(10, 15, 12) = {max_of_three(10, 15, 12)}")