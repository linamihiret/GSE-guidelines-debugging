# Problem for Debugging: Division by Zero in Average Calculation

def calculate_average(scores):
    """
    Calculates the average of scores.
    However, it incorrectly counts negative values in the denominator.
    """

    total = 0
    count = 0

    for s in scores:
        if s >= 0:
            total += s
        count += 1  # This is incorrectly counting all values (including negatives)

    return total / count


# Test cases
print(calculate_average([15, 25, 35]))      # Expected: 25.0 (but may return incorrect result)
print(calculate_average([5, 0, 10]))        # Expected: 5.0 (but may return incorrect result)
print(calculate_average([]))                # Expected: Error or handled case (division by zero)
print(calculate_average([-1, -3, -5]))      # Expected: Error or handled case (no valid scores)
print(calculate_average([0, 0, 0]))         # Expected: 0.0 (all zeroes as valid inputs)