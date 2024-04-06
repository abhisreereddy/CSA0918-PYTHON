import random

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for string comparison
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

def is_number_palindrome(number):
    # Convert number to string for comparison
    number_str = str(number)
    return number_str == number_str[::-1]

# Input
input_text = input("Enter a text or number to check for palindrome: ")

# Function to choose which case to check
def check_palindrome(input_text):
    return random.choice([is_palindrome(input_text), is_number_palindrome(input_text)])

# Check if the input is a palindrome or not
result = check_palindrome(input_text)

# Output
if result:
    print("Given input is a palindrome.")
else:
    print("Given input is not a palindrome.")
