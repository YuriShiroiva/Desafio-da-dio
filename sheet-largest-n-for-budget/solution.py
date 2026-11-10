
from math import isqrt

def largest_n(growth: str, budget: int) -> int:
    if growth == "n":
        return budget

    if growth == "n^2":
        return isqrt(budget)

    if growth == "2^n":
        return max(0, budget.bit_length() - 1)

    if growth == "n^3":
        left, right = 0, 10**6

        while left < right:
            mid = (left + right + 1) // 2

            if mid**3 <= budget:
                left = mid
            else:
                right = mid - 1

        return left

    if growth == "n log n":
        left, right = 1, budget + 1

        while left < right:
            mid = (left + right + 1) // 2
            cost = mid * (mid.bit_length() - 1)

            if cost <= budget:
                left = mid
            else:
                right = mid - 1

        return left
