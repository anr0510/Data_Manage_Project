def find_words(words, k):
    result = []
    for i in words:
        if len(i) > k:
            result.append(i)
    return result

# Example usage
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")


 # Create an empty list   result = []  to store words greater than k
 # Iterate through each word in the list
 # Check if the length of the i is greater than k
 # If yes, append it to the result list
