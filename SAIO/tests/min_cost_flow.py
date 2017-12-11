from unittest import TestCase
from labs.min_cost_flow import *
import unittest
from numpy import *

class TestMinCostFlowSolver(TestCase):
  def test_first(self):
    inp = [
      [0, 1, 1, 1],
      [1, 5, 3, 0],
      [2, 1, 3, 3],
      [2, 3, 5, 1],
      [4, 2, 4, 0],
      [4, 3, 1, 5],
      [5, 2, 3, 9],
      [5, 4, 4, 0],
      [5, 0, -2, 0]
    ]
    n = 6
    basic_indexes = set([0, 4, 6, 10, 12])
    nonbasic_indexes = set([2, 8, 14, 16])

    res = [4, 0, 0, 0, 0, 6, 5, 1, 3]
    self.assertEqual(MinCostFlowSolver(inp, n, basic_indexes, nonbasic_indexes).solve().get_x(), res)

  def test_second(self):
    inp = [
      [0, 1, 9, 2],
      [0, 7, 5, 7],
      [1, 2, 1, 4],
      [1, 5, 3, 0],
      [1, 6, 5, 3],
      [2, 8, -2, 0],
      [3, 2, -3, 0],
      [4, 3, 6, 3],
      [5, 4, 8, 4],
      [6, 2, -1, 0],
      [6, 3, 4, 0],
      [6, 4, 7, 5],
      [6, 8, 1, 0],
      [7, 6, 2, 0],
      [7, 8, 2, 0],
      [8, 5, 6, 2]
    ]
    n = 9
    basic_indexes = set([0, 2, 4, 8, 14, 16, 22, 30])
    nonbasic_indexes = set([6, 10, 12, 18, 20, 24, 26, 28])
    res = [0, 9, 4, 1, 0, 0, 0, 0, 5, 0, 5, 1, 0, 2, 0, 1]
    self.assertEqual(MinCostFlowSolver(inp, n, basic_indexes, nonbasic_indexes).solve().get_x(), res)

  def test_third(self):
    inp = [
      [0, 1, 8, 5],
      [0, 7, 3, 0],
      [1, 2, 2, 0],
      [1, 6, 9, 0],
      [2, 5, 4, 0],
      [3, 2, -2, 0],
      [3, 5, 1, 0],
      [4, 3, 8, 6],
      [5, 4, 4, 0],
      [6, 2, 11, 1],
      [6, 4, 6, 7],
      [6, 5, 2, 0],
      [7, 6, 5, 5],
      [7, 5, 5, 6]
    ]

    n = 8
    res = [5, 0, 0, 0, 0, 0, 0, 6, 5, 1, 2, 0, 0, 11]
    basic_indexes = set([0, 2, 14, 18, 20, 24, 26])
    nonbasic_indexes = set([4, 6, 8, 10, 12, 16, 22])
    self.assertEqual(MinCostFlowSolver(inp, n, basic_indexes, nonbasic_indexes).solve().get_x(), res)

  def test_fourth(self):
    inp = [
      [0, 1, 8, 5],
      [0, 7, 3, 4],
      [1, 2, 2, 0],
      [1, 6, 9, 3],
      [2, 5, 4, 0],
      [3, 2, -2, 0],
      [4, 3, -3, 6],
      [5, 4, 8, 7],
      [6, 2, 13, 4],
      [6, 3, 1, 0],
      [6, 4, 1, 0],
      [6, 5, 7, 3],
      [7, 6, 1, 0],
      [7, 5, -1, 0]
    ]
    n = 8
    res = [2, 7, 0, 0, 0, 4, 10, 4, 0, 0, 7, 0, 3, 0]
    basic_indexes = set([0, 2, 6, 12, 14, 16, 22])
    nonbasic_indexes = set([4, 8, 10, 18, 20, 24, 26])
    self.assertEqual(MinCostFlowSolver(inp, n, basic_indexes, nonbasic_indexes).solve().get_x(), res)

if __name__ == '__main__':
  unittest.main()
