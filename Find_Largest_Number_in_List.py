list = [10, 20, -30, 40, 50]

minimum = list[1]
# This is the index and we set it as the minimum value which is 20
# Rest all values will be compared with this value to get minimum value

for i in list:
    if i > minimum:
        minimum = i

print("The largest number is: ", minimum)