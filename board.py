import numpy as np
import piece as pc

""" Board Class
    Describes the game board and it's methods """


class Board:
    """ Represents the standard Tetris board
        10 blocks wide by 20 blocks height
        Contains operations for game flow

        (0, 0) on the Tetris board corresponds
        to the bottom left corner """

    def __init__(self):
        self.board = np.ndarray((10, 20), dtype=bool)

        for i in range(0, 10):
            for j in range(0, 20):
                self.board[i][j] = False

        self.widths = np.zeros((1, 20), dtype=int)
        self.heights = np.zeros((1, 10), dtype=int)

    def place(self, piece: pc.Piece, x: int, y: int):
        """ Places a given Tetris piece at the given xy coordinates """
        rows = piece.body.shape[0]
        cols = piece.body.shape[1]

        for i in range(0, rows):
            for j in range(0, cols):
                if piece.body[i][j] == 1:
                    self.board[x + i][y + j] = True

    def _update_heights(self):
        """ Updates the array of heights """
        for i in range(0, 10):
            self.heights[i] = self.heights[i] - 1
        return

    def _update_widths(self, row_removed: int):
        """ Updates the array of widths """
        for i in range(row_removed, 19):
            self.widths[i] = self.widths[i+1]
        self.widths[19] = 0
        return

    def _check_full(self):
        """ Returns a list of rows in the board that are filled """
        rows = []
        for i in range(0, np.ndarray.max(self.heights)):
            if self.widths[i] == 10:
                rows.append(i)
        return rows

    def _clear_rows(self, rows: list):
        """ Recursively eliminates rows from the board """
        self._clear_rows(rows[1:])

        if len(rows) != 0:
            row = rows[0]

            for i in range(row, np.ndarray.max(self.heights)):
                self.board[row][i] = self.board[row][i+1]

            self._update_heights()
            self._update_widths(row)
        return

    def clear_rows(self):
        """ Clears the filled rows on the board """
        self._clear_rows(self._check_full())
        return
