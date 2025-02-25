def minimumSwaps(nums):
    n = len(nums)
    
    # Initialize indices
    min_index = -1
    max_index = -1
    
    # Traverse the array to find the indices
    
    for i in range(n):
        if nums[i] == min(nums) and min_index == -1:
            min_index = i  # First occurrence of smallest element
        if nums[i] == max(nums):
            max_index = i  # Last occurrence of largest element (updates on each match)
    
    # Calculate swaps
    swaps = min_index + (n - 1 - max_index)
    
    # Adjust for overlap
    if min_index > max_index:
        swaps -= 1
    
    return swaps

nums = [3, 4, 5, 5, 3, 1]
print(minimumSwaps(nums))  # Output: 6
