# Type-Hinted Calculator

from typing import Optional

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> Optional[float]:
    """Returns the division result. Returns None if divisor is zero."""
    if b == 0:
        return None
    return a / b

def power(base: float, exp: float) -> float:
    """Returns base raised to the power exp."""
    return base ** exp

def modulo(a: int, b: int) -> int:
    """Returns the remainder after division."""
    if b == 0:
        print("Modulo by zero is not allowed.")
        return 0
    return a % b


print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))
print("Power:", power(2, 3))
print("Modulo:", modulo(10, 3))