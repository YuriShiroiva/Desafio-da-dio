def count_halving_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    count  = max(0, n.bit_length() - 1)
    return count
