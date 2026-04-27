def calculate_average(scores):
    total = 0
    count = 0

    for s in scores:
        if s >= 0:
            total += s
        count += 1

    return total / count

# Test cases
print(calculate_average([10, 20, 30]))      # Expected: 20
print(calculate_average([10, -5, 15]))      # Expected: 12.5