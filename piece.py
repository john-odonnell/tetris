import numpy as np

""" Piece Class """
""" Describes the Tetrominoes and their methods """

""" Piece IDs 
    0 - Stick    1 - L1    2 - L2    3 - S1
    4 - S2       5 - Square    6 - Pyramid """


class PieceNode:
    """ Represents a particular orientation of a body
        Contains pointers to the immediate left and right rotations """
    def __init__(self, body: np.ndarray):
        self.body: np.ndarray = body
        self.prev: PieceNode = self
        self.next: PieceNode = self


class PieceList:
    """ Doubly Linked List of piece rotations """
    def __init__(self, piece_id: int, piece: np.ndarray):
        self.id: int = piece_id
        self.head: PieceNode = PieceNode(piece)
        self.current: PieceNode = self.head
        self.num_nodes: int = 1

    """ Fills the Linked List with all rotational iterations 
        of a particular body arrangement """
    def fill_rotations(self):
        if self.id == 5:
            return

        # if self.id == 0 or self.id == 3 or self.id == 4:
        else:
            if self.id == 0 or self.id == 3 or self.id == 4:
                num_rotations = 1
            else:
                num_rotations = 3

            for rot in range(0, num_rotations):
                cols = self.current.body.shape[1]
                rows = self.current.body.shape[0]
                new = np.zeros((cols, rows), dtype=int)

                for i in range(0, rows):
                    for j in range(0, cols):
                        new[cols - 1 - j][i] = self.current.body[i][j]

                new_piece = PieceNode(new)
                new_piece.prev = self.current
                new_piece.next = self.head
                new_piece.prev.next = new_piece
                new_piece.next.prev = new_piece

                self.current = new_piece

            self.current = self.head

        return


class Piece:
    """ Represents a piece's body and its skirt
        Contains a DLL of all rotational iterations of the piece """
    def __init__(self, piece_id: int, body: np.ndarray):
        self.body: np.ndarray = body
        self.id: int = piece_id
        self.skirt: np.ndarray = self.get_skirt()
        self.rotations: PieceList = PieceList(piece_id, body)

        self.rotations.fill_rotations()

    def get_width(self):
        """ Returns the width of the piece """
        return self.body.shape[1]

    def get_height(self):
        """ Returns the height of the piece """
        return self.body.shape[0]

    def get_skirt(self):
        """ Returns an array of the lowest height of the piece """
        skirt = []

        width = self.get_width()
        height = self.get_height()

        for j in range(0, width):
            for i in range(0, height):
                if self.body[i][j] == 1:
                    skirt.append(i)
                    break

        return skirt

    def rotate_right(self):
        """ Rotate the piece to the clockwise """
        self.rotations.current = self.rotations.current.next
        self.body = self.rotations.current
        self.skirt = self.get_skirt()
        return

    def rotate_left(self):
        """ Rotate the piece to the counter-clockwise """
        self.rotations.current = self.rotations.current.prev
        self.body = self.rotations.current
        self.skirt = self.get_skirt()
        return
