"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # use a dictionary to store how many times we've seen each number
    # The keys are numbers from nums (what we know)
    # The dictionary values are how many times we've seen that number (what we want to know)
    my_dict = {num: 0 for num in nums} # dictionary comprehension
    for num in nums:
        my_dict[num] += 1 # Every time we see a number, increment its counter

    # Search the dictionary for a key with value 1. This is the number that only occurs once!
    for (key, val) in my_dict.items():
        if val == 1:
            return key

print(single_number([3,3,2]))
print(single_number([5,2,3,2,3]))
print(single_number([10]))

# Time complexity: O(n) linear (two for loops, each O(n) => O(2n) = O(n))
# Space complexity: O(n) linear

def single_number_quadratic(nums):
    # use an array to store values with no duplicates
    no_dupes = []

    for num in nums:
        if num not in no_dupes: # O(n) for looking up an item in a list
            # Otherwise we haven't seen this one before, so add it to no_dupes
            no_dupes.append(num)
        else:
            # remove if we find a duplicate
            no_dupes.remove(num)

    return no_dupes.pop()

# Time complexity: O(n^2) quadratic (because of line 37 O(n) list lookup happening n times)
# Space complexity: O(n) linear


def single_number_brute_force(nums):
    for (i,num) in enumerate(nums):
        count = 1 # we've seen this number once, see if it happens again
        # look through the rest of the array and see if it is duplicated
        for j in range(i+1,len(nums)):
            if (nums[j] == num):
                count += 1
        
        if count == 1:
            return num

# Time complexity: O(n^2) quadratic
# Space complexity: O(1) constant