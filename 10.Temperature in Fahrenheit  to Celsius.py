def reverse_alphabetical_order(word):
    sorted_word = ''.join(sorted(word, reverse=True))
    return sorted_word
word = input("Enter the word: ")
result = reverse_alphabetical_order(word)
print("Alphabetical Order:", result)
