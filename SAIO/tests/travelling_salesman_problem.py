from unittest import TestCase
from labs.travelling_salesman_problem import *
import unittest

class TravellingSalesmanProblem(TestCase):
  def test_first(self):
    c = [
      [inf, 10, 25, 25, 10],
      [1, inf, 10, 15, 2],
      [8, 9, inf, 20, 10],
      [14, 10, 24, inf, 15],
      [10, 8, 25, 27, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 62)

  def test_second(self):
    c = [
      [inf, 2, 1, 10, 6],
      [4, inf, 3, 1, 3],
      [2, 5, inf, 8, 4],
      [6, 7, 13, inf, 3],
      [10, 2, 4, 6, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 12)

  def test_third(self):
    c = [
      [inf, 27, 43, 16, 30, 26],
      [7, inf, 16, 1, 30, 30],
      [20, 13, inf, 35, 5, 0],
      [21, 16, 25, inf, 18, 18],
      [12, 46, 27, 48, inf, 5],
      [23, 5, 5, 9, 5, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 63)

  def test_fourth(self):
    c = [
      [inf, 10, 25, 25, 10],
      [1, inf, 10, 15, 2],
      [8, 9, inf, 20, 10],
      [14, 10, 24, inf, 15],
      [10, 8, 25, 27, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 62)

  def test_fifth(self):
    c = [
      [inf, 10, 10, 8, 13, 1],
      [3, inf, 1, 17, 17, 7],
      [1, 10, inf, 6, 1, 17],
      [6, 3, 2, inf, 5, 12],
      [8, 17, 8, 13, inf, 11],
      [11, 14, 12, 6, 11, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 20)

  def test_six(self):
    c = [
      [inf, 8, 0, 1, 18, 16, 5],
      [19, inf, 12, 5, 11, 8, 17],
      [10, 19, inf, 17, 11, 15, 5],
      [1, 8, 9, inf, 11, 2, 2],
      [11, 12, 14, 8, inf, 4, 1],
      [9, 3, 5, 17, 15, inf, 19],
      [13, 6, 15, 13, 18, 10, inf]
    ]
    res = TravellingSalesmanProblemSolver(c).solve()
    self.assertEqual(res.r, 31)

if __name__ == '__main__':
  unittest.main()