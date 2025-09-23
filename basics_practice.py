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