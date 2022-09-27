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

    def test_any_queen_unsafe(self):
        #tests for false
        state = QueensState(4,4)

        self.assertEqual(state.any_queens_unsafe(), False) ## empty
        state.chessboard[0][1] = 1
        self.assertEqual(state.any_queens_unsafe(), False)# one
        state.chessboard[1][3] = 1
        self.assertEqual(state.any_queens_unsafe(), False) ## two
        state.chessboard[2][0] = 1
        self.assertEqual(state.any_queens_unsafe(), False) ## three
        state.chessboard[3][2] = 1
        self.assertEqual(state.any_queens_unsafe(), False) #3 four (this is optimal any more and it is true)

        #tests for true
        state.chessboard[0][0] = 1
        self.assertEqual(state.any_queens_unsafe(), True) ## checking if any more placed is false

        state2 = QueensState(4,4)
        state2.chessboard[2][1] = 1
        state2.chessboard[3][0] = 1

        self.assertEqual(state2.any_queens_unsafe(), True) ## checking diagonal test

    def test_with_queens_added(self):
        ## no error
        Position = namedtuple('Position', ['row', 'column'])
        point1 = Position(2,2)
        point2 = Position(2,1)
        point3 = Position(3,2)
        state = QueensState(4,4)
        state.chessboard[2][3] = 1
        x = state.with_queens_added([point1,point2,point3])


        #error
        point4 = Position(3,4)
        x2 = state.with_queens_added([point1, point2, point3, point4])

    def test_with_queens_removed(self):
        Position = namedtuple('Position', ['row', 'column'])
        point1 = Position(2, 2)
        point2 = Position(2, 1)
        point3 = Position(3, 2)
        point4 = Position(1, 1)
        state = QueensState(4, 4)
        state.chessboard[2][3] = 1
        x = state.with_queens_added([point1, point2, point3])
        print(x.chessboard)

        y = x.with_queens_removed([point1, point2]) # works
        print(y.chessboard)
        print(x.chessboard)

        x.with_queens_removed([point1, point2, point4]) # doesn't work


if __name__ == '__main__':
    unittest.main()
