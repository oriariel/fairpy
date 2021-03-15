#!python3

"""
An implementation of the min-sharing algorithm. Reference:

Fedor Sandomirskiy and Erel Segal-Halevi (2020).
["Efficient Fair Division with Minimal Sharing"](https://arxiv.org/abs/1908.01669).

Programmer: Eliyahu Sattat
Since:  2020
"""

import datetime, cvxpy, numpy as np
from time_limit import time_limit, TimeoutException

from fairpy.divisible.ValuationMatrix import ValuationMatrix
from fairpy.divisible.AllocationMatrix import AllocationMatrix

from fairpy.divisible.min_sharing_impl.FairProportionalAllocationProblem import FairProportionalAllocationProblem
from fairpy.divisible.min_sharing_impl.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem

def proportional_allocation_with_min_sharing(valuation_matrix: ValuationMatrix)->AllocationMatrix:
    """
    Finds a proportional allocation with a minimum number of sharings.

    >>> proportional_allocation_with_min_sharing([ [3] , [5] ])   # single item
    [[0.5]
     [0.5]]
    >>> proportional_allocation_with_min_sharing([ [3,3] , [1,1] ])   # two identical items
    [[1. 0.]
     [0. 1.]]
    >>> proportional_allocation_with_min_sharing([ [3,2] , [1,4] ])   # two different items
    [[1. 0.]
     [0. 1.]]
    """
    valuation_matrix = ValuationMatrix(valuation_matrix)
    problem = FairProportionalAllocationProblem(valuation_matrix)  # FairEnvyFreeAllocationProblem
    problem.find_allocation_with_min_shering()
    num_sharing = problem.min_sharing_number
    return AllocationMatrix(problem.min_sharing_allocation)

def envyfree_allocation_with_min_sharing(valuation_matrix: ValuationMatrix)->AllocationMatrix:
    """
    Finds an envy-free allocation with a minimum number of sharings.

    >>> envyfree_allocation_with_min_sharing([ [3] , [5] ])   # single item
    [[0.5]
     [0.5]]
    >>> envyfree_allocation_with_min_sharing([ [3,3] , [1,1] ])   # two identical items
    [[1. 0.]
     [0. 1.]]
    >>> envyfree_allocation_with_min_sharing([ [3,2] , [1,4] ])   # two different items
    [[1. 0.]
     [0. 1.]]
    """
    valuation_matrix = ValuationMatrix(valuation_matrix)
    problem = FairEnvyFreeAllocationProblem(valuation_matrix)  # FairEnvyFreeAllocationProblem
    problem.find_allocation_with_min_shering()
    num_sharing = problem.min_sharing_number
    return AllocationMatrix(problem.min_sharing_allocation)



if __name__ == '__main__':
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))