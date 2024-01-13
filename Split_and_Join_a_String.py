input_str = "Python program to split and join a string"

word_list = input_str.split()

separator = "         "

output_str = separator.join(word_list)

print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)



# By default, split on whitespace
# Join the list of words into a string
# specify the separator between words
# Print the results
