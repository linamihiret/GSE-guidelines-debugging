# Solution for Problem 03: Debugging List Deduplication Logic

def remove_duplicates(nums):
    """
    Removes duplicates from a sorted list.
    Returns a new list with unique elements.
    """

    if not nums:
        return []

    result = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            result.append(nums[i])

    return result


# Test cases
if __name__ == "__main__":
    print(remove_duplicates([1, 1, 2, 2, 3]))  # Expected: [1, 2, 3]
    print(remove_duplicates([1, 1, 1, 1]))     # Expected: [1]
    print(remove_duplicates([]))               # Expected: []
    print(remove_duplicates([5]))              # Expected: [5]