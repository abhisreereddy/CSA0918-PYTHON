numbers = input("Enter a list of numbers separated by space: ").split()
print("Elements in reverse order:")
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
