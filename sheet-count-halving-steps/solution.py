def count_halving_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    count  = 0 
    while n > 1:
        n //= 2
        count += 1
    return count
