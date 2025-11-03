
# Program-2.py
# Language: Python
# Description: Generate odd number series until input 'a'

def generate_series(a):
    series = []
    for i in range(a):
        series.append(2 * i + 1)
    return series

# Example Usage
if __name__ == "__main__":
    a = int(input("Enter a number: "))
    result = generate_series(a)
    print(", ".join(map(str, result)))
