from os import path
from pathlib import Path
from random import randint
from typing import Dict, Iterable, List, Tuple, Union

import numpy as np
import pygame

from . import letters
from . import sound

DIM_X: int = 155
DIM_Y: int = 120
BOUNDARY_X: int = 125
BOUNDARY_Y: int = 100
X_GAP: int = (DIM_X - BOUNDARY_X) // 2
Y_GAP: int = (DIM_Y - BOUNDARY_Y) // 2
DISP: np.ndarray = np.array((X_GAP, Y_GAP)).astype(int)

RESOLUTION: np.ndarray = np.array((DIM_X, DIM_Y))
PSEUDO_SCREEN: pygame.Surface = pygame.Surface(RESOLUTION)
SCREEN: pygame.Surface = pygame.display.set_mode(
    RESOLUTION * 8, pygame.FULLSCREEN
)
pygame.mouse.set_visible(False)

pygame.display.set_caption('Outbreak')

# The clock which keeps the frame rate consistent
CLOCK = pygame.time.Clock()

# Time passed contains the following values:
# time_passed[0] = time player has been active in game +
#     (bonus points / 10)
# time_passed[1] = time since player was caught by infected
# time_passed[2] = time since beginning of new game
time_passed: np.ndarray = np.array((0, 0, 0))

colours: Dict[str, np.ndarray] = {
    'black': 255 * np.array((0, 0, 0)),
    'red': 255 * np.array((1, 0, 0)),
    'green': 255 * np.array((0, 1, 0)),
    'blue': 255 * np.array((0, 0, 1)),
    'cyan': 255 * np.array((0, 1, 1)),
    'white': 255 * np.array((1, 1, 1)),
    'yellow': 255 * np.array((1, 1, 0)),
    'magenta': 255 * np.array((1, 0, 1))
}


class HighScores:
    """
    Reads and edits the high score file.
    """

    def __init__(self) -> None:
        """
        If the highscores.txt file is missing, the file is written.
        :return: None
        """
        self.users: List[str] = []
        self.points: List[int] = []
        self.insert_user: Union[None, str] = None
        self.insert_points: Union[None, int] = None
        self.index: int = -1

        # Creates the file if it is missing.
        if 'highscores.txt' not in Path().iterdir():
            with open('highscores.txt', 'w') as f:
                f.write(('ANON,0\n' * 10)[:-1])

        with open('highscores.txt', 'r') as f:
            # Unpacks the scores
            scores_text = list(map(str.strip, f.readlines()))
            for score_text in scores_text:
                user, points = score_text.split(',')
                self.users.append(user)
                self.points.append(int(points))

    @staticmethod
    def calculate_score(game_time: int) -> int:
        """
        Calculates the score of the user.
        :param game_time: int
            The amount of time that has passed since the game started.
        :return: int
            The score the player receives for their playing time. The
            longer they have survived, the higher the score they
            receive.
        """
        return 10 * (game_time // 100)

    def new_score(self, insert_points: int) -> None:
        """
        Finds where the new score should be placed in the high scores
        list.
        :param insert_points: int
            The number of points of the most recent score.
        :return: None
        """
        # Stops if the player got a worse score than those in the
        # highscores list.
        if insert_points <= min(self.points):
            return

        # Refreshes the name to be inserted and the number of points.
        self.insert_user = ''
        self.insert_points = insert_points

        # Sets the index to be below the next highest or equal score.
        for self.index, points in enumerate(self.points):
            if insert_points > points:
                break

    @property
    def scores(self) -> Iterable[Tuple[str, int]]:
        """
        Returns the zip of the users and points.
        :return: Iterable[Tuple[str, int]]
            The zip contains the names of the users and their
            respective scores.
        """
        return zip(self.users, self.points)

    def update_scores(self) -> None:
        """
        Writes the updated highscores to the highscores table.
        :return: None
        """
        with open('highscores.txt', 'w') as f:
            for user, points in self.scores:
                f.write(f'{user},{points}\n')


class Entity:
    """
    Base class for characters, eggs, and shockwaves.
    """

    def __init__(self, pos: np.ndarray) -> None:
        """
        Stores the position of the entity.
        :param pos: np.ndarray
            The x, y position of the entity on the screen.
        :return: None
        """
        self.pos = pos


class Character(Entity):
    """
    A character which runs about on screen.
    """

    def __init__(
            self, char_id: str, pos: Union[Tuple[int, int], np.ndarray]
    ) -> None:
        """
        Stores the data about the character.
        :param char_id: str
            The ID of the character. Can be 'Main', 'Infected', or
            'Disinfected'. 'Main' is the ID of the playable character,
            'Infected' is the ID of all characters who are infected,
            and 'Disinfected' is the ID of all non-playable characters
            who are not infected.
        :param pos: Union[Tuple[int, int], np.ndarray]
            The position of character on the screen.
        :return: None
        """
        super().__init__(np.array(pos))
        self.id: str = char_id
        self.colour: np.ndarray
        if self.id == 'Main':
            self.colour = colours['yellow']
        elif self.id == 'Infected':
            self.colour = colours['green']
        else:
            self.colour = colours['red']
        self.frame: int = -1  # -1 means the character isn't moving
        self.sprite: int = 0
        self.distract_time: int = 0
        self.caught: bool = False

        self.target: Union[None, np.ndarray]
        if self.id == 'Infected' and MAIN.caught:
            self.target = self.on_death_target()
        elif self.id in ('Main', 'Infected'):
            self.target = None
        else:
            self.target = np.array((
                randint(1, BOUNDARY_X - 3),
                randint(1, BOUNDARY_Y - 3)
            ))

    @property
    def x(self) -> int:
        """
        Returns the x position.
        :return: int
            The x position of the character.
        """
        return self.pos[0]

    @x.setter
    def x(self, x: int) -> None:
        """
        Changes the x position.
        :param x: int
            The new x position of the character.
        :return: None
        """
        self.pos[0] = x

    @property
    def y(self) -> int:
        """
        Returns the y position.
        :return: y
            The y position of the character.
        """
        return self.pos[1]

    @y.setter
    def y(self, y: int) -> None:
        """
        Changes the y position.
        :param y:
            The new y position of the character.
        :return: None
        """
        self.pos[1] = y

    def distance(self, obj: Entity) -> int:
        """
        Calculates the absolute position difference in pixels between
        two objects.
        :param obj: Entity
            The other entity with respect to which the distance is
            being measured.
        :return: int
            The absolute distance. Note that this distance is a sum in
            the x and y directions. It does not use Pythagoras'
            theorem.
        """
        return sum(abs(self.pos - obj.pos))

    def move_left(self) -> None:
        """
        Moves the character leftwards.
        :return: None
        """
        # Keeps the infected characters from bunching up.
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.x - self.x + 1) < abs(char.x - self.x) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return

        # If physically possible, moves the character left.
        if self.x - 1 > 0:
            self.x -= 1
            self.set_animate()

    def move_right(self) -> None:
        """
        Moves the character rightwards.
        :return None:
        """
        # Keeps the infected characters from bunching up.
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.x - self.x - 1) < abs(char.x - self.x) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return

        # If physically possible, moves the character right.
        if self.x + 1 < BOUNDARY_X - 2:
            self.x += 1
            self.set_animate()

    def move_up(self) -> None:
        """
        Moves the character upwards.
        :return: None
        """
        # Keeps the infected characters from bunching up.
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.y - self.y + 1) < abs(char.y - self.y) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return

        # If physically possible, moves the character up.
        if self.y - 1 > 0:
            self.y -= 1
            self.set_animate()

    def move_down(self) -> None:
        """
        Moves the character downwards.
        :return: None
        """
        # Keeps the infected characters from bunching up.
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.y - self.y - 1) < abs(char.y - self.y) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return

        # If physically possible, moves the character down.
        if self.y + 1 < BOUNDARY_Y - 2:
            self.y += 1
            self.set_animate()

    def animate(self) -> None:
        """
        Animates the character.
        :return None:
        """
        # Makes sure that the character is animating.
        if self.frame >= 0:
            self.frame += 1
            # Resets the frame number.
            if self.frame == 3:
                self.frame = 0
                self.sprite += 1
                # Resets the sprite number.
                if self.sprite == 4:
                    self.sprite = 0

    @staticmethod
    def on_death_target() -> np.ndarray:
        """
        Creates a new target in the top left of the screen when the main
        character dies.
        :return: np.ndarray
            The new target.
        """
        return np.random.uniform(1, 10, 2).astype(int)

    def new_target(self) -> None:
        """
        Create a new target.
        :return: None
        """
        self.target = np.array((
            randint(1, BOUNDARY_X - 3),
            randint(1, BOUNDARY_Y - 3)
        ))

    def move_ai(self) -> None:
        """
        Moves the non-playable character.
        :return: None
        """
        # Non-infected NPCs approach random targets
        if self.target is not None and self.frame in (-1, 1):
            if self.x > self.target[0]:
                self.move_left()
            elif self.x < self.target[0]:
                self.move_right()
            if self.y > self.target[1]:
                self.move_up()
            elif self.y < self.target[1]:
                self.move_down()
            if all(self.pos == self.target):
                if self.id != 'Infected':
                    self.new_target()
                else:
                    self.target = None

        # Infected characters chase the main character
        elif self.id == 'Infected' and self.frame in (-1, 1):
            if self.x > MAIN.x:
                self.move_left()
            elif self.x < MAIN.x:
                self.move_right()
            if self.y > MAIN.y:
                self.move_up()
            elif self.y < MAIN.y:
                self.move_down()

    def distract(self) -> None:
        """
        Occasionally, the infected characters are distracted.
        :return: None
        """
        if self.id == 'Infected' and self.target is None:
            self.distract_time += 1
            if randint(1, 6000) < self.distract_time - 20:
                self.distract_time = 0
                self.new_target()
                if len(characters) < 100 and randint(1, 10) == 1:
                    eggs.append(Egg(self.pos))
                    sound.layegg_wav.play()

    def mainloop(self) -> None:
        """
        Changes the sprite mainloop.
        :return: None
        """
        self.distract()
        self.move_ai()
        self.animate()
        self.infect()

    def set_animate(self, on: bool = True) -> None:
        """
        Sets the animation on or off.
        :param on: bool
            Whether to animate the character or not.
        :return: None
        """
        if on and self.frame == -1:
            self.frame = 0
        elif not on:
            self.frame = -1
            self.sprite = 0

    def infect(self) -> None:
        """
        Infects all surrounding NPCs.
        :return: None
        """
        infect_radius = 5
        if self.id != 'Infected':
            return

        for char in filter(
                lambda x: x.id not in ('Infected', 'Main'), characters
        ):
            if (
                    abs(char.x - self.x) < infect_radius
                    and abs(char.y - self.y) < infect_radius
            ):
                char.colour = colours['green']
                char.id = 'Infected'
                if MAIN.caught:
                    char.target = char.on_death_target()

        if (abs(MAIN.x - self.x) < infect_radius and
                abs(MAIN.y - self.y) < infect_radius and
                not MAIN.caught and
                MAIN.flash_i is None):
            for shockwave in shockwaves:
                if sum(MAIN.pos - shockwave.pos) < shockwave.radius:
                    return
            MAIN.colour = colours['green']
            MAIN.caught = True
            sound.lose_wav.play()
            for char in characters:
                if char.id == 'Infected':
                    self.distract_time = 0
                    char.target = char.on_death_target()
            high_scores.new_score(10 * int(time_passed[0] / 100))


class MainCharacter(Character):
    """
    The main character who the user controls.
    """

    def __init__(self, pos: Union[Tuple[int, int], np.ndarray]) -> None:
        super().__init__(char_id='Main', pos=pos)
        self.flash_i: Union[None, int] = None
        self.mobile: bool = False
        self.lives: int = 3

    def mainloop(self) -> None:
        """
        Same as character mainloop, except checks to revive and flash
        first.
        :return: None
        """
        self.revive()
        self.flash()
        super().mainloop()

    def revive(self) -> None:
        """
        If the main character dies, and still has lives, it can be revived.
        :return: None
        """
        if time_passed[1] == 100 and self.lives > 0:
            self.pos = np.array((90, 90))
            self.colour = colours['yellow']
            self.caught = False
            time_passed[1] = 0
            self.lives -= 1
            self.flash_i = 0

    def flash(self) -> None:
        """
        Upon revival, the main character flashes to alert the user to its
        position. During this time, the user cannot be caught.
        :return: None
        """
        if self.flash_i is not None:
            self.flash_i += 1
            if self.flash_i == 30:
                self.flash_i = None

    def visible(self) -> bool:
        """
        Returns True if the main character can be seen.
        :return: bool
            Whether the main character is visible.s
        """
        return self.flash_i is None or self.flash_i % 10 < 5


class Shockwave(Entity):
    """
    A shockwave is visibly emitted from an egg.
    """

    def __init__(self, pos: Union[Tuple[int, int], np.ndarray]) -> None:
        """
        Stores the shockwave details.
        :param pos: Union[Tuple[int, int], np.ndarray]
            The central position of the shockwave.
        :return: None
        """
        super().__init__(pos)
        self.radius: int = 1
        sound.shockwave_wav.play()

    def draw(self) -> None:
        """
        Draws the shockwave.
        :return: None
        """
        pygame.draw.lines(
            PSEUDO_SCREEN, colours['magenta'], True,
            (
                self.pos + DISP + np.array((self.radius, 0)),
                self.pos + DISP + np.array((0, self.radius)),
                self.pos + DISP + np.array((-self.radius, 0)),
                self.pos + DISP + np.array((0, -self.radius))
            )
        )

    def mainloop(self) -> None:
        """
        Runs the shockwave mainloop.
        :return: None
        """
        # Increases the shockwave size.
        self.radius += 2

        # Disinfects all infected characters within range.
        for char in characters:
            if (
                    char.id == 'Infected'
                    and char.distance(self) < self.radius
                    and len(list(filter(lambda x: x.id == 'Infected',
                                        characters))) > 1
            ):
                char.id = 'Disinfected'
                char.new_target()
                char.colour = colours['red']
                time_passed[0] += 100

        # The shockwave is removed once it has expanded sufficiently.
        if self.radius > 20:
            shockwaves.remove(self)


class Egg(Entity):
    """
    An egg hatches infected characters.
    """
    def __init__(self, pos: Union[Tuple[int, int], np.ndarray]) -> None:
        """
        Stores the egg position.
        :param pos: Union[Tuple[int, int], np.ndarray]
            The position of the egg.
        :return: None
        """
        super().__init__(pos)
        self.age: int = 0
        self.colour: np.ndarray = colours['blue']

    def mainloop(self) -> None:
        """
        Ages the egg appropriately.
        :return: None
        """
        self.age += 1
        self.flash()
        if self.age <= 200:
            self.collect()
        else:
            self.hatch()

    def hatch(self) -> None:
        """
        Hatches the egg.
        :return: none
        """
        sound.hatch_wav.play()
        eggs.remove(self)
        characters.append(Character(char_id='Infected', pos=self.pos))

    def collect(self) -> None:
        """
        If the main character picks up the egg before hatching, it disinfects
        all characters within a radius, unless all of them are within range, in
        which case, one remains infected.
        :return: None
        """
        if MAIN.distance(self) < 5 and not MAIN.caught:
            eggs.remove(self)
            shockwaves.append(Shockwave(self.pos))
            time_passed[0] += 200

    def flash(self) -> None:
        """
        The egg shortly flashes before hatching.
        :return: None
        """
        if self.age > 150 and self.age % 5 == 0:
            if self.colour is colours['blue']:
                self.colour = colours['cyan']
                sound.crack_wav.play()
            else:
                self.colour = colours['blue']


def draw_heart(pos: np.ndarray) -> None:
    """
    Draws a heart, representing a life.
    :param pos: np.ndarray
        The (x, y) position of where the heart is drawn.
    :return: None
    """
    pygame.draw.lines(PSEUDO_SCREEN, colours['red'], False, (
        pos + (0, 1),
        pos + (0, 2),
        pos + (2, 4),
        pos + (4, 2),
        pos + (4, 1),
        pos + (3, 0),
        pos + (3, 2),
        pos + (2, 3),
        pos + (1, 2),
        pos + (1, 0),
        pos + (2, 1),
        pos + (2, 2)
    ))


def draw_countdown() -> None:
    """
    Draws the countdown on screen.
    :return: None
    """
    if MAIN.mobile:
        return

    y = int(DIM_Y / 2) - 5

    if time_passed[2] < 20:
        text = '3'
    elif time_passed[2] < 40:
        text = '2'
    else:
        text = '1'

    write_centre_align(text, y=y, colour=colours['white'])


def register_objects() -> None:
    """
    Runs the mainloop.
    :return: None
    """
    if MAIN.mobile:
        for character in characters:
            character.mainloop()

        for egg in eggs:
            egg.mainloop()

        for shockwave in shockwaves:
            shockwave.mainloop()

    elif time_passed[2] > 60:
        MAIN.mobile = True


def display_objects() -> None:
    """
    Refreshes the screen.
    :return: None
    """
    # Refreshes the screen
    PSEUDO_SCREEN.fill(colours['black'])

    # Draw a border
    pygame.draw.lines(PSEUDO_SCREEN, colours['white'], True,
                      (DISP,
                       DISP + (BOUNDARY_X - 1, 0),
                       DISP + (BOUNDARY_X - 1, BOUNDARY_Y - 1),
                       DISP + (0, BOUNDARY_Y - 1)))

    # Displays the eggs
    for egg in eggs:
        size = 2 if egg.age > 100 else 1
        pygame.draw.rect(PSEUDO_SCREEN, egg.colour,
                         (DISP + egg.pos, size * np.array((1, 1))))

    # Displays the characters on the screen
    for char in characters:
        if char == MAIN and not MAIN.visible():
            continue
        pygame.draw.rect(PSEUDO_SCREEN, char.colour,
                         (DISP + char.pos, np.array((2, 2))))
        if char.sprite == 1:
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((0, -1)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((-1, 0)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((1, 2)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((2, 1)),
                                 char.colour)
        elif char.sprite == 3:
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((1, -1)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((-1, 1)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((0, 2)),
                                 char.colour)
            PSEUDO_SCREEN.set_at(DISP + char.pos + np.array((2, 0)),
                                 char.colour)

    for shockwave in shockwaves:
        shockwave.draw()

    # Draws the score at the top right
    write_right_align(str(high_scores.calculate_score(time_passed[0])), y=1,
                      size='small')

    # Draws hearts representing lives
    for heart_i in range(MAIN.lives):
        draw_heart(np.array((heart_i * 6 + 1, 1)))

    write_centre_align('OUTBREAK', y=2, size='small')

    draw_countdown()

    # Enlarges the screen
    SCREEN.blit(pygame.transform.scale(PSEUDO_SCREEN, RESOLUTION * 8), (0, 0))
    pygame.display.flip()


def write_left_align(
        text: str, *, y: int, x: int = 1,
        colour: np.ndarray = colours['green'], size: str = 'large'
) -> None:
    """
    Draws left aligned text.
    :param text: str
        The text to be written.
    :param y: int
        The y position of the upper border of the text.
    :param x: int
        The x position of the left-hand side of the text.
    :param colour: np.ndarray
        The colour of the text.
    :param size: str
        The size of the text. If large, set size to 'large'.
    :return: None
    """
    if size == 'large':
        gap = 10
        char_dict = letters.char_to_func
    else:
        gap = 6
        char_dict = letters.char_to_mini_func

    for char in text:
        char_dict[char](PSEUDO_SCREEN, np.array((x, y)), colour=colour)
        x += gap


def write_right_align(
        text: str, *, y: int, x: int = DIM_X,
        colour: np.ndarray = colours['green'], size: str = 'large'
) -> None:
    """
    Displays right aligned text.
    :param text: str
        The text to be written.
    :param y: int
        The y position of the upper border of the text.
    :param x: int
        The x position of the right-hand side of the text.
    :param colour: np.ndarray
        The colour of the text.
    :param size: str
        The size of the text. If large, set size to 'large'.
    :return: None
    """
    if size == 'large':
        gap = 10
        char_dict = letters.char_to_func
    else:
        gap = 6
        char_dict = letters.char_to_mini_func

    for char in str(text)[::-1]:
        x -= gap
        char_dict[char](PSEUDO_SCREEN, np.array((x, y)), colour=colour)


def write_centre_align(
        text: str, *, y: int, colour: np.ndarray = colours['green'],
        size: str = 'large'
) -> None:
    """
    Displays centre aligned text.
    :param text: str
        The text to be written.
    :param y: int
        The y position of the upper border of the text.
    :param colour: np.ndarray
        The colour of the text.
    :param size: str
        The size of the text. If large, set size to 'large'.
    :return: None
    """
    if size == 'large':
        gap = 10
        char_dict = letters.char_to_func
    else:
        gap = 6
        char_dict = letters.char_to_mini_func

    x = int((DIM_X - len(text) * gap) / 2)
    for char in text:
        char_dict[char](PSEUDO_SCREEN, np.array((x, y)), colour=colour)
        x += gap


def display_highscores() -> None:
    """
    Displays the highscores onto the screen.
    :return: None
    """
    PSEUDO_SCREEN.fill(colours['black'])
    write_centre_align('HIGHSCORES', y=5)
    y = 20
    for i, (user, points) in enumerate(high_scores.scores):
        if i == high_scores.index:
            write_left_align(high_scores.insert_user, y=y)
            if len(high_scores.insert_user) == 4:
                write_left_align('ENTER', y=y, x=46)
            else:
                pygame.draw.line(PSEUDO_SCREEN, colours['green'],
                                 np.array((len(
                                     high_scores.insert_user) * 10 + 1,
                                           y + 8)),
                                 np.array((len(
                                     high_scores.insert_user) * 10 + 8,
                                           y + 8)))
            y += 10
            if i == 8:
                break

        write_left_align(user, y=y)
        write_right_align(str(points), y=y)

        y += 10
        if i == 9:
            break

    # Enlarges the screen
    SCREEN.blit(pygame.transform.scale(PSEUDO_SCREEN, RESOLUTION * 8), (0, 0))
    pygame.display.flip()


def new_game() -> None:
    """
    Creates a new game.
    :return: None
    """
    time_passed[0] = 0
    time_passed[1] = 0
    time_passed[2] = 0
    MAIN.caught = False
    MAIN.colour = colours['yellow']
    MAIN.pos = np.array((90, 90))
    MAIN.lives = 3
    MAIN.mobile = False
    characters.clear()
    characters.append(MAIN)
    characters.append(Character('Infected', (10, 10)))
    for __ in range(11):
        x = randint(1, BOUNDARY_X - 3)
        y = randint(1, BOUNDARY_Y - 3)
        characters.append(Character('Disinfected', (x, y)))
    eggs.clear()
    shockwaves.clear()


def type_char(event: pygame.event.EventType) -> None:
    """
    Types a character in the credits.
    :param event: Event
        The event containing the keystroke.
    :return: None
    """
    if (high_scores.insert_user is not None and
            len(high_scores.insert_user) < 4):
        high_scores.insert_user += letters.event_to_char[event.key]


def delete_char() -> None:
    """
    Removes the last character in the credits.
    :return: None
    """
    if (high_scores.insert_user is not None and
            len(high_scores.insert_user) > 0):
        high_scores.insert_user = high_scores.insert_user[:-1]


def enter_name() -> bool:
    """
    Occurs when the user finishes typing their name and hits enter.
    :return: bool
        Whether or not the entry has been made.
    """
    if (high_scores.insert_user is not None and
            len(high_scores.insert_user) == 4):
        high_scores.users.insert(high_scores.index,
                                 high_scores.insert_user)
        high_scores.points.insert(high_scores.index,
                                  high_scores.insert_points)
        high_scores.insert_user = None
        high_scores.insert_points = None
        high_scores.index = -1
        high_scores.users.pop()
        return True
    else:
        return False


def control_main() -> None:
    """
    Moves the character appropriately.
    :return: None
    """
    pressed = pygame.key.get_pressed()
    if MAIN.mobile and not MAIN.caught:
        if pressed[pygame.K_LEFT]:
            MAIN.move_left()
        elif pressed[pygame.K_RIGHT]:
            MAIN.move_right()
        if pressed[pygame.K_UP]:
            MAIN.move_up()
        elif pressed[pygame.K_DOWN]:
            MAIN.move_down()

    if (MAIN.caught or not any((
            pressed[pygame.K_LEFT],
            pressed[pygame.K_RIGHT],
            pressed[pygame.K_UP],
            pressed[pygame.K_DOWN],
    ))):
        MAIN.set_animate(False)


def increment_time() -> None:
    """
    Adjusts the recorded time appropriately.
    :return: None
    """
    # Increases the time since the game started (for countdown purposes only)
    if not MAIN.mobile:
        time_passed[2] += 1

    # Increases the time since game started
    elif not MAIN.caught:
        time_passed[0] += 1

    # Otherwise increases the time since caught
    elif time_passed[1] <= 100:
        time_passed[1] += 1


def handle_key_down() -> None:
    """
    Handles the pressing down of a key.
    :return: None
    """
    for event in pygame.event.get():
        if (
                event.type == pygame.QUIT or
                (
                        event.type == pygame.KEYDOWN
                        and event.key == pygame.K_ESCAPE
                )
        ):
            high_scores.update_scores()
            characters.remove(MAIN)
            break
        elif (event.type == pygame.KEYDOWN and
              event.key in letters.event_to_char):
            type_char(event)
        elif (event.type == pygame.KEYDOWN and
              event.key == pygame.K_BACKSPACE):
            delete_char()
        elif (event.type == pygame.KEYDOWN and
              event.key == pygame.K_RETURN):
            if enter_name():
                continue

        if (event.type == pygame.KEYDOWN and
                event.key != pygame.K_LALT and
                event.key != pygame.K_RALT):
            if time_passed[1] >= 100 and high_scores.insert_user is None:
                new_game()
                SS.on_start_screen = True


def mainloop() -> None:
    """
    Runs the mainloop for the game.
    :return: None
    """
    handle_key_down()

    if SS.on_start_screen:
        return

    if MAIN not in characters:
        return

    control_main()
    increment_time()

    if time_passed[1] <= 100:
        register_objects()
        display_objects()
    else:
        display_highscores()

    CLOCK.tick(25)


class StartScreen:
    """
    Provides a start screen for the player.
    """
    def __init__(self) -> None:
        """
        Stores the state of being on.
        :return: None
        """
        self.flash_i: int = 0
        self.on_start_screen: bool = True

        self.start_img: pygame.Surface = pygame.image.load(path.join(
            path.dirname(path.realpath(__file__)), 'play_screen.png'
        ))

    def start_screen(self) -> None:
        """
        Introduces the game to the character.
        :return: None
        """
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.KEYDOWN and
                     event.key == pygame.K_ESCAPE)):
                high_scores.update_scores()
                characters.remove(MAIN)
                break
            elif (event.type == pygame.KEYDOWN and
                  event.key != pygame.K_LALT and
                  event.key != pygame.K_RALT):
                self.on_start_screen = False
                self.flash_i = 0
                return

        self.flash_i += 1

        PSEUDO_SCREEN.fill(colours['black'])
        PSEUDO_SCREEN.blit(self.start_img, DISP)

        if self.flash_i > 25:
            write_centre_align('PRESS ANY KEY', y=DISP[1] + 70, size='small',
                               colour=colours['white'])
            write_centre_align('TO START', y=DISP[1] + 76, size='small',
                               colour=colours['white'])
            if self.flash_i > 50:
                self.flash_i = 0

        SCREEN.blit(pygame.transform.scale(PSEUDO_SCREEN, RESOLUTION * 8),
                    (0, 0))
        pygame.display.flip()

        CLOCK.tick(25)


SS: StartScreen = StartScreen()
MAIN: MainCharacter = MainCharacter((90, 90))
characters: List[Character] = []
eggs: List[Egg] = []
shockwaves: List[Shockwave] = []

new_game()

high_scores: HighScores = HighScores()

try:
    while MAIN in characters:
        if SS.on_start_screen:
            SS.start_screen()
        else:
            mainloop()
finally:
    pygame.display.quit()
    pygame.quit()
