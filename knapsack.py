import time
import random

def knapsack_exhaustive(weights, values, capacity):
    n = len(weights)
    max_value = 0
    # Iterate through all 2^n possibilities
    for i in range(1 << n):
        current_weight = 0
        current_value = 0
        for j in range(n):
            if (i >> j) & 1:
                current_weight += weights[j]
                current_value += values[j]

        if current_weight <= capacity:
            max_value = max(max_value, current_value)
    return max_value

# Testing for different n to find the 10-minute limit
results = []
for n in range(4, 30): # Adjust range as needed
    weights = [random.randint(1, 20) for _ in range(n)]
    values = [random.randint(10, 50) for _ in range(n)]
    capacity = sum(weights) // 2

    start = time.time()
    knapsack_exhaustive(weights, values, capacity)
    end = time.time()

    elapsed = end - start
    results.append((n, elapsed))
    print(f"n={n}, Time: {elapsed:.4f}s")

    if elapsed > 600: # 10 minutes limit
        break
