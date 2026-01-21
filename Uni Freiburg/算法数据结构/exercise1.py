"""
Implementation of QuickSort algorithm with different methods of
choosing the pivot method.

Copyright 2016, University of Freiburg.
Olelsii Saukh <saukho@cs.uni-freiburg.de>
"""

import sys
import time
from random import randint


# Quicksort might cause a recursion depth >5000 -> increase limit
sys.setrecursionlimit(6000)


def quicksort(array, randomized=True):
    """
    Sort array in ascending order. Wrapper for the sorting method.

    Args:
        int[] array:    integer array
        bool randomized:    method how to pick pivot. True if randomized.

        >>> array = [20,1]
        >>> quicksort(array, True)
        >>> array
        [1, 20]
        >>> array = [20,1]
        >>> quicksort(array, False)
        >>> array
        [1, 20]
    """
    if len(array) == 0:  
        return
    quicksort_recursive(array, 0, len(array) - 1, randomized)

def quicksort_recursive(array, left, right, randomized):
    """
    Method that recursively divides array on parts and calls the
    rearrangement procedure on each part.

    Args:
        int[] array:    integer array that has to be sorted
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool randomized:    method how to pick pivot. True if randomized.
    """
    if left < right:
        pivot_index = quicksort_divide(array, left, right, randomized)
        quicksort_recursive(array, left, pivot_index - 1, randomized)
        quicksort_recursive(array, pivot_index + 1, right, randomized)


def quicksort_divide(array, left, right, randomized):
    """
    Method that executes the divide step of the algorithm. Method chooses
    pivot element and  performs arranges the elements inside the array in such
    a way, that elements that are smaller than pivot are placed to the left of
    it, and elements that are larger that pivot are placed the the right of
    pivot (arbitrary for elements equal to pivot).

    Args:
        int[] array:    integer array that has to be rearranged.
        int left:    left index from which the rearrangement starts.
        int right:    right index till which the rearrangement goes.
        bool randomized:    method how to pick pivot. True if randomized.
    Returns:
        int:    index where the pivot after the split is located.
    """
     # 1. 选择并确定 pivot（移到区间左边界，简化后续逻辑）
    if randomized:
        # 随机选一个索引（left 到 right 之间），与左边界交换
        pivot_idx = randint(left, right)
        array[left], array[pivot_idx] = array[pivot_idx], array[left]
    # 此时 pivot 固定在左边界（array[left]）
    pivot = array[left]
    
    # 2. 双指针遍历，重排数组
    i = left + 1  # i 是“左部区域的右边界指针”，初始指向左边界+1
    for j in range(left + 1, right + 1):
        # j 遍历从 left+1 到 right 的所有元素
        if array[j] <= pivot:
            # 当前元素属于左部，与 i 位置交换，i 右移
            array[i], array[j] = array[j], array[i]
            i += 1
    
    # 3. 将 pivot 移到左部区域的最右侧（最终位置）
    array[left], array[i - 1] = array[i - 1], array[left]
    return i - 1  # 返回 pivot 的最终索引



def quick_sort_performance(rand_values=True, rand_pivot=True):
    """
    Method that outputs array size and elapsed time for sorting.

    Args:
        rand_values:    True if array should contain random values
        rand_pivot:    switch pivot strategy for evaluation
    """

    for n in range(100, 5001, 100):
        if rand_values:
            array = [randint(0, 5000) for i in range(n)]
        else:
            array = [k for k in range(n, 0, -1)]

        start_time = time.time()
        quicksort(array, rand_pivot)
        run_time = (time.time() - start_time) * 1000
        print("{}\t{:.1f}".format(n, run_time))


if __name__ == "__main__":
    quick_sort_performance(False, False)



