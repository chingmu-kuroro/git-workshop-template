import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
print(calculate_circle_area(5))  # Example usage

def calculate_square_area(side):
    """Calculate the area of a square given the length of its side."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2
print(calculate_square_area(4))  # Example usage

# 寫一個函式，接收一個數字串列，回傳該串列中的最大值
def find_maximum(numbers):
    """Return the maximum value from a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty")
    return max(numbers)
print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5]))  # Example usage