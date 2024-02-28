
import random
import math
import matplotlib.pyplot as plt

def estimate_pi_2(N):
    points_inside_circle = 0

    for _ in range(N):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1

    estimated_pi_2 = 4 * points_inside_circle / N
    return estimated_pi_2

# List of N values from 1 to 10,000, incrementing by 50
num_points = list(range(1, 100001, 500))

# Calculate estimated values of pi for different N values
estimated_pi_values = [estimate_pi_2(N) for N in num_points]

# Create a list of the actual value of pi for the same number of points
actual_values = [math.pi] * len(num_points)

# Plot the estimates and the actual value of pi
plt.plot(num_points, estimated_pi_values, label="Estimated Pi")
plt.plot(num_points, actual_values,  label="Actual Pi")
plt.xlabel("Number of Points (N)")
plt.ylabel("Value of Pi")
plt.legend()
plt.title("Estimation of Pi using Monte Carlo Method")
plt.grid(True)
plt.show()