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
print(calc.add(5, 3))        
print(calc.divide(10, 0))                