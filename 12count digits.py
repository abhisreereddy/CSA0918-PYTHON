def count_digits(number):
    return len(str(number))
number = input("Enter number: ")
num_digits = count_digits(number)
print("Output:", num_digits)
