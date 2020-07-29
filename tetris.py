import pygame
import board as bd
import piece as pc

BLOCK_SIZE = 25

pygame.init()
# (0,0) is the top left corner of the screen
screen = pygame.display.set_mode((10*BLOCK_SIZE, 21*BLOCK_SIZE))
# board and piece surface are responsible for drawing their own components
# and updating when need be
board_surface = pygame.Surface((10*BLOCK_SIZE, 21*BLOCK_SIZE))

""" (0,0) on the board is the top left corner
    This is to simplify the process of printing the board onto a surface """
sample_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

board_class = bd.Board(sample_board)

""" Body arrays are vertically inverted due to the inversion of the game board """
t_bodies = [
    [
        [0, 0, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 0],
        [0, 1, 0]
    ]
]


def draw_stdout():
    for j in range(board_class.height):
        for i in range(board_class.width):
            if board_class.board[j][i] != 0:
                print(board_class.board[j][i], end=" ")
            else:
                print(" ", end=" ")
        print("\n")


def draw_board():
    for j in range(board_class.height):
        for i in range(board_class.width):
            if board_class.board[j][i] != 0:
                pygame.draw.rect(board_surface, (255, 255, 255),
                                 (i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def draw_piece(piece: pc.Piece, piece_surface: pygame.Surface):
    for j in range(len(piece.currentBody)):
        for i in range(len(piece.currentBody[0])):
            if piece.currentBody[j][i] != 0:
                pygame.draw.rect(piece_surface, (255, 255, 255),
                                 ((piece.x * BLOCK_SIZE) + (i * BLOCK_SIZE),
                                  ((piece.y * BLOCK_SIZE) + (j * BLOCK_SIZE)),
                                  BLOCK_SIZE, BLOCK_SIZE))


def game_loop():
    playing = True
    speed = 1
    maxfps = 30

    dontburn = pygame.time.Clock()

    while playing:

        # create new piece here
        t_piece = pc.Piece(6, t_bodies, 3, 10)

        falling = True
        while falling:
            # establish background
            screen.fill((0, 0, 0))
            # create black piece surface
            piece_surface = pygame.Surface((10 * BLOCK_SIZE, 21 * BLOCK_SIZE))

            # drop piece according to speed
            if board_class.drop_check(t_piece):
                t_piece.drop(speed)
            else:
                falling = False

            # draw board and then piece
            draw_board()
            draw_piece(t_piece, piece_surface)
            # blit board and then piece
            screen.blit(board_surface, (0, 0))
            screen.blit(piece_surface, (0, 0))
            # update display
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and board_class.move_check_left(t_piece):
                        t_piece.move_left()
                    elif event.key == pygame.K_d and board_class.move_check_right(t_piece):
                        t_piece.move_right()
                    elif event.key == pygame.K_s:
                        t_piece.rotate_right()
                    elif event.key == pygame.K_w:
                        t_piece.rotate_left()

            piece_surface.fill((0, 0, 0, 0))
            dontburn.tick(30)

        board_class.place(t_piece)

    return


if __name__ == "__main__":
    game_loop()
