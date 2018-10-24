import numpy as np
import pygame

green = np.array((0, 255, 0))

def draw_a(surface, pos):
    '''
    Draws the letter 'a'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))

def draw_b(surface, pos):
    '''
    Draws the letter 'b'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 1)), pos + np.array((6, 3)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 5)), pos + np.array((6, 7)))

def draw_c(surface, pos):
    '''
    Draws the letter 'c'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 1)), pos + np.array((0, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), green)
    surface.set_at(pos + np.array((6, 7)), green)

def draw_d(surface, pos):
    '''
    Draws the letter 'd'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), green)
    surface.set_at(pos + np.array((6, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((7, 2)), pos + np.array((7, 6)))

def draw_e(surface, pos):
    '''
    Draws the letter 'e'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 8)), pos + np.array((7, 8)))

def draw_f(surface, pos):
    '''
    Draws the letter 'f'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))

def draw_g(surface, pos):
    '''
    Draws the letter 'g'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 1)), pos + np.array((0, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), green)
    surface.set_at(pos + np.array((6, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((5, 6)), pos + np.array((7, 6)))

def draw_h(surface, pos):
    '''
    Draws the letter 'h'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))

def draw_i(surface, pos):
    '''
    Draws the letter 'i'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 1)), pos + np.array((4, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_j(surface, pos):
    '''
    Draws the letter 'j'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((8, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 1)), pos + np.array((5, 6)))
    surface.set_at(pos + np.array((4, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((3, 8)), pos + np.array((1, 6)))

def draw_k(surface, pos):
    '''
    Draws the letter 'k'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    surface.set_at(pos + np.array((2, 4)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((3, 4)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 5)), pos + np.array((7, 8)))

def draw_l(surface, pos):
    '''
    Draws the letter 'l'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_m(surface, pos):
    '''
    Draws the letter 'm'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((0, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((4, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 0)), pos + np.array((7, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 3)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 5)), pos + np.array((5, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 0)), pos + np.array((8, 8)))

def draw_n(surface, pos):
    '''
    Draws the letter 'n'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))

def draw_o(surface, pos):
    '''
    Draws the letter 'o'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((1, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((8, 2)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((7, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((0, 2)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), green)

def draw_p(surface, pos):
    '''
    Draws the letter 'p'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 5)), pos + np.array((5, 5)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 4)), pos + np.array((7, 3)))

def draw_q(surface, pos):
    '''
    Draws the letter 'q'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((1, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((8, 2)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 6)), pos + np.array((8, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 2)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), green)

def draw_r(surface, pos):
    '''
    Draws the letter 'r'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 5)), pos + np.array((5, 5)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 4)), pos + np.array((7, 3)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 5)), pos + np.array((7, 8)))

def draw_s(surface, pos):
    '''
    Draws the letter 's'.
    '''
    surface.set_at(pos + np.array((7, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 1)), pos + np.array((1, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 3)), pos + np.array((3, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 5)), pos + np.array((7, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((1, 7)), green)

def draw_t(surface, pos):
    '''
    Draws the letter 't'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 1)), pos + np.array((4, 8)))

def draw_u(surface, pos):
    '''
    Draws the letter 'u'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((1, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 0)), pos + np.array((7, 7)))

def draw_v(surface, pos):
    '''
    Draws the letter 'v'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((4, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 7)), pos + np.array((5, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 5)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 3)), pos + np.array((7, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 1)), pos + np.array((8, 0)))

def draw_w(surface, pos):
    '''
    Draws the letter 'w'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((0, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 7)), pos + np.array((2, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((3, 7)), pos + np.array((4, 6)))
    surface.set_at(pos + np.array((4, 5)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((5, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 7)), pos + np.array((8, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 5)), pos + np.array((8, 0)))

def draw_x(surface, pos):
    '''
    Draws the letter 'x'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((8, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 0)), pos + np.array((0, 8)))

def draw_y(surface, pos):
    '''
    Draws the letter 'y'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((4, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 3)), pos + np.array((8, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((4, 5)), pos + np.array((4, 8)))

def draw_z(surface, pos):
    '''
    Draws the letter 'z'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 1)), pos + np.array((1, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))

def draw_1(surface, pos):
    '''
    Draws the digit '1'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((4, 0)), pos + np.array((4, 7)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 1)), pos + np.array((3, 0)))

def draw_2(surface, pos):
    '''
    Draws the digit '2'.
    '''
    surface.set_at(pos + np.array((0, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((7, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((8, 2)), pos + np.array((0, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 8)), pos + np.array((8, 8)))

def draw_3(surface, pos):
    '''
    Draws the digit '3'.
    '''
    surface.set_at(pos + np.array((1, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((7, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((8, 2)), pos + np.array((8, 3)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 4)), pos + np.array((7, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 5)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((6, 8)), pos + np.array((2, 8)))
    surface.set_at(pos + np.array((1, 7)), green)

def draw_4(surface, pos):
    '''
    Draws the digit '4'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((5, 0)), pos + np.array((5, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 4)), pos + np.array((4, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 4)), pos + np.array((8, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((0, 3)))

def draw_5(surface, pos):
    '''
    Draws the digit '5'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((0, 0)), pos + np.array((8, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 1)), pos + np.array((0, 3)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 3)), pos + np.array((4, 3)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 5)), pos + np.array((8, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 7)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 8)), pos + np.array((5, 8)))

def draw_6(surface, pos):
    '''
    Draws the digit '6'.
    '''
    surface.set_at(pos + np.array((8, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 1)), pos + np.array((0, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((0, 3)), pos + np.array((0, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 7)), pos + np.array((2, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((3, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 7)), pos + np.array((8, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((8, 5)), pos + np.array((7, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 3)), pos + np.array((2, 3)))
    surface.set_at(pos + np.array((1, 4)), green)

def draw_7(surface, pos):
    '''
    Draws the digit '7'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 1)), pos + np.array((4, 8)))

def draw_8(surface, pos):
    '''
    Draws the digit '8'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((2, 0)), pos + np.array((6, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 1)), pos + np.array((0, 2)))
    surface.set_at(pos + np.array((1, 3)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((7, 1)), pos + np.array((8, 2)))
    surface.set_at(pos + np.array((7, 3)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 5)), pos + np.array((0, 6)))
    surface.set_at(pos + np.array((1, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((7, 5)), pos + np.array((8, 6)))
    surface.set_at(pos + np.array((7, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))

def draw_9(surface, pos):
    '''
    Draws the digit '9'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((3, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 1)), pos + np.array((1, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 1)), pos + np.array((7, 2)))
    pygame.draw.line(surface, green,
                     pos + np.array((1, 3)), pos + np.array((2, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 3)), pos + np.array((6, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((3, 4)), pos + np.array((5, 4)))
    pygame.draw.line(surface, green,
                     pos + np.array((7, 4)), pos + np.array((7, 5)))
    pygame.draw.line(surface, green,
                     pos + np.array((6, 6)), pos + np.array((6, 8)))

def draw_0(surface, pos):
    '''
    Draws the digit '0'.
    '''
    pygame.draw.line(surface, green,
                     pos + np.array((3, 0)), pos + np.array((5, 0)))
    surface.set_at(pos + np.array((2, 1)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((7, 2)), pos + np.array((7, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((5, 8)), pos + np.array((3, 8)))
    surface.set_at(pos + np.array((6, 7)), green)
    pygame.draw.line(surface, green,
                     pos + np.array((1, 2)), pos + np.array((1, 6)))
    pygame.draw.line(surface, green,
                     pos + np.array((2, 7)), pos + np.array((6, 1)))
    surface.set_at(pos + np.array((2, 7)), green)

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
