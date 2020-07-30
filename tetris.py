import pygame
import board as bd
import piece as pc
import random as rand

BLOCK_SIZE = 25

""" Initialize Pygame, constant screen and surfaces """
pygame.init()
# (0,0) is the top left corner of the screen
screen = pygame.display.set_mode((12*BLOCK_SIZE, 22*BLOCK_SIZE))
# board and piece surface are responsible for drawing their own components
# and updating when need be
# board_surface = pygame.Surface((12*BLOCK_SIZE, 22*BLOCK_SIZE))

""" (0,0) on the board is the top left corner
    This is to simplify the process of printing the board onto a surface
    The board has a rim on the left and right of 0s, and 1s on the bottom
    This is to facilitate piece hit-boxes extending past the playable game board """
sample_board = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# initialize board abstraction
board_class = bd.Board(sample_board)

""" Body arrays are vertically inverted due to the inversion of the game board """
i_bodies = [
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0]
    ],
    [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]
    ]
]
j_bodies = [
    [
        [0, 0, 0],
        [2, 2, 2],
        [2, 0, 0]
    ],
    [
        [0, 2, 0],
        [0, 2, 0],
        [0, 2, 2]
    ],
    [
        [0, 0, 2],
        [2, 2, 2],
        [0, 0, 0]
    ],
    [
        [2, 2, 0],
        [0, 2, 0],
        [0, 2, 0]
    ]
]
l_bodies = [
    [
        [0, 0, 0],
        [3, 3, 3],
        [0, 0, 3]
    ],
    [
        [0, 3, 3],
        [0, 3, 0],
        [0, 3, 0]
    ],
    [
        [3, 0, 0],
        [3, 3, 3],
        [0, 0, 0]
    ],
    [
        [0, 3, 0],
        [0, 3, 0],
        [3, 3, 0]
    ]
]
o_bodies = [
    [
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [0, 4, 4, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [0, 4, 4, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [0, 4, 4, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 4, 4, 0],
        [0, 4, 4, 0]
    ]
]
s_bodies = [
    [
        [0, 0, 0],
        [5, 5, 0],
        [0, 5, 5]
    ],
    [
        [0, 0, 5],
        [0, 5, 5],
        [0, 5, 0]
    ],
    [
        [5, 5, 0],
        [0, 5, 5],
        [0, 0, 0]
    ],
    [
        [0, 5, 0],
        [5, 5, 0],
        [5, 0, 0]
    ]
]
t_bodies = [
    [
        [0, 0, 0],
        [6, 6, 6],
        [0, 6, 0]
    ],
    [
        [0, 6, 0],
        [0, 6, 6],
        [0, 6, 0]
    ],
    [
        [0, 6, 0],
        [6, 6, 6],
        [0, 0, 0]
    ],
    [
        [0, 6, 0],
        [6, 6, 0],
        [0, 6, 0]
    ]
]
z_bodies = [
    [
        [0, 0, 0],
        [0, 7, 7],
        [7, 7, 0]
    ],
    [
        [0, 7, 0],
        [0, 7, 7],
        [0, 0, 7]
    ],
    [
        [0, 7, 7],
        [7, 7, 0],
        [0, 0, 0]
    ],
    [
        [7, 0, 0],
        [7, 7, 0],
        [0, 7, 0]
    ]
]

# hosts all piece body lists
bodies = [i_bodies, j_bodies, l_bodies, o_bodies, s_bodies, t_bodies, z_bodies]


def draw_stdout():
    """ Draws the Tetris board state to stdout for debugging purposes """
    for j in range(board_class.height):
        for i in range(board_class.width):
            if board_class.board[j][i] != 0:
                print(board_class.board[j][i], end=" ")
            else:
                print(" ", end=" ")
        print("\n")


def draw_board(board_surface: pygame.Surface):
    """ Draws the board onto the board surface """
    for j in range(board_class.height):
        for i in range(board_class.width):
            if board_class.board[j][i] != 0:
                pygame.draw.rect(board_surface, (255, 255, 255),
                                 (i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_piece(piece: pc.Piece, piece_surface: pygame.Surface):
    """ Draws a given piece onto a given piece surface """
    for j in range(len(piece.currentBody)):
        for i in range(len(piece.currentBody[0])):
            if piece.currentBody[j][i] != 0:
                pygame.draw.rect(piece_surface, (255, 255, 255),
                                 ((piece.x * BLOCK_SIZE) + (i * BLOCK_SIZE),
                                  ((piece.y * BLOCK_SIZE) + (j * BLOCK_SIZE)),
                                  BLOCK_SIZE, BLOCK_SIZE))


def game_loop():
    """ Main Game Loop
        Contains event handling and calls to piece and board classes """
    playing = True
    # frequency defined in milliseconds
    drop_freq = 500
    maxfps = 30

    dontburn = pygame.time.Clock()
    DROPEVENT = pygame.USEREVENT
    pygame.time.set_timer(DROPEVENT, drop_freq)

    id_next = rand.randint(0, 6)
    next_piece = pc.Piece(id_next, bodies[id_next], 3, 0)

    while playing:

        # assign this piece from next piece
        piece_id = id_next
        piece = next_piece
        # creat next piece
        id_next = rand.randint(0, 6)
        next_piece = pc.Piece(id_next, bodies[id_next], 3, 0)

        board_surface = pygame.Surface((12 * BLOCK_SIZE, 22 * BLOCK_SIZE))
        draw_board(board_surface)

        falling = True
        while falling:
            # establish background
            screen.fill((0, 0, 0))
            # create black piece surface
            piece_surface = pygame.Surface((12 * BLOCK_SIZE, 22 * BLOCK_SIZE))

            # draw board and then piece
            draw_board(board_surface)
            draw_piece(piece, piece_surface)
            # blit board and then piece
            screen.blit(board_surface, (0, 0))
            screen.blit(piece_surface, (0, 0))
            # update display
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    falling = False
                    playing = False
                    pygame.quit()
                    exit()
                elif event.type == DROPEVENT:
                    # drop piece according to speed
                    if board_class.drop_check(piece):
                        piece.drop()
                    else:
                        falling = False
                elif event.type == pygame.KEYDOWN:
                    # keypress events
                    if event.key == pygame.K_a and board_class.move_check_left(piece):
                        piece.move_left()
                    elif event.key == pygame.K_d and board_class.move_check_right(piece):
                        piece.move_right()
                    elif event.key == pygame.K_s:
                        piece.rotate_right()
                    elif event.key == pygame.K_w:
                        piece.rotate_left()

            piece_surface.fill((0, 0, 0, 0))

            dontburn.tick(maxfps)

        board_class.place(piece)
        board_class.update_populations()
        board_class.clear_rows()

    return


if __name__ == "__main__":
    game_loop()
