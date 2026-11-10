from math import isqrt

def count_divisor_steps(n: int) -> int:
    """Return how many times `count += 1` runs."""
    # TODO: write your solution here
    if n <= 0:
        return 0
    root  = isqrt(n)

    count = 2 * sum(n // i for i in range(1, root + 1))
    count -= root * root
    

    return count
