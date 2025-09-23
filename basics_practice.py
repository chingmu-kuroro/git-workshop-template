import math
def calculate_circle_area(radius):
    return math.pi * radius * radius
print(calculate_circle_area(5))

students = [{"id":1, "name":"Alice", "major":"computer science"}, 
            {"id":2, "name":"Bob", "major":"mathematics"}, 
            {"id":3, "name":"Charlie", "major":"physics"}]

# 寫一個函式，接收一個數字列表，回傳該數字列表的最大值
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))