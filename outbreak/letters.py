import numpy as np
import pygame

green = np.array((0, 255, 0))

def draw_a(surface, pos, colour=green):
    """
    Draws the letter 'a'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))

def draw_b(surface, pos, colour=green):
    """
    Draws the letter 'b'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 1)), pos + np.array((6, 3)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 5)), pos + np.array((6, 7)))

def draw_c(surface, pos, colour=green):
    """
    Draws the letter 'c'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 1)), pos + np.array((0, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), colour)
    surface.set_at(pos + np.array((6, 7)), colour)

def draw_d(surface, pos, colour=green):
    """
    Draws the letter 'd'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), colour)
    surface.set_at(pos + np.array((6, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 2)), pos + np.array((7, 6)))

def draw_e(surface, pos, colour=green):
    """
    Draws the letter 'e'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((7, 8)))

def draw_f(surface, pos, colour=green):
    """
    Draws the letter 'f'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))

def draw_g(surface, pos, colour=green):
    """
    Draws the letter 'g'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 1)), pos + np.array((0, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), colour)
    surface.set_at(pos + np.array((6, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 6)), pos + np.array((7, 6)))

def draw_h(surface, pos, colour=green):
    """
    Draws the letter 'h'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))

def draw_i(surface, pos, colour=green):
    """
    Draws the letter 'i'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 1)), pos + np.array((4, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_j(surface, pos, colour=green):
    """
    Draws the letter 'j'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((8, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 1)), pos + np.array((5, 6)))
    surface.set_at(pos + np.array((4, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 8)), pos + np.array((1, 6)))

def draw_k(surface, pos, colour=green):
    """
    Draws the letter 'k'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    surface.set_at(pos + np.array((2, 4)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 4)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 5)), pos + np.array((7, 8)))

def draw_l(surface, pos, colour=green):
    """
    Draws the letter 'l'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_m(surface, pos, colour=green):
    """
    Draws the letter 'm'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((0, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((4, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 3)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 5)), pos + np.array((5, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 0)), pos + np.array((8, 8)))

def draw_n(surface, pos, colour=green):
    """
    Draws the letter 'n'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))

def draw_o(surface, pos, colour=green):
    """
    Draws the letter 'o'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((1, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 2)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((7, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 2)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), colour)

def draw_p(surface, pos, colour=green):
    """
    Draws the letter 'p'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 5)), pos + np.array((5, 5)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 4)), pos + np.array((7, 3)))

def draw_q(surface, pos, colour=green):
    """
    Draws the letter 'q'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((1, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 2)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 6)), pos + np.array((8, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 2)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), colour)

def draw_r(surface, pos, colour=green):
    """
    Draws the letter 'r'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 5)), pos + np.array((5, 5)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 4)), pos + np.array((7, 3)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 5)), pos + np.array((7, 8)))

def draw_s(surface, pos, colour=green):
    """
    Draws the letter 's'.
    """
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 1)), pos + np.array((1, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 3)), pos + np.array((3, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 5)), pos + np.array((7, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((1, 7)), colour)

def draw_t(surface, pos, colour=green):
    """
    Draws the letter 't'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 1)), pos + np.array((4, 8)))

def draw_u(surface, pos, colour=green):
    """
    Draws the letter 'u'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 7)))

def draw_v(surface, pos, colour=green):
    """
    Draws the letter 'v'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((4, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 7)), pos + np.array((5, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 5)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 3)), pos + np.array((7, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 1)), pos + np.array((8, 0)))

def draw_w(surface, pos, colour=green):
    """
    Draws the letter 'w'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((0, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 7)), pos + np.array((2, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 7)), pos + np.array((4, 6)))
    surface.set_at(pos + np.array((4, 5)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 7)), pos + np.array((8, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 5)), pos + np.array((8, 0)))

def draw_x(surface, pos, colour=green):
    """
    Draws the letter 'x'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((8, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 0)), pos + np.array((0, 8)))

def draw_y(surface, pos, colour=green):
    """
    Draws the letter 'y'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((4, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 3)), pos + np.array((8, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 5)), pos + np.array((4, 8)))

def draw_z(surface, pos, colour=green):
    """
    Draws the letter 'z'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 1)), pos + np.array((1, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_1(surface, pos, colour=green):
    """
    Draws the digit '1'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 0)), pos + np.array((4, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 1)), pos + np.array((3, 0)))

def draw_2(surface, pos, colour=green):
    """
    Draws the digit '2'.
    """
    surface.set_at(pos + np.array((0, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 2)), pos + np.array((0, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((8, 8)))

def draw_3(surface, pos, colour=green):
    """
    Draws the digit '3'.
    """
    surface.set_at(pos + np.array((1, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 2)), pos + np.array((8, 3)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 4)), pos + np.array((7, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 5)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((1, 7)), colour)

def draw_4(surface, pos, colour=green):
    """
    Draws the digit '4'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 0)), pos + np.array((5, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 4)), pos + np.array((4, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 4)), pos + np.array((8, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((0, 3)))

def draw_5(surface, pos, colour=green):
    """
    Draws the digit '5'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((8, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 1)), pos + np.array((0, 3)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 3)), pos + np.array((4, 3)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 5)), pos + np.array((8, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 8)), pos + np.array((5, 8)))

def draw_6(surface, pos, colour=green):
    """
    Draws the digit '6'.
    """
    surface.set_at(pos + np.array((8, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 1)), pos + np.array((0, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 3)), pos + np.array((0, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 7)), pos + np.array((2, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 7)), pos + np.array((8, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 5)), pos + np.array((7, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 3)), pos + np.array((2, 3)))
    surface.set_at(pos + np.array((1, 4)), colour)

def draw_7(surface, pos, colour=green):
    """
    Draws the digit '7'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 1)), pos + np.array((4, 8)))

def draw_8(surface, pos, colour=green):
    """
    Draws the digit '8'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 1)), pos + np.array((0, 2)))
    surface.set_at(pos + np.array((1, 3)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 1)), pos + np.array((8, 2)))
    surface.set_at(pos + np.array((7, 3)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 5)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 5)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))

def draw_9(surface, pos, colour=green):
    """
    Draws the digit '9'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 1)), pos + np.array((1, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 3)), pos + np.array((2, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 3)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 4)), pos + np.array((7, 5)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 6)), pos + np.array((6, 8)))

def draw_0(surface, pos, colour=green):
    """
    Draws the digit '0'.
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 0)), pos + np.array((5, 0)))
    surface.set_at(pos + np.array((2, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 2)), pos + np.array((7, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 8)), pos + np.array((3, 8)))
    surface.set_at(pos + np.array((6, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 2)), pos + np.array((1, 6)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 7)), pos + np.array((6, 1)))
    surface.set_at(pos + np.array((2, 7)), colour)

def draw_a_mini(surface, pos, colour=green):
    """
    Draws a small letter 'A'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 2),
                       pos + (2, 2),
                       pos + (1, 1),
                       pos + (2, 0),
                       pos + (3, 1),
                       pos + (3, 2),
                       pos + (4, 2),
                       pos + (4, 4)))

def draw_b_mini(surface, pos, colour=green):
    """
    Draws a small letter 'B'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 2),
                       pos + (0, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (3, 2),
                       pos + (1, 2),
                       pos + (0, 1),
                       pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1)))

def draw_c_mini(surface, pos, colour=green):
    """
    Draws a small letter 'C'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (4, 4)))

def draw_d_mini(surface, pos, colour=green):
    """
    Draws a small letter 'D'
    """
    pygame.draw.lines(surface, colour, True,
                      (pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))

def draw_e_mini(surface, pos, colour=green):
    """
    Draws a small letter 'E'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 4),
                       pos + (4, 4)))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (4, 2))

def draw_f_mini(surface, pos, colour=green):
    """
    Draws a small letter 'F'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 4)))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (3, 2))

def draw_g_mini(surface, pos, colour=green):
    """
    Draws a small letter 'G'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 2),
                       pos + (3, 2)))

def draw_h_mini(surface, pos, colour=green):
    """
    Draws a small letter 'H'
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (0, 4))
    pygame.draw.line(surface, colour, pos + (4, 0), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (4, 2))

def draw_i_mini(surface, pos, colour=green):
    """
    Draws a small letter 'I'
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 0))
    pygame.draw.line(surface, colour, pos + (0, 4), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (2, 1), pos + (2, 4))

def draw_j_mini(surface, pos, colour=green):
    """
    Draws a small letter 'J'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (3, 1),
                       pos + (3, 3),
                       pos + (2, 4),
                       pos + (1, 4),
                       pos + (0, 3)))

def draw_k_mini(surface, pos, colour=green):
    """
    Draws a small letter 'K'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (0, 2),
                       pos + (0, 4)))
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (2, 2),
                       pos + (4, 4)))

def draw_l_mini(surface, pos, colour=green):
    """
    Draws a small letter 'L'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 4),
                       pos + (4, 4)))

def draw_m_mini(surface, pos, colour=green):
    """
    Draws a small letter 'M'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 1),
                       pos + (1, 0),
                       pos + (2, 1),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (4, 4)))
    pygame.draw.line(surface, colour, pos + (2, 2), pos + (2, 4))

def draw_n_mini(surface, pos, colour=green):
    """
    Draws a small letter 'N'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 0),
                       pos + (1, 0),
                       pos + (1, 1),
                       pos + (3, 3),
                       pos + (3, 4),
                       pos + (4, 4),
                       pos + (4, 0)))

def draw_o_mini(surface, pos, colour=green):
    """
    Draws a small letter 'O'
    """
    pygame.draw.lines(surface, colour, True,
                      (pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 1),
                       pos + (3, 0)))

def draw_p_mini(surface, pos, colour=green):
    """
    Draws a small letter 'P'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (1, 2)))

def draw_q_mini(surface, pos, colour=green):
    """
    Draws a small letter 'Q'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (2, 2),
                       pos + (4, 4),
                       pos + (1, 4),
                       pos + (0, 3),
                       pos + (0, 1),
                       pos + (1, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (4, 3)))

def draw_r_mini(surface, pos, colour=green):
    """
    Draws a small letter 'R'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (3, 3),
                       pos + (4, 4)))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (2, 2))

def draw_s_mini(surface, pos, colour=green):
    """
    Draws a small letter 'S'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (3, 2),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))

def draw_t_mini(surface, pos, colour=green):
    """
    Draws a small letter 'T'
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 0))
    pygame.draw.line(surface, colour, pos + (2, 1), pos + (2, 4))

def draw_u_mini(surface, pos, colour=green):
    """
    Draws a small letter 'U'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 0)))

def draw_v_mini(surface, pos, colour=green):
    """
    Draws a small letter 'V'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (1, 3),
                       pos + (2, 4),
                       pos + (3, 3),
                       pos + (3, 2),
                       pos + (4, 1),
                       pos + (4, 0)))

def draw_w_mini(surface, pos, colour=green):
    """
    Draws a small letter 'W'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (2, 3),
                       pos + (2, 2)))
    pygame.draw.lines(surface, colour, False,
                      (pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 0)))

def draw_x_mini(surface, pos, colour=green):
    """
    Draws a small letter 'X'
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (4, 0), pos + (3, 1))
    pygame.draw.line(surface, colour, pos + (1, 3), pos + (0, 4))

def draw_y_mini(surface, pos, colour=green):
    """
    Draws a small letter 'Y'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (2, 2),
                       pos + (4, 0)))
    pygame.draw.line(surface, colour, pos + (2, 3), pos + (2, 4))

def draw_z_mini(surface, pos, colour=green):
    """
    Draws a small letter 'Z'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (0, 4),
                       pos + (4, 4)))

def draw_1_mini(surface, pos, colour=green):
    """
    Draws a small digit '1'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 1),
                       pos + (1, 0),
                       pos + (2, 0),
                       pos + (2, 3)))
    pygame.draw.line(surface, colour, pos + (0, 4), pos + (4, 4))

def draw_2_mini(surface, pos, colour=green):
    """
    Draws a small digit '2'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (1, 2),
                       pos + (0, 3),
                       pos + (0, 4),
                       pos + (4, 4)))

def draw_3_mini(surface, pos, colour=green):
    """
    Draws a small digit '3'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))
    pygame.draw.line(surface, colour, pos + (0, 2), pos + (2, 2))

def draw_4_mini(surface, pos, colour=green):
    """
    Draws a small digit '4'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 2),
                       pos + (4, 2),
                       pos + (3, 3),
                       pos + (3, 4)))
    pygame.draw.line(surface, colour, pos + (3, 0), pos + (3, 1))

def draw_5_mini(surface, pos, colour=green):
    """
    Draws a small digit '5'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 2),
                       pos + (3, 2),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))

def draw_6_mini(surface, pos, colour=green):
    """
    Draws a small digit '6'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (3, 2),
                       pos + (1, 2)))

def draw_7_mini(surface, pos, colour=green):
    """
    Draws a small digit '7'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (3, 3),
                       pos + (2, 4)))

def draw_8_mini(surface, pos, colour=green):
    """
    Draws a small digit '8'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 1),
                       pos + (3, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (3, 2),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (1, 4),
                       pos + (0, 3)))

def draw_9_mini(surface, pos, colour=green):
    """
    Draws a small digit '9'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 1),
                       pos + (3, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (4, 2),
                       pos + (4, 4)))

def draw_0_mini(surface, pos, colour=green):
    """
    Draws a small digit '0'
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (3, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 1),
                       pos + (3, 1),
                       pos + (1, 3)))

def draw_nothing(surface, pos, colour=green):
    """
    Doesn't draw anything. Used for space bars.
    """

char_to_func = {
    'A': draw_a,
    'B': draw_b,
    'C': draw_c,
    'D': draw_d,
    'E': draw_e,
    'F': draw_f,
    'G': draw_g,
    'H': draw_h,
    'I': draw_i,
    'J': draw_j,
    'K': draw_k,
    'L': draw_l,
    'M': draw_m,
    'N': draw_n,
    'O': draw_o,
    'P': draw_p,
    'Q': draw_q,
    'R': draw_r,
    'S': draw_s,
    'T': draw_t,
    'U': draw_u,
    'V': draw_v,
    'W': draw_w,
    'X': draw_x,
    'Y': draw_y,
    'Z': draw_z,
    '1': draw_1,
    '2': draw_2,
    '3': draw_3,
    '4': draw_4,
    '5': draw_5,
    '6': draw_6,
    '7': draw_7,
    '8': draw_8,
    '9': draw_9,
    '0': draw_0,
    ' ': draw_nothing,
    }

char_to_mini_func = {
    'A': draw_a_mini,
    'B': draw_b_mini,
    'C': draw_c_mini,
    'D': draw_d_mini,
    'E': draw_e_mini,
    'F': draw_f_mini,
    'G': draw_g_mini,
    'H': draw_h_mini,
    'I': draw_i_mini,
    'J': draw_j_mini,
    'K': draw_k_mini,
    'L': draw_l_mini,
    'M': draw_m_mini,
    'N': draw_n_mini,
    'O': draw_o_mini,
    'P': draw_p_mini,
    'Q': draw_q_mini,
    'R': draw_r_mini,
    'S': draw_s_mini,
    'T': draw_t_mini,
    'U': draw_u_mini,
    'V': draw_v_mini,
    'W': draw_w_mini,
    'X': draw_x_mini,
    'Y': draw_y_mini,
    'Z': draw_z_mini,
    '1': draw_1_mini,
    '2': draw_2_mini,
    '3': draw_3_mini,
    '4': draw_4_mini,
    '5': draw_5_mini,
    '6': draw_6_mini,
    '7': draw_7_mini,
    '8': draw_8_mini,
    '9': draw_9_mini,
    '0': draw_0_mini,
    ' ': draw_nothing,
    }

event_to_char = {
    pygame.K_a: 'A',
    pygame.K_b: 'B',
    pygame.K_c: 'C',
    pygame.K_d: 'D',
    pygame.K_e: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_i: 'I',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_m: 'M',
    pygame.K_n: 'N',
    pygame.K_o: 'O',
    pygame.K_p: 'P',
    pygame.K_q: 'Q',
    pygame.K_r: 'R',
    pygame.K_s: 'S',
    pygame.K_t: 'T',
    pygame.K_u: 'U',
    pygame.K_v: 'V',
    pygame.K_w: 'W',
    pygame.K_x: 'X',
    pygame.K_y: 'Y',
    pygame.K_z: 'Z',
    }
