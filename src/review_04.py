"""
Example Four: list comprehensions
"""

"""
Use a list comprehension to create a new list called new_list out of the numbers list. Use the list comprehension to make sure that the new_list only contains positive numbers and make sure they are cast as integers into the new_list.
"""

numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]

# The nice list comprehension way
new_list = [int(num) for num in numbers if num > 0]
# [expression for item in container if condition]

# Same thing, but with longer syntax
long_way = []
for num in numbers:
    if num > 0:
        long_way.append(int(num))

print(new_list)
print(long_way)