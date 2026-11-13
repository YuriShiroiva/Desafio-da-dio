def count_pairs_with_sum(nums, target):
    """Return how many pairs i < j have nums[i] + nums[j] == target."""
    seen = {}
    count = 0
    for num in nums:
        count += seen.get(target - num, 0)
        seen[num] = seen.get(num, 0) + 1 
    
    return count
