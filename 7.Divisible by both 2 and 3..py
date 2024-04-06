def check_divisibility(num):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3.")
    else:
        print(f"{num} is not divisible by both 2 and 3.")
num = int(input("Enter a number: "))
check_divisibility(num)
