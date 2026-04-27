# Solution for Problem 02: Debugging Incorrect Average Calculation

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
            count += 1

    # Handle edge case: no valid scores
    if count == 0:
        raise ValueError("No valid (non-negative) scores provided.")

    return total / count


# Test cases
if __name__ == "__main__":
    print(calculate_average([10, 20, 30]))      # Expected: 20.0
    print(calculate_average([10, -5, 15]))      # Expected: 12.5

    # Edge case test
    try:
        print(calculate_average([-1, -2, -3]))
    except ValueError as e:
        print("Caught expected error:", e)