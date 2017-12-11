from unittest import TestCase
from labs.resource_allocation import *
import unittest
from numpy import *

class TestRecourceAllocationSolver(TestCase):
  def test_first(self):
    f = array([
      array([0, 3, 4, 5, 8, 9, 10]),
      array([0, 2, 3, 7, 9, 12, 13]),
      array([0, 1, 2, 6, 11, 11 ,13])
    ])
    res = [1, 1, 4]
    self.assertEqual(ResourceAllocationSolver(f).solve().x, res)

  def test_second(self):
    f = array([
      array([0, 1, 2 ,3 ,4 ,5]),
      array([0, 0, 1, 2, 4, 7]),
      array([0, 2, 2, 3, 3, 5])
    ])
    res = [0, 5, 0]
    self.assertEqual(ResourceAllocationSolver(f).solve().x, res)
  
  def test_third(self):
    f = array([
      array([0, 1, 2 ,2 ,4 ,5, 6]),
      array([0, 2, 3, 5 ,7 ,7 ,8]),
      array([0, 2, 4, 5, 6, 7, 7])
    ])
    res = [0, 4, 2]
    self.assertEqual(ResourceAllocationSolver(f).solve().x, res)
  
  def test_fourth(self):
    f = array([
      array([0, 1, 1, 3, 6, 10, 11]),
      array([0, 2, 3, 5, 6, 7, 13]),
      array([0, 1, 4, 4, 7, 8, 9])
    ])
    res = [0, 6, 0]
    self.assertEqual(ResourceAllocationSolver(f).solve().x, res)

  def test_fifth(self):
    f = array([
      array([0, 1, 2, 4, 8, 9, 9, 23]),
      array([0, 2, 4, 6, 6, 8, 10, 11]),
      array([0, 3, 4, 7, 7, 8, 8, 24])
    ])
    res = [0, 0, 7]
    self.assertEqual(ResourceAllocationSolver(f).solve().x, res)

if __name__=='__main__':
  unittest.main()
