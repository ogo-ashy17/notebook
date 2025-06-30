c = 0
def fibonacci(n: int) -> int:
    global c
    c += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))  # Output: 5
print(c)
# if __name__ == "__main__":
#     # Example usage
#     c = 0
#     print(fibonacci(5, c))  # Output: 5
#     print(c)
#     for i in range(10):
#         c += 1
#     print(c)  # Output: 10

