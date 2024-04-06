def sum_of_digits(n, number):
    digit_sum = sum(int(digit) for digit in str(number))
    if digit_sum < 10:
        return digit_sum
    else:
        return sum_of_digits(n, digit_sum)
N = int(input("Enter N value: "))
number = int(input(f"Enter {N} digit number: "))
result = sum_of_digits(N, number)
print(f"Sum of {N} digit number:", result)
