def remove_duplicates(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            result.append(nums[i])
    return result

# Test case
print(remove_duplicates([1, 1, 2, 2, 3]))  
# Expected: [1, 2, 3]