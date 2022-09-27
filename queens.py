# queens.py
#
# ICS 33 Fall 2022
# Project 0: History of Modern
#
# A module containing tools that could assist in solving variants of the
# well-known "n-queens" problem.  Note that we're only implementing one part
# of the problem: immutably managing the "state" of the board (i.e., which
# queens are arranged in which cells).
#
# Your goal is to complete the QueensState class described below, though
# you'll need to build it incrementally, as well as test it incrementally by
# writing unit tests in test_queens.py.  Make sure you've read the project
# write-up before you proceed, as it will explain the requirements around
# following (and documenting) an incremental process of solving this problem.
#
# DO NOT MODIFY THE Position NAMEDTUPLE OR THE PROVIDED EXCEPTION CLASSES.

from collections import namedtuple



Position = namedtuple('Position', ['row', 'column'])

# Ordinarily, we would write docstrings within classes or their methods.
# Since a namedtuple builds those classes and methods for us, we instead
# add the documentation by hand afterward.
Position.__doc__ = 'A position on a chessboard, specified by zero-based row and column numbers.'
Position.row.__doc__ = 'A zero-based row number'
Position.column.__doc__ = 'A zero-based column number'



class DuplicateQueenError(Exception):
    """An exception indicating an attempt to add a queen where one is already present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where the duplicate queen exists."""
        self._position = position


    def __str__(self) -> str:
        return f'duplicate queen in row {self._position.row} column {self._position.column}'



class MissingQueenError(Exception):
    """An exception indicating an attempt to remove a queen where one is not present."""

    def __init__(self, position: Position):
        """Initializes the exception, given a position where a queen is missing."""
        self._position = position


    def __str__(self) -> str:
        return f'missing queen in row {self._position.row} column {self._position.column}'



class QueensState:
    """Immutably represents the state of a chessboard being used to assist in
    solving the n-queens problem."""

    def __init__(self, rows: int, columns: int):
        """Initializes the chessboard to have the given numbers of rows and columns,
        with no queens occupying any of its cells."""
        self.rows = rows
        self.columns = columns
        self.chessboard = []
        for i in range(rows):
            self.chessboard.append([])
            for j in range(columns):
                self.chessboard[i].append(0)



    def queen_count(self) -> int:
        total = 0
        for i in self.chessboard:
            for j in i:
                if j == 1:
                    total += 1
        return total


    def queens(self) -> list[Position]:
        """Returns a list of the positions in which queens appear on the chessboard,
        arranged in no particular order."""
        list_of_position = []
        for i in self.chessboard:
            for j in i:
                if j == 1:
                    list_of_position.append((self.chessboard.index(i), i.index(j)))

        return list_of_position


    def has_queen(self, position: Position) -> bool:
        """Returns True if a queen occupies the given position on the chessboard, or
        False otherwise."""
        if self.chessboard[(position[0]) -1][(position[1] -1)] == 1:
            return True
        else:
            return False



    def any_queens_unsafe(self) -> bool:
        """Returns True if any queens on the chessboard are unsafe (i.e., they can
        be captured by at least one other queen on the chessboard), or False otherwise."""
        total = 0
        for i in range(self.rows):
            for j in range(self.columns):
                if self.chessboard[i][j] == 1:
                    for z in range(self.rows):
                        if self.chessboard[z][j] == 1:
                            total += 1
                    if total > 1:
                        return True
                    total = 0
                    for x in range(self.columns):
                        if self.chessboard[i][x] == 1:
                            total += 1
                    if total > 1:
                        return True
                    total = 0

        for i in range(self.rows):
            for j in range(self.columns):
                if self.chessboard[i][j] == 1:
                    total = 0
                    row = i
                    column = j
                    while True:
                        if (0 <= row < self.rows) and (0 <= column < self.columns):
                            if self.chessboard[row][column] == 1:
                                total += 1
                            if total > 1:
                                return True
                            else:
                                row -= 1
                                column -= 1
                        else:
                            break
                    total = 0
                    row = i
                    column = j
                    while True:
                        if (0 <= row < self.rows) and (0 <= column < self.columns):
                            if self.chessboard[row][column] == 1:
                                total += 1
                            if total > 1:
                                return True
                            else:
                                row -= 1
                                column += 1
                        else:
                            break


        return False


    def with_queens_added(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens added in the given positions.
        Raises a DuplicateQueenException when there is already a queen in at
        least one of the given positions."""
        state = QueensState(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                state.chessboard[i][j] = self.chessboard[i][j]
        for i in positions:
            if self.has_queen(i) == True:
                raise DuplicateQueenError(i)
            else:
                state.chessboard[(i[0]) -1][(i[1] -1)] = 1

        return state


    def with_queens_removed(self, positions: list[Position]) -> 'QueensState':
        """Builds a new QueensState with queens removed from the given positions.
        Raises a MissingQueenException when there is no queen in at least one of
        the given positions."""
        state = QueensState(self.rows,self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                state.chessboard[i][j] = self.chessboard[i][j]
        for i in positions:
            if self.has_queen(i) == True:
                state.chessboard[i[0] - 1][i[1] -1] = 0
            else:
                raise MissingQueenError(i)

        return state

