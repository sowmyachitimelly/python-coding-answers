
# Program-3.py
# Language: Python
# Description: Generate series with different pattern for odd and even numbers

def generate_series(a):
    series = []
    if a % 2 == 0:
        limit = a - 1
    else:
        limit = a
    for i in range(limit):
        series.append(2 * i + 1)
    return series

# Example Usage
if __name__ == "__main__":
    a = int(input("Enter a number: "))
    result = generate_series(a)
    print(", ".join(map(str, result)))
