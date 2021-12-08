"""
Example One: mutability of lists
Shallow copy - just copying the reference (causes unexpected mutations)
"""
my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = my_list1 # copies the reference
# How would you verify that my_list1 and my_list2 have the same identity?
print("Do my_list1 and my_list2 have same identity?", my_list2 is my_list1)

my_list1.append(7)
# Check if my_list1 and my_list2 still have the same identity.
# If they do, why is that?
print("Do my_list1 and my_list2 still have same identity?", my_list2 is my_list1)


"""
If we don't want to mutate other objects invisibly like this, we avoid using equals assign. Here's the alternative (much like creating a new object with the spread operator in javascript)

Deep copy - copy over the contents to a brand new object, without any lingering association to the original
"""
my_list3 = [1, 2, 3, 4, 5, 6]
my_list4 = list(my_list3)
print(my_list3, my_list4)

print("Do my_list3 and my_list4 have same identity?", my_list4 is my_list3)

my_list3.append(7)
# Check if my_list3 and my_list4 still have the same identity.
# If they do, why is that?
print("Do my_list3 and my_list4 still have same identity?", my_list4 is my_list3)