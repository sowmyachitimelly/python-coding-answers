

# Program-1.py
# Language: Python
# Description: Simple Calculator using Class for basic arithmetic operations with symbols (+, -, *, /)

class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation

    def calculate(self):
        if self.operation == '+':
            return self.a + self.b
        elif self.operation == '-':
            return self.a - self.b
        elif self.operation == '*':
            return self.a * self.b
        elif self.operation == '/':
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b
        else:
            return "Invalid operation symbol! Use +, -, *, or /"

# Example Usage
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation symbol (+, -, *, /): ").strip()
    
    calc = Calculator(a, b, operation)
    print("Result:", calc.calculate())





