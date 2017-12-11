from unittest import TestCase
from labs.floyd import *
import unittest
from numpy import inf

class TestFloydSolver(TestCase):
  def test_first(self):
    g = [
      [0, 9, inf, 3, inf, inf ,inf ,inf],
      [9, 0, 2, inf, 7, inf, inf, inf],
      [inf, 2, 0, 2, 4, 8, 6, inf],
      [3, inf, 2, 0, inf, inf, 5, inf],
      [inf, 7, 4, inf, 0, 10, inf, inf],
      [inf, inf, 8, inf, 10, 0, 7, inf],
      [inf, inf, 6, 5, inf, 7, 0, inf],
      [inf, inf, inf, inf, 9, 12, 10, 0]
    ]
    gn = [
      [0, 7, 5, 3, 9, 13, 8, inf],
      [7, 0, 2, 4, 6, 10, 8, inf],
      [5, 2, 0, 2, 4, 8, 6, inf],
      [3, 4, 2, 0, 6, 10, 5, inf],
      [9, 6, 4, 6, 0, 10, 10, inf], 
      [13, 10, 8, 10, 10, 0, 7, inf], 
      [8, 8, 6, 5, 10, 7, 0, inf], 
      [18, 15, 13, 15, 9, 12, 10, 0]
    ]
    self.assertEqual(FloydSolver(g).solve().g, gn)

  def test_second(self):
    g = [
      [0, 3, 2, 6, inf, inf ,inf ,inf, inf],
      [inf, 0, inf, 2, inf, inf, inf ,inf ,inf],
      [inf, inf ,0, inf ,inf, 4, inf, inf ,inf],
      [inf, inf, 3, 0, 1, inf, 6, inf, inf],
      [inf, inf, inf, inf, 0, inf, 7, 5, inf],
      [inf, inf, inf, inf, 5, 0, inf, 4, inf],
      [inf, inf, inf, inf, inf, inf, 0, 2, 4],
      [inf, inf, inf, inf, inf, inf, inf, 0, 4],
      [inf, inf, inf, inf, inf, inf, inf, inf, 0]
    ]
    gn = [
      [0, 3, 2, 5, 6, 6, 11, 10, 14],
      [inf, 0, 5, 2, 3, 9, 8, 8, 12],
      [inf, inf, 0, inf, 9, 4, 16, 8, 12],
      [inf, inf, 3, 0, 1, 7, 6, 6, 10],
      [inf, inf, inf, inf, 0, inf, 7, 5, 9],
      [inf, inf, inf, inf, 5, 0, 12, 4, 8],
      [inf, inf, inf, inf, inf, inf, 0, 2, 4],
      [inf, inf, inf, inf, inf, inf, inf, 0, 4],
      [inf, inf, inf, inf, inf, inf, inf, inf, 0]
    ]
    self.assertEqual(FloydSolver(g).solve().g, gn)

if __name__ == '__main__':
  unittest.main()
