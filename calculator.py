def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


if __name__ == "__main__":
    # Example usage
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"Sum: {add(x, y)}")
    print(f"Difference: {subtract(x, y)}")