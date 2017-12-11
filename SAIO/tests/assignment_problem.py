from unittest import TestCase
from labs.assignment_problem import *
import unittest

class TestAssignmentProblemSolver(TestCase):
  def test_first(self):
    c = [
      [2, 10, 9, 7],
      [15, 4, 14, 8],
      [13, 14, 16, 11],
      [4, 15, 13, 19]
    ]
    self.assertEqual(AssignmentProblemSolver(c).solve(), [2, 1, 3, 0])
  
  def test_second(self):
    c = [
      [2, -1, 9, 4],
      [3, 2, 5, 1],
      [13, 0, -3, 4],
      [5, 6, 1, 2]
    ]
    self.assertEqual(AssignmentProblemSolver(c).solve(), [1, 0, 2, 3])

  def test_third(self):
    c = [
      [6, 4, 13, 4, 19, 15, 11, 8],
      [17, 15, 18, 14, 0, 7, 18, 7],
      [3, 5, 11, 9, 7, 7, 18, 16],
      [17, 10, 16, 19, 9, 6, 1, 5],
      [14, 2, 10, 14, 11, 6, 4, 10],
      [17, 11, 17, 12, 1, 10, 6, 19],
      [13, 1, 4, 2, 2, 7, 2, 14],
      [12, 15, 19, 11, 13, 1, 7, 8]
    ]
    self.assertEqual(AssignmentProblemSolver(c).solve(), [3, 7, 0, 6, 1, 4, 2, 5])

  def test_fourth(self):
    c = [
      [9, 6, 4, 9, 3, 8, 0],
      [5, 8, 6, 8, 8, 3, 5],
      [5, 2, 1, 1, 8, 6, 8],
      [1, 0, 9, 2, 5, 9, 2],
      [9, 2, 3, 3, 0, 3, 0],
      [7, 3, 0, 9, 4, 5, 6],
      [0, 9, 6, 0, 8, 8, 9]
    ]
    self.assertEqual(AssignmentProblemSolver(c).solve(), [6, 5, 3, 1, 4, 2, 0])

  def test_fifth(self):
    c = [
      [6, 6, 2, 4, 7, 1, 9, 4, 6],
      [5, 0, 2, 4, 9, 2, 9, 2, 0],
      [7, 6, 0, 5, 2, 3, 0, 5, 5],
      [9, 5, 8, 9, 2, 3, 1, 5, 7],
      [3, 1, 7, 3, 0, 2, 2, 8, 1],
      [3, 0, 0, 6, 1, 7, 2, 4, 7],
      [5, 6, 1, 9, 9, 8, 4, 1, 8],
      [5, 4, 5, 2, 2, 6, 6, 5, 6],
      [3, 6, 1, 6, 3, 0, 5, 2, 2]
    ]
    self.assertEqual(AssignmentProblemSolver(c).solve(), [5, 8, 2, 6, 4, 1, 7, 3, 0])

if __name__ == '__main__':
  unittest.main()