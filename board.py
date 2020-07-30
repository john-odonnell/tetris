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
        self.row_population = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 14]
        self.heights = [23, 23, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 23]
        self.score = 0

        self.game_over = False

    def _collision_code(self, piece: pc.Piece, x: int, y: int):
        """ Returns True if the piece can be placed at the given (x,y) """
        # checks each block of the piece against its corresponding board position
        for i in range(len(piece.currentBody)):
            for j in range(len(piece.currentBody[0])):
                if self.board[y + i][x + j] != 0 and piece.currentBody[i][j] != 0:
                    return True
        return False

    def rotate_check(self, piece: pc.Piece, direction: int):
        """ Checks if a piece is making a valid rotation
            direction: 0=clockwise, 1=counterclockwise """
        valid = True

        if direction == 0:
            piece.rotate_right()
            valid = self._collision_code(piece, piece.x, piece.y)
            piece.rotate_left()
        elif direction == 1:
            piece.rotate_left()
            valid = self._collision_code(piece, piece.x, piece.y)
            piece.rotate_right()

        return valid

    def drop_check(self, piece: pc.Piece):
        """ Returns True if the piece can drop one row """
        return not self._collision_code(piece, piece.x, piece.y + 1)

    def move_check_left(self, piece: pc.Piece):
        """ Returns True if the piece can move to the left one column """
        return not self._collision_code(piece, piece.x - 1, piece.y)

    def move_check_right(self, piece: pc.Piece):
        """ Returns True if the piece can move to the right one column """
        flag = True
        try:
            flag = self._collision_code(piece, piece.x + 1, piece.y)
        except IndexError:
            pass
        return not flag

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
        """ Updates the population and height matrices to assist row clearing and EOG """
        for i in range(self.height):
            pop = 0
            for j in range(self.width):
                if self.board[i][j] != 0:
                    pop = pop + 1
            self.row_population[i] = pop

        for j in range(self.width):
            height = 0
            while True:
                if self.board[height][j] != 0:
                    self.heights[j] = height
                    break
                height = height + 1

        return

    def _check_full(self) -> list:
        """ Returns a list of rows in the board that are filled """
        rows = []
        for i in range(self.height - 1):
            if self.row_population[i] == 14:
                rows.append(i)
        return rows

    def update_score(self, rows_cleared: int):
        """ Updates score based on the number of lines cleared at once """
        if rows_cleared == 1:
            self.score = self.score + 40
        elif rows_cleared == 2:
            self.score = self.score + 100
        elif rows_cleared == 3:
            self.score = self.score + 300
        elif rows_cleared == 4:
            self.score = self.score + 1200
        return

    def clear_rows(self):
        """ Clears the filled rows on the board """
        # self._clear_rows(self._check_full())
        to_clear = self._check_full()
        for i in to_clear:
            for j in range(1, i + 1):
                self.board[i - j + 1] = self.board[i - j]
            self.board[0] = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
        self.update_score(len(to_clear))
        self.update_populations()
        return

    def end_of_game(self):
        """ Determines if the board is in an EOG state """
        for i in range(2, len(self.heights) - 2):
            if self.heights[i] <= 2:
                self.game_over = True
        return self.game_over
