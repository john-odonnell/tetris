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

    def __init__(self, board: list):
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        self.row_population = []
        self.col_population = []

        # fills the population matrices with 0s on init
        for i in range(0, len(board)):
            self.col_population.append(0)
        for j in range(0, len(board[0])):
            self.row_population.append(0)

    def _collision_code(self, piece: pc.Piece, x: int, y: int):
        """ Returns True if the piece can be placed at the given (x,y) """
        # checks each block of the piece against its corresponding board position
        for i in range(len(piece.currentBody)):
            for j in range(len(piece.currentBody[0])):
                if self.board[y + i][x + j] != 0 and piece.currentBody[i][j] != 0:
                    return True
        return False

    def drop_check(self, piece: pc.Piece):
        """ Returns True if the piece can drop one row """
        return not self._collision_code(piece, piece.x, piece.y + 1)

    def move_check_left(self, piece: pc.Piece):
        """ Returns True if the piece can move to the left one column """
        return not self._collision_code(piece, piece.x - 1, piece.y)

    def move_check_right(self, piece: pc.Piece):
        """ Returns True if the piece can move to the right one column """
        return not self._collision_code(piece, piece.x + 1, piece.y)

    def check_collision(self, piece: pc.Piece, x: int, y: int):
        """ Returning True indicates collision/invalid placement """
        return self._collision_code(piece, piece.x, piece.y)

    def place(self, piece: pc.Piece):
        """ Places a given Tetris piece at the given xy coordinates """
        if not self.check_collision(piece, piece.x, piece.y):
            x = piece.x
            y = piece.y

            for i in range(len(piece.currentBody)):
                for j in range(len(piece.currentBody[0])):
                    if piece.currentBody[i][j] != 0:
                        self.board[y + i][x + j] = piece.currentBody[i][j]

    def update_populations(self):
        """ Updates the population matricies to assist row clearing and EOG """
        for i in range(self.height):
            pop = 0
            for j in range(self.width):
                if self.board[i][j] != 0:
                    pop = pop + 1
            self.row_population[i] = pop

        for j in range(self.width):
            pop = 0
            for i in range(self.height):
                if self.board[i][j] != 0:
                    pop = pop + 1
            self.col_population[j] = pop

    def _check_full(self) -> list:
        """ Returns a list of rows in the board that are filled """
        rows = []
        for i in range(self.height):
            if self.row_population[i] == 10:
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
