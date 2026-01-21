"""
Bucketsort implementation using linked lists

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import math  # noqa
import random
import time

import BucketSort  # noqa


def radix_sort(array, k):
    '''
    Implements the radix sort algorithm to sort
        data elements with keys in range(k+1)

    Args:
        array: array of data elements
        k: largest key

    >>> array = [10-i for i in range(10)]
    >>> radix_sort(array, 100)
    >>> str(array)
    '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'
    '''


def radix_sort_performance():
    '''
    Method that outputs key range and elapsed time for sorting.
    '''
    for k in range(2*10**4, (12*(10**5))+1, 2*10**4):
        array = [random.randint(0, k) for i in range(10**4)]
        start_time = time.time()
        radix_sort(array, k)
        run_time = (time.time() - start_time) * 1000
        print("%d\t%.1f" % (k, run_time))


if __name__ == "__main__":
    radix_sort_performance()



