"""
Module Calculator: Cung cấp các phép tính toán số học cơ bản.
"""

def add(a, b):
    """Cộng hai số a và b."""
    return a + b

def subtract(a, b):
    """Trừ số b từ số a."""
    return a - b

def multiply(a, b):
    """Nhân hai số a và b."""
    return a * b

def divide(a, b):
    """
    Divide number a by number b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b
