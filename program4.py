
# Program-4.py
# Language: Python
# Description: Count numbers in list that are multiples of 1–9

def count_multiples(numbers):
    result = {}
    for i in range(1, 10):
        count = sum(1 for n in numbers if n % i == 0)
        result[i] = count
    return result

# Example Usage
if __name__ == "__main__":
    numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    output = count_multiples(numbers)
    print(output)
