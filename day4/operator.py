iteration = int(input("enter the number of iterations:"))
numbers = []
for i in range(iteration):
    num = int(input("Enter input {i + 1}: "))
    numbers.append(num)


operation = input("Enter operation choice (add, subtract, divide, multiply, floor divide): ")


result = None

if operation == "add":
    result = 0
    for num in numbers:
        result += num
elif operation == "subtract":
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
elif operation == "divide":
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
elif operation == "multiply":
    result = 1
    for num in numbers:
        result *= num
elif operation == "floor divide":
    result = numbers[0]
    for num in numbers[1:]:
        result //= num
else:
    print("Invalid operation choice!")

if result is not None:
    print("Result:", result)
