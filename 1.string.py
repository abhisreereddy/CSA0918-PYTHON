def check_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
input_str1 = "listen"
input_str2 = "silent"
if check_anagram(input_str1, input_str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
