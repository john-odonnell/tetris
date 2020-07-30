""" Piece Class """
""" Describes the Tetrominoes and their methods """

""" Piece IDs 
    0 - Stick    1 - L1    2 - L2    3 - S1
    4 - S2       5 - Square    6 - Pyramid """


class Piece:
    """ Represents a piece's body and its skirt
        Contains a DLL of all rotational iterations of the piece """
    def __init__(self, piece_id: int, bodies: list, x: int, y: int):
        self.pieceId = piece_id
        # list of all body rotations
        self.bodies = bodies
        # which body rotation is currently in use
        self.currentIndex = 0
        self.currentBody = bodies[self.currentIndex]

        # coordinates on the board


        self.x = x
        self.y = y

    """ Setter Functions """
    def set_id(self, piece_id: int):
        self.pieceId = id

    def set_bodies(self, bodies: list):
        self.bodies = bodies

    def set_current_body(self, idx: int):
        self.currentIndex = idx
        self.currentBody = self.bodies[idx]

    def set_x(self, x: int):
        self.x = x

    def set_y(self, y: int):
        self.y = y

    """ Getter Functions """
    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_bodies(self) -> list:
        return self.bodies

    def get_current_body(self) -> list:
        return self.currentBody

    def get_id(self) -> int:
        return self.id

    """ Game Functions """
    def rotate_right(self):
        """ Rotate the piece to the clockwise """
        self.currentIndex = (self.currentIndex + 1) % 4
        self.currentBody = self.bodies[self.currentIndex]

    def rotate_left(self):
        """ Rotate the piece to the counter-clockwise """
        self.currentIndex = (self.currentIndex - 1) % 4
        self.currentBody = self.bodies[self.currentIndex]

    def drop(self):
        """ Changes the y position of the Piece according to level speed """
        self.y = self.y + 1

    def move_left(self):
        """ Moves the piece one block to the left """
        self.x = self.x - 1

    def move_right(self):
        """ Moves the piece one block to the right """
        self.x = self.x + 1
