"""
Example Three
"""
# Initialize a list and assign to produce
produce = ["Apple", "Banana", "Carrot"]
# Initialize a tuple and include a reference to the produce list in the tuple
store = ("Bill's Grocery", produce)
print(id(store))
# Add a new item to the produce list
produce.append("Dragonfruit")
print(id(store))

# Did you notice that the identity of store remained the same?
# But I thought if you changed a mutable object, a new object would
# be created in memory? Why did that not occur here?