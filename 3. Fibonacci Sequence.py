def fibonacci(n):
    # Method 1: Iterative (efficient)
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

    # Method 2: Recursive with memoization
    # memo = {}
    # def fib(n):
    #     if n in memo:
    #         return memo[n]
    #     if n <= 1:
    #         return n
    #     memo[n] = fib(n-1) + fib(n-2)
    #     return memo[n]
    # return fib(n)

# Example
print(fibonacci(10))  # Output: 55