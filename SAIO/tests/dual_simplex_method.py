from unittest import TestCase
from labs.dual_simplex_method import *
from labs.simplex_method import *
import unittest
from numpy import *

class TestDualSimplexMethodSolver(TestCase):
  eps = 0.001

  def is_equal(self, first, second):
    return all(abs(array(first) - second) < self.eps)

  def test_first(self):
    A = array([
      array([2, 1, -1, 0, 0, 1], dtype=float64),
      array([1, 0, 1, 1, 0, 0], dtype=float64),
      array([0, 1, 0, 0, 1, 0], dtype=float64)
    ])
    b = array([2, 5, 0], dtype=float64)
    c = array([3, 2, 0, 3, -2, -4], dtype=float64)
    d_low = array([0, -1, 2, 1, -1, 0], dtype=float64)
    d_high = array([2, 4, 4, 3, 3, 5], dtype=float64)
    x0 = DualSimplexMethodSolver(A,b,c,d_low,d_high).solve()
    res = array([1.5, 1.0, 2.0, 1.5, -1.0, 0.0])
    self.assertEqual(self.is_equal(x0.x, res), True)
    

  def test_second(self):
    A = array([
      array([1, -5, 3, 1, 0, 0], dtype=float64),
      array([4, -1, 1, 0, 1, 0], dtype=float64),
      array([2, 4, 2, 0, 0, 1], dtype=float64)
    ])
    b = array([-7, 22, 30], dtype=float64)
    c = array([7, -2, 6, 0, 5, 2], dtype=float64)
    d_low = array([2, 1, 0, 0, 1, 1], dtype=float64)
    d_high = array([6, 6, 5, 2, 4, 6], dtype=float64)
    x0 = DualSimplexMethodSolver(A,b,c,d_low,d_high).solve()
    res = array([5, 3.0, 1.0, 0, 4.0, 6.0])
    self.assertEqual(self.is_equal(x0.x, res), True)

  def test_third(self):
    A = array([
      array([1, 0, 2, 2, -3, 3], dtype=float64),
      array([0, 1, 0, -1, 0, 1], dtype=float64),
      array([1, 0, 1, 3, 2, 1], dtype=float64)
    ])
    b = array([15, 0, 13], dtype=float64)
    c = array([3, 0.5, 4, 4, 1, 5], dtype=float64)
    d_low = array([0, 0, 0, 0, 0, 0], dtype=float64)
    d_high = array([3, 5, 4, 3, 3, 4], dtype=float64)
    x0 = DualSimplexMethodSolver(A,b,c,d_low,d_high).solve()
    res = array([3, 0, 4.0, 1.1818, 0.6364, 1.1818])
    self.assertEqual(self.is_equal(x0.x, res), True)

  def test_fourth(self):
    A = array([
      array([1, -3, 2, 0, 1, -1, 4, -1, 0], dtype=float64),
      array([1, -1, 6, 1, 0, -2, 2, 2, 0], dtype=float64),
      array([2, 2, -1, 1, 0, -3, 8, -1, 1], dtype=float64),
      array([4, 1, 0, 0, 1, -1, 0, -1, 1], dtype=float64),
      array([1, 1, 1 ,1, 1, 1, 1, 1, 1], dtype=float64)
    ])
    b = array([3, 9, 9, 5, 9], dtype=float64)
    c = array([-1, 5, -2, 4, 3, 1, 2, 8, 3], dtype=float64)
    d_low = array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float64)
    d_high = array([5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=float64)
    x0 = DualSimplexMethodSolver(A,b,c,d_low,d_high).solve()
    res = array([1.1579, 0.6942, 0, 0, 2.8797, 0, 1.0627, 3.2055, 0])
    self.assertEqual(self.is_equal(x0.x, res), True)

  def test_error(self):
    A = array([
      array([1, 7, 2, 0, 1, -1, 4], dtype=float64),
      array([0, 5, 6, 1, 0, -3, -2], dtype=float64),
      array([3, 2, 2, 1, 1, 1, 5], dtype=float64)
    ])
    b = array([1, 4, 7], dtype=float64)
    c = array([1, 2, 1, -3, 3, 1, 0], dtype=float64)
    d_low = array([-1, 1, -2, 0, 1, 2, 4], dtype=float64)
    d_high = array([3, 2, 2, 5, 3, 4, 5], dtype=float64)
    with self.assertRaises(ValueError):
      DualSimplexMethodSolver(A,b,c,d_low,d_high).solve()

if __name__ == "__main__":
    unittest.main()