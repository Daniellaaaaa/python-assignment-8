# Requirements:
# 1. The class should allow basic operations: add, subtract, multiply, divide.
# 2. Each operation should be a separate method.
# 3. Handle division by zero gracefully.
# 4. Allow both integers and floats.

# Example Usage:
#     calc = Calculator()
#     print(calc.add(5, 3))        # 8
#     print(calc.divide(10, 0))    # "Error: Division by zero"

class Calculator:
    def add(self, first_num, second_num):
        addition=first_num + second_num
        return addition

    def subtract(self, first_num, second_num):
        subtraction=first_num - second_num
        return subtraction

    def multiply(self, first_num, second_num):
        multiplication=first_num * second_num
        return multiplication


    def divide(self, first_num, second_num):
        if second_num == 0:
            return "Error: Division by zero"
        else:
            division=first_num / second_num
            return division



calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.divide(10, 0))    # "Error: Division by zero"                