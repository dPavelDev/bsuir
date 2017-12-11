from unittest import TestCase
from labs.ford_falkerson import *
import unittest

class TestFordFalkersonSolver(TestCase):
  def test_first(self):
    inp = [
      [0, 1, 4],
      [0, 3, 9],
      [1, 3, 2],
      [1, 4, 4],
      [2, 4, 1],
      [2, 5, 10],
      [3, 2, 1],
      [3, 5, 6],
      [4, 5, 1],
      [4, 6, 2],
      [5, 6, 9]
    ]
    s, t, n = 0, 6, 7
    self.assertEqual(FordFalkersonSolver(inp, n, s, t).solve().flow, 10)

  def test_second(self):
    inp = [
      [0, 1, 3],
      [0, 2, 2],
      [0, 3, 1],
      [0, 5, 6],
      [1, 3, 1],
      [1, 4, 2],
      [2, 3, 1],
      [2, 4, 2],
      [2, 5, 4],
      [3, 4, 7],
      [3, 6, 4],
      [3, 7, 1],
      [3, 5, 5],
      [4, 6, 3],
      [4, 7, 2],
      [5, 7, 4],
      [6, 7, 5],
      [6, 5, 3]
    ]
    s, t, n = 0, 7, 8
    self.assertEqual(FordFalkersonSolver(inp, n, s, t).solve().flow, 10)

  def test_third(self):
    inp = [
      [0, 1, 4],
      [0, 6, 2],
      [0, 5, 5],
      [0, 4, 1],
      [0, 2, 1],
      [1, 3, 1],
      [1, 5, 6],
      [2, 4, 2],
      [3, 6, 3],
      [3, 2, 6],
      [4, 7, 3],
      [4, 5, 4],
      [5, 6, 1],
      [5, 7, 3],
      [5, 8, 6],
      [6, 8, 5],
      [6, 7, 4],
      [7, 8, 4]
    ]
    s, t, n = 0, 8, 9
    self.assertEqual(FordFalkersonSolver(inp, n, s, t).solve().flow, 13)


if __name__ == '__main__':
  unittest.main()