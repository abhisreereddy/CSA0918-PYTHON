def decimal_to_binary(decimal):
    if decimal < 0:
        return '-' + decimal_to_binary(-decimal)
    elif decimal == 0:
        return '0'
    else:
        binary = ''
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary
test_cases = [(5, "101"), (-4, "-100"), (0, "0"), (1, "1")]
for decimal, expected_output in test_cases:
    result = decimal_to_binary(decimal)
    print(f"Input: {decimal}, Output: {result}, Expected: {expected_output}")
