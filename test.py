import random
import time
import sort_algs as sort
import pandas as pd
import os
from rich.progress import Progress
import matplotlib.pyplot as plt

os.system('cls')

def gen_rand_list(min_value, max_value, num_elements):
    return [random.randint(min_value, max_value) for _ in range(num_elements)]

def execute_function(func, *args):
    return func(*args,)

def verify_sort(random_list, sorted_list):
    passed = False
    if sorted_list == sorted(random_list):
        passed = True
    return passed


if __name__ == "__main__":
    min_values = [0]
    # max_values = [10, 100, 1000, 10000]
    max_values = [1000]
    # num_elements = [10, 100, 1000, 10000]
    num_elements = list(range(100, 1100, 100))
    funcs = [sort.quick_sort]

    iterations = len(min_values) * len(max_values) * len(num_elements) * len(funcs)
    print(f"{iterations} Iterations")
    # t = p.add_task("Processing...", total=iterations)

    data = pd.DataFrame(columns=['Algorith', 'Minimum Value', 'Maximum Value', 'n', 'Run Time'])
    print(data)


    with Progress() as p:
        t = p.add_task("Processing...", total=iterations)
        for func in funcs:
            for min_value in min_values:
                for max_value in max_values:
                    for num in num_elements:

                        random_list = gen_rand_list(min_value, max_value, num)
                        low, high = 0, len(random_list) - 1
                        start_time = time.perf_counter()
                        if func != sort.quick_sort:
                            sorted_list = execute_function(func, random_list)
                        else:
                            sorted_list = execute_function(func, random_list, low, high)
                        end_time = time.perf_counter()

                        elapsed = end_time - start_time
                        passed = verify_sort(random_list, sorted_list)

                        if passed == True:
                            print(f"Execution time for {num} elements using {func.__name__}: {elapsed:.6f} seconds\n")
                        else:
                            print(f"Failed to sort {num} elements using {func.__name__}:{elapsed:.6f} seconds\n")
                        new_row_data = {'Algorith': func.__name__, 'Minimum Value': min_value, 'Maximum Value': max_value, 'n': num, 'Run Time': elapsed}
                        new_row_df = pd.DataFrame([new_row_data])
                        data = pd.concat([data, new_row_df], ignore_index=True)
                        p.update(t, advance=1)
    data.index += 1
    print(data)

    # data = {
    #     'Year': [2000, 2001, 2002, 2003, 2004],
    #     'Sales': [100, 120, 110, 130, 150],
    #     'Expenses': [70, 80, 75, 85, 90]
    # }
    # df = pd.DataFrame(data)

    # Plotting a line chart of 'Sales' over 'Year'
    data.plot(x='n', y='Run Time', kind='line', title=func.__name__)
    plt.show()

    # Plotting multiple columns
    # df.plot(x='Year', y=['Sales', 'Expenses'], kind='line', title='Sales vs Expenses')
    # plt.show()