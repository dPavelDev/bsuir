from unittest import TestCase
from labs.integer_linear_programming import *
import unittest
from numpy import *

class TestTheBranchAndBoundMethod(TestCase):
  eps = 0.0000000001

  def is_equal(self, first, second):
    return all(abs(array(first) - second) < self.eps)

  def test_first(self):
    A = array([
      array([1, -5, 3, 1, 0, 0], dtype=float64),
      array([4, -1, 1, 0, 1, 0], dtype=float64),
      array([2, 4, 2, 0, 0, 1], dtype=float64),
    ])
    b = array([-8, 22, 30], dtype=float64)
    c = array([7, -2, 6, 0, 5, 2], dtype=float64)
    d_low = array([2, 1, 0, 0, 1, 1], dtype=float64)
    d_high = array([6, 6, 5, 2, 4, 6], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c, d_low, d_high).the_branch_and_bound_method()
    res = array([6, 3, 0, 1, 1, 6], dtype=float64)
    self.assertEqual(self.is_equal(res, x0.x), True)

  def test_second(self):
    A = array([
      array([1, 0, 3, 1, 0, 0], dtype=float64),
      array([0, -1, 1, 1, 1, 2], dtype=float64),
      array([-2, 4, 2, 0, 0, 1], dtype=float64),
    ])
    b = array([10, 8, 10], dtype=float64)
    c = array([7, -2, 6, 0, 5, 2], dtype=float64)
    d_low = array([0, 1, -1, 0, -2, 1], dtype=float64)
    d_high = array([3, 3, 6, 2, 4, 6], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c, d_low, d_high).the_branch_and_bound_method()
    res = array([1, 1, 3, 0, 2, 2], dtype=float64)
    self.assertEqual(self.is_equal(res, x0.x), True)

  def test_third(self):
    A = array([
      array([1, -3, 2, 0, 1, -1, 4, -1 ,0], dtype=float64),
      array([1, -1, 6, 1, 0, -2, 2, 2, 0], dtype=float64),
      array([2, 2, -1, 1, 0, -3, 8, -1, 1], dtype=float64),
      array([4, 1, 0, 0, 1, -1, 0, -1, 1], dtype=float64),
      array([1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=float64),
    ])
    b = array([3, 9, 9, 5, 9], dtype=float64)
    c = array([-1, 5, -2, 4, 3, 1, 2, 8, 3], dtype=float64)
    d_low = array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=float64)
    d_high = array([5, 5, 5, 5, 5, 5, 5, 5, 5], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c, d_low, d_high).the_branch_and_bound_method()
    res = array([1, 1, 1, 1, 1, 1, 1, 1, 1], dtype=float64)
    self.assertEqual(self.is_equal(res, x0.x), True)

class TestGomoriMethod(TestCase):
  eps = 0.0000000001

  def is_equal(self, first, second):
    return all(abs(array(first) - second) < self.eps)

  def test_first(self):
    A = array([
      array([7, 4, 1], dtype=float64)
    ])
    b = array([13], dtype=float64)
    c = array([21, 11, 0], dtype=float64)
    res = array([ 0., 3., 1., 1., 0.], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c).the_gomori_method()
    self.assertEqual(self.is_equal(res, x0.x), True)

  def test_second(self):
    A = array([
      array([5, -1, 1, 0, 0], dtype=float64),
      array([-1, 2, 0, 1, 0], dtype=float64),
      array([-7, 2, 0, 0, 1], dtype=float64),
    ])
    b = array([15, 6, 0], dtype=float64)
    c = array([-3.5, 1, 0, 0, 0], dtype=float64)
    res = array([0, 0, 15, 6, 0, 3, 0], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c).the_gomori_method()
    self.assertEqual(self.is_equal(res, x0.x), True)

  def test_third(self):
    A = array([
      array([5, 3, 1, 0, 0], dtype=float64),
      array([-1, 2, 0, 1, 0], dtype=float64),
      array([1, -2, 0, 0, 1], dtype=float64),
    ])
    b = array([4, 3, 7], dtype=float64)
    c = array([1, -1, 0, 0, 0], dtype=float64)
    res = array([0, 0, 4, 3, 7, 0], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c).the_gomori_method()
    self.assertEqual(self.is_equal(res, x0.x), True)

  def test_fourth(self):
    A = array([
      array([1, -5, 3, 1, 0,0], dtype=float64),
      array([4, -1, 1, 0, 1,0], dtype=float64),
      array([2, 4, 2, 0, 0, 1], dtype=float64),
    ])
    b = array([-8, 22, 30], dtype=float64)
    c = array([7, -2, 6, 0, 5, 2], dtype=float64)
    res = array([0, 2, 0, 2, 24, 22, 1, 0], dtype=float64)
    x0 = IntegerLinearProgrammingSolver(A, b, c).the_gomori_method()
    self.assertEqual(self.is_equal(res, x0.x), True


if __name__=='__main__':
  unittest.main()