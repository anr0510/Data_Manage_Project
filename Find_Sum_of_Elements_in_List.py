numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the sum
sum_of_numbers = 0

# Iterate through the list and accumulate the sum
for i in numbers:
    sum_of_numbers += i

# Print the sum
print("Sum of elements in the list:", sum_of_numbers)

# Below code also works same as above

list = eval(input("Enter List:"))
sum=0;
for x in list:
        sum = sum + x;
print("The Sum=",sum)