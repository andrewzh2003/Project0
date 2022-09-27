# test_queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState
import unittest
from collections import namedtuple


class TestQueensState(unittest.TestCase):
    def test_zero_queen_count_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)

    def test_chessboard_creation(self):
        state = QueensState(2,2)
        self.assertEqual(state.chessboard, [[0,0],[0,0]])

    def test_queen_count_after_initializing(self):
        state = QueensState(4,4)
        state.chessboard[0][2] = 1
        self.assertEqual(state.queen_count(), 1)

    def test_queen_position_real(self):
        state = QueensState(4,4)
        state.chessboard[0][2] = 1
        self.assertEqual(state.queens(),[(0,2)])

    def test_emptyList_queen_initially(self):
        state = QueensState(4,4)
        self.assertEqual(state.queens(), [])

    def test_has_queen_false(self):
        Position = namedtuple('Position', ['row', 'column'])
        state = QueensState(2, 2)
        point = Position(2, 1)
        self.assertEqual(state.has_queen(point), False)
        state.chessboard[1][1] = 1
        self.assertEqual(state.has_queen(point), False)
        state.chessboard[1][0] = 1
        self.assertEqual(state.has_queen(point), True)



    # def test_has_queen_true(self):
    #     Position = namedtuple('Position', ['row', 'column'])
    #     point = Position(4,4)
    #     state = QueensState(2,4)

if __name__ == '__main__':
    unittest.main()
