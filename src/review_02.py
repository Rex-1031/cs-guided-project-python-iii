"""
Example Two: strings are immutable
"""
my_text1 = "BloomTech"
my_text2 = my_text1
# How would you verify that my_text1 and my_text2 have the same identity?
print(id(my_text1))
print(id(my_text2))
print(my_text1 is my_text2)

my_text1 += " is awesome!"
# Check if my_text1 and my_text2 still have the same identity?
print(id(my_text1))
print(id(my_text2))
print(my_text1 is my_text2)
# If they do not, why is that?

# Now check if my_text1 and my_text2 have the same value?
print("your code here")
# Do they? Explain why or why not.