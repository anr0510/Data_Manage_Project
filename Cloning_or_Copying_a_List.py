original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

# The [:] slicing notation without specifying start or end indices
# creates a shallow copy of the list.

# The elements of original_list are copied into cloned_list,
# creating an identical but separate list.