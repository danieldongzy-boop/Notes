"""
QuickSort algorithm with two pivot strategies and performance measurement.

Author: Zhanyu Dong (based on template by Oleksii Saukh)
University of Freiburg - Algorithms and Data Structures
"""

import sys
import time
import matplotlib.pyplot as plt
from random import randint

# Allow deeper recursion
sys.setrecursionlimit(6000)


def quicksort(array, randomized=True):
    if len(array) == 0:
        return
    quicksort_recursive(array, 0, len(array) - 1, randomized)


def quicksort_recursive(array, left, right, randomized):
    if left < right:
        pivot_index = quicksort_divide(array, left, right, randomized)
        quicksort_recursive(array, left, pivot_index - 1, randomized)
        quicksort_recursive(array, pivot_index + 1, right, randomized)


def quicksort_divide(array, left, right, randomized):
    if randomized:
        pivot_idx = randint(left, right)
        array[left], array[pivot_idx] = array[pivot_idx], array[left]

    pivot = array[left]
    i = left + 1

    for j in range(left + 1, right + 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1


# ========== Performance Measurement ==========

def measure_runtime(n_values, rand_values, rand_pivot):
    results = []
    for n in n_values:
        if rand_values:
            array = [randint(0, 5000) for _ in range(n)]
        else:
            array = [k for k in range(n, 0, -1)]

        start = time.time()
        quicksort(array, rand_pivot)
        elapsed = (time.time() - start) * 1000  # ms
        results.append(elapsed)
    return results


def quick_sort_performance():
    n_values = list(range(100, 5001, 100))

    variants = [
        ("Random values + Random pivot", True, True),
        ("Random values + First pivot", True, False),
        ("Reversed values + Random pivot", False, True),
        ("Reversed values + First pivot", False, False),
    ]

    plt.figure(figsize=(10, 6))
    for label, rand_values, rand_pivot in variants:
        runtimes = measure_runtime(n_values, rand_values, rand_pivot)
        plt.plot(n_values, runtimes, label=label)

    plt.title("QuickSort Runtime Comparison (Linear scale)")
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("quicksort_linear.png")

    # ==== 新增：对数坐标图 ====
    plt.figure(figsize=(10, 6))
    for label, rand_values, rand_pivot in variants:
        runtimes = measure_runtime(n_values, rand_values, rand_pivot)
        plt.plot(n_values, runtimes, label=label)

    plt.yscale("log")
    plt.title("QuickSort Runtime Comparison (Logarithmic scale)")
    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (ms, log scale)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig("quicksort_log.png")
    plt.show()
    # Save simple text summary
    with open("experience.txt", "w") as f:
        f.write("QuickSort Runtime Experiment\n")
        f.write("--------------------------------------------------\n")
        f.write("Compared four variants of QuickSort:\n")
        f.write("1. Random pivot + Random input\n")
        f.write("2. First pivot + Random input\n")
        f.write("3. Random pivot + Reversed input\n")
        f.write("4. First pivot + Reversed input\n\n")
        f.write("Observations:\n")
        f.write("- Random pivot performs consistently well.\n")
        f.write("- Using first element as pivot is bad for reversed arrays (worst case O(n^2)).\n")
        f.write("- Runtime grows roughly as n log n for randomized version.\n")
        f.write("- Reversed arrays show clear degradation for deterministic pivot.\n")




if __name__ == "__main__":
    quick_sort_performance()
