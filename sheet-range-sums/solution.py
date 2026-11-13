def range_sums(nums, queries):
    """Return the sum of nums[l..r] for each [l, r] in queries."""
    # This is correct but too slow: it re-adds every range from scratch.
    prefix = [0]
    
    for num in nums:
        prefix.append(prefix[-1] + num)

    result = []

    for left, rigth in queries:
        result.append(prefix[rigth + 1] - prefix[left])
        
    return result
