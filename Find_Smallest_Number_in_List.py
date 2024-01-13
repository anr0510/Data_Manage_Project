# Sample list of numbers
numbers = [30, 10, 45, 5, 20]

# Sort the list in descending order
numbers.sort()

# Check if there are at least two elements in the list
if len(numbers) >= 2:
    second_Smallest = numbers[1]
    print("The second Smallest number in the list is:", second_Smallest)
else:
    print("The list does not contain a second Smallest number.")