# 1. Using Using the Slice Operator
original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]
print(cloned_list)

# The [:] slicing notation without specifying start or end indices
# creates a shallow copy of the list.

# The elements of original_list are copied into cloned_list,
# creating an identical but separate list.

# =========================================================
# 2. Using the list() constructor
original_list = [1, 2, 3, 4, 5]
cloned_list = list(original_list)
print(cloned_list)

# list(original_list) creates a new list (cloned_list)
# based on the elements present in original_list.
# The list() function is used here to create a new list
# by passing the original_list as an argument.

# =========================================================
# 3. Using List Comprehension
original_list = [1, 2, 3, 4, 5]
cloned_list = [item for item in original_list]
print(cloned_list)