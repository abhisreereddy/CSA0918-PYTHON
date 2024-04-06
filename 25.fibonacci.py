def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence
n = int(input("Enter the value of N: "))
fib_numbers = fibonacci(n)
print("Fibonacci sequence up to the", n, "th number:")
print(*fib_numbers)
