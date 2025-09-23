import math
def calculate_circle_area(radius):
    return math.pi * radius * radius
print(calculate_circle_area(5))

students = [{"id":1, "name":"Alice", "major":"computer science"}, 
            {"id":2, "name":"Bob", "major":"mathematics"}, 
            {"id":3, "name":"Charlie", "major":"physics"}]

# 寫一個函式，接收一個數字列表，回傳該數字列表的最大值
def find_max(numbers: list) -> int | None:
    """
    傳回數字列表中的最大值，若列表為空則回傳 None。
    """
    try:
        return max(numbers)
    except ValueError:
        return None

print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# 寫一個程式，從1印到100。
# 如果數字是3的倍數，印"Fizz"；如果是5的倍數，印"Buzz"；如果同時是3和5的倍數，印"FizzBuzz"
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)