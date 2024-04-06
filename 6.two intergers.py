def perform_operations(num1, num2):
    result_and = num1 & num2
    print("Bitwise AND:", bin(result_and))
    result_or = num1 | num2
    print("Bitwise OR:", bin(result_or))
    result_xor = num1 ^ num2
    print("Bitwise XOR:", bin(result_xor))
    result_left_shift = num1 << num2
    print("Left shift:", bin(result_left_shift))
    result_right_shift = num1 >> num2
    print("Right shift:", bin(result_right_shift))
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
perform_operations(num1, num2)
