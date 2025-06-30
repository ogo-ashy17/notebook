
def fibonacci(n: int) -> int:
    c =+ 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # Example usage
    c = 0
    print(fibonacci(5))  # Output: 5
    print(c)
    for i in range(10):
        c =+ 1
    print(c)  # Output: 10

