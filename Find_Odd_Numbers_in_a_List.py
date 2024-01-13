# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using a list comprehension to filter even numbers
Odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the Odd numbers
print("Even numbers in the list:", Odd_numbers)

# Below and above code is one and the same

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        Odd_numbers.append(num)
    else:
        pass  # For Even numbers, do nothing

print("Even numbers in the list:", Odd_numbers)
