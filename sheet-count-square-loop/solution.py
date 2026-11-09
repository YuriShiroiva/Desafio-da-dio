from math import isqrt
def count_square_loop(n: int) -> int:
    """Return how many times the loop body runs."""
    # TODO: write your solution here
    return isqrt(n) if n >= 0 else 0
