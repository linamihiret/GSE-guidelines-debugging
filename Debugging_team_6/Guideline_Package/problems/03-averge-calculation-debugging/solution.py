# Solution for Problem 01: Debugging Division by Zero in Average Calculation

def calculate_average(scores):
    """
    Calculates the average of non-negative scores.
    Negative values are ignored.
    """

    total = 0
    count = 0

    for s in scores:
        if s >= 0:
            total += s
            count += 1  # Now, only counts non-negative values

    # Handle edge case: no valid scores
    if count == 0:
        raise ValueError("No valid (non-negative) scores provided.")

    return total / count


# Test cases
if __name__ == "__main__":
    print(calculate_average([15, 25, 35]))      # Expected: 25.0
    print(calculate_average([5, 0, 10]))        # Expected: 5.0
    print(calculate_average([]))                # Expected: Error or handled case (empty list)
    print(calculate_average([-1, -3, -5]))      # Expected: Error or handled case (no valid scores)
    print(calculate_average([0, 0, 0]))         # Expected: 0.0 (all zeroes as valid inputs)

    # Edge case test
    try:
        print(calculate_average([-1, -2, -3]))
    except ValueError as e:
        print("Caught expected error:", e)