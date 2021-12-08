"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    # Plan: use a dictionary to remember what I've seen so far
    # The keys of the dictionary are numbers from the list (this is what I know)
    # The values of the dictionary are the indices where those numbers appear in the list (this is what I'm trying to figure out, with the help of the dictionary)
    # I can ask the dictionary "Where is a 5?" and it'll return the index where a 5 exists

    my_dict = {}

    for (i, num) in enumerate(nums): # n loop
        complement = target - num # 1
        # look for the complement, with the help of my favorite dictionary
        if complement in my_dict:
            return [i, my_dict[complement]] # O(1) for dictionary (hashmap) access 
        my_dict[num] = i # O(1) to add to a dictionary. (This goes after because we're not allowing an element to sum with itself)

    return "No two sum solution"

print(two_sum([2,5,9,13], 7)) # expected value: [0,1]
print(two_sum([4,3,5], 8)) # expected value: [1,2]
print(two_sum([9,3,7,12,4], 11)) # expected value: [2,4]

# Time complexity: O(n), constant
# Space complexity: O(n), constant



def two_sum_quadratic(nums, target):
    # Your code here
    # Look through the array, and for each number:
    for (i, num) in enumerate(nums): # n loop
        complement = target - num # 1
        # See if there is a complement for that number (target - num)
        # search the "rest of the list" from after i, not the entire list again
        for j in range(i+1,len(nums)): # n loop (within other n loop)
            if nums[j] == complement: # 1
                return [i,j]
    return "No two sum solution"

# Time complexity: O(n^2), quadratic
# n * (n+1) = n^2 + n

# Space complexity: O(1), constant





# num + complement = target
# complement = target - num