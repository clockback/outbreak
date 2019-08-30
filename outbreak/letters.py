import numpy as np
import pygame
from typing import Callable, Dict

green: np.ndarray = np.array((0, 255, 0))


def draw_a(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'a'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 8)), pos + np.array((4, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))


def draw_b(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'b'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_c(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'c'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 1)), pos + np.array((0, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((5, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((5, 8)))
    surface.set_at(pos + np.array((6, 1)), colour)
    surface.set_at(pos + np.array((6, 7)), colour)


def draw_d(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'd'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_e(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'e'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((7, 8)))


def draw_f(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'f'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((7, 4)))


def draw_g(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'g'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_h(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'h'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 4)), pos + np.array((6, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))


def draw_i(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'i'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 1)), pos + np.array((4, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))


def draw_j(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'j'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((8, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 1)), pos + np.array((5, 6)))
    surface.set_at(pos + np.array((4, 7)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 8)), pos + np.array((1, 6)))


def draw_k(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'k'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    surface.set_at(pos + np.array((2, 4)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((3, 4)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 5)), pos + np.array((7, 8)))


def draw_l(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'l'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))


def draw_m(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'm'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_n(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'n'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 0)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 8)))


def draw_o(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'o'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_p(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'p'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_q(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'q'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_r(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'r'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_s(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 's'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_t(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 't'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 1)), pos + np.array((4, 8)))


def draw_u(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'u'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((1, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 0)), pos + np.array((7, 7)))


def draw_v(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'v'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_w(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'w'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_x(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'x'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((8, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 0)), pos + np.array((0, 8)))


def draw_y(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'y'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((4, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 3)), pos + np.array((8, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 5)), pos + np.array((4, 8)))


def draw_z(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the letter 'z'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 1)), pos + np.array((1, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((7, 8)))


def draw_1(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '1'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((4, 0)), pos + np.array((4, 7)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 8)), pos + np.array((6, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((2, 1)), pos + np.array((3, 0)))


def draw_2(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '2'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    surface.set_at(pos + np.array((0, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((6, 0)))
    surface.set_at(pos + np.array((7, 1)), colour)
    pygame.draw.line(surface, colour,
                     pos + np.array((8, 2)), pos + np.array((0, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 8)), pos + np.array((8, 8)))


def draw_3(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '3'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_4(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '4'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((5, 0)), pos + np.array((5, 8)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 4)), pos + np.array((4, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((6, 4)), pos + np.array((8, 4)))
    pygame.draw.line(surface, colour,
                     pos + np.array((0, 0)), pos + np.array((0, 3)))


def draw_5(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '5'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_6(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '6'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_7(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '7'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour,
                     pos + np.array((1, 0)), pos + np.array((7, 0)))
    pygame.draw.line(surface, colour,
                     pos + np.array((7, 1)), pos + np.array((4, 8)))


def draw_8(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '8'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_9(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '9'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_0(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws the digit '0'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_a_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'A'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_b_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'B'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_c_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'C'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (4, 4)))


def draw_d_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'D'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, True,
                      (pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))


def draw_e_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'E'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 4),
                       pos + (4, 4)))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (4, 2))


def draw_f_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'F'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 4)))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (3, 2))


def draw_g_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'G'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_h_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'H'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (0, 4))
    pygame.draw.line(surface, colour, pos + (4, 0), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (1, 2), pos + (4, 2))


def draw_i_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'I'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 0))
    pygame.draw.line(surface, colour, pos + (0, 4), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (2, 1), pos + (2, 4))


def draw_j_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'J'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (3, 1),
                       pos + (3, 3),
                       pos + (2, 4),
                       pos + (1, 4),
                       pos + (0, 3)))


def draw_k_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'K'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_l_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'L'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 4),
                       pos + (4, 4)))


def draw_m_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'M'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_n_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'N'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_o_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'O'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_p_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'P'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 4),
                       pos + (0, 0),
                       pos + (3, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (1, 2)))


def draw_q_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'Q'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_r_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'R'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_s_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'S'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_t_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'T'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 0))
    pygame.draw.line(surface, colour, pos + (2, 1), pos + (2, 4))


def draw_u_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'U'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 3),
                       pos + (1, 4),
                       pos + (3, 4),
                       pos + (4, 3),
                       pos + (4, 0)))


def draw_v_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'V'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_w_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'W'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_x_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'X'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.line(surface, colour, pos + (0, 0), pos + (4, 4))
    pygame.draw.line(surface, colour, pos + (4, 0), pos + (3, 1))
    pygame.draw.line(surface, colour, pos + (1, 3), pos + (0, 4))


def draw_y_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'Y'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (2, 2),
                       pos + (4, 0)))
    pygame.draw.line(surface, colour, pos + (2, 3), pos + (2, 4))


def draw_z_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small letter 'Z'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (0, 4),
                       pos + (4, 4)))


def draw_1_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '1'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 1),
                       pos + (1, 0),
                       pos + (2, 0),
                       pos + (2, 3)))
    pygame.draw.line(surface, colour, pos + (0, 4), pos + (4, 4))


def draw_2_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '2'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_3_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '3'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_4_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '4'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (0, 2),
                       pos + (4, 2),
                       pos + (3, 3),
                       pos + (3, 4)))
    pygame.draw.line(surface, colour, pos + (3, 0), pos + (3, 1))


def draw_5_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '5'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 0),
                       pos + (0, 0),
                       pos + (0, 2),
                       pos + (3, 2),
                       pos + (4, 3),
                       pos + (3, 4),
                       pos + (0, 4)))


def draw_6_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '6'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_7_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '7'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (0, 0),
                       pos + (4, 0),
                       pos + (4, 1),
                       pos + (3, 2),
                       pos + (3, 3),
                       pos + (2, 4)))


def draw_8_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '8'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_9_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '9'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
    """
    pygame.draw.lines(surface, colour, False,
                      (pos + (4, 1),
                       pos + (3, 0),
                       pos + (1, 0),
                       pos + (0, 1),
                       pos + (1, 2),
                       pos + (4, 2),
                       pos + (4, 4)))


def draw_0_mini(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Draws a small digit '0'.
    :param surface: pygame.Surface
        The surface on which to draw.
    :param pos: np.ndarray
        The position of the character to draw.
    :param colour: np.ndarray
        The colour of the character to draw.
    :return: None
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


def draw_nothing(
        surface: pygame.Surface, pos: np.ndarray, colour: np.ndarray = green
) -> None:
    """
    Doesn't draw anything. Used for space bars.
    """


char_to_func: Dict[str, Callable[
    [pygame.Surface, np.ndarray, np.ndarray], None
]] = {
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

char_to_mini_func: Dict[str, Callable[
    [pygame.Surface, np.ndarray, np.ndarray], None
]] = {
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

event_to_char: Dict[str, Callable[
    [pygame.Surface, np.ndarray, np.ndarray], None
]] = {
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
