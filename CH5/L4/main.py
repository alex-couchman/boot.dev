from pprint import pprint
import time
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from sklearn.metrics import r2_score

def power_set(nums):
    subsets = [[]]
    if nums == []:
        return subsets
    for num in nums:
        new_subsets = []
        for subset in subsets:
            new_subset = subset.copy()
            new_subset.append(num)
            new_subsets.append(new_subset)
        subsets.extend(new_subsets)
    return subsets

if __name__ == "__main__":
    
    def generate_random_named_color():
        """Selects a random named color from Matplotlib's CSS4 colors."""
        return random.choice(list(mcolors.CSS4_COLORS.keys()))
    
    iterations = 20
    num_elements = []
    run_times = []
    for each in range(1, iterations + 1):
        num_elements.append(each)
        nums = list(range(1, each + 1))
        start = time.perf_counter()
        result = power_set(nums)
        end = time.perf_counter()
        run_time = end - start
        run_times.append(run_time)
        print(f"Done. {run_time:.6f} seconds with {each} elements.")
        # result = sorted(result, key=lambda x: len(x))
        # print(result)
        # pprint(result)
    # print(num_elements)
    # print(run_times)

    # Sample data
    # x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # y = np.array([2, 4, 5, 4, 6, 7, 8, 9, 10, 12])

    x = np.array(num_elements)
    y = np.array(run_times)
    
    # Plot the scatter plot
    plt.scatter(x, y, color='blue', label='Data Points')

    # Choose the degree of the polynomial (e.g., 2 for quadratic, 3 for cubic)
    degrees = [1, 2, 3, 4, 5, 6] # Example: quadratic fit

    for degree in degrees:

        # Calculate the coefficients
        coefficients = np.polyfit(x, y, degree)

        # Create a polynomial function from the coefficients
        polynomial_function = np.poly1d(coefficients)

        # Generate y-values for the best-fit curve
        best_fit_y = polynomial_function(x)

        # Calculate R-squared
        r_squared = r2_score(run_times, best_fit_y)

        # Plot the line of best fit
        plt.plot(x, best_fit_y, color=generate_random_named_color(), label=f'Polynomial Best-Fit (Degree {degree}) R^2={r_squared:.3f}')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot with Line of Best Fit')
    plt.legend()
    plt.grid(True)
    plt.show()