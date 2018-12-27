from os import listdir, path
from random import randint

import numpy as np
import pygame

from . import letters
from . import sound

DIM_X, DIM_Y = 155, 120
BOUNDARY_X, BOUNDARY_Y = 125, 100
X_GAP = (DIM_X - BOUNDARY_X) / 2
Y_GAP = (DIM_Y - BOUNDARY_Y) / 2
DISP = np.array((X_GAP, Y_GAP)).astype(int)

RESOLUTION = np.array((DIM_X, DIM_Y))
PSEUDO_SCREEN = pygame.Surface(RESOLUTION)
SCREEN = pygame.display.set_mode(RESOLUTION * 8)#pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

pygame.display.set_caption('Outbreak')

CLOCK = pygame.time.Clock()

# Time passed contains the following values:
# time_passed[0] = time player has been active in game + (bonus points / 10)
# time_passed[1] = time since player was caught by infected
# time_passed[2] = time since beginning of new game
time_passed = np.array((0, 0, 0))

colours = {
    'black': 255 * np.array((0, 0, 0)),
    'red': 255 * np.array((1, 0, 0)),
    'green': 255 * np.array((0, 1, 0)),
    'blue': 255 * np.array((0, 0, 1)),
    'cyan': 255 * np.array((0, 1, 1)),
    'white': 255 * np.array((1, 1, 1)),
    'yellow': 255 * np.array((1, 1, 0)),
    'magenta': 255 * np.array((1, 0, 1))
    }

class HighScores():
    '''
    Reads and edits the high score file.
    '''
    def __init__(self):
        '''
        If the highscores.txt file is missing, the file is written.
        '''
        self.users = []
        self.points = []
        self.insert_user = None
        self.insert_points = None
        self.index = -1
        
        # Creates the file if it is missing.
        if 'highscores.txt' not in listdir():
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
    def calculate_score(game_time):
        '''
        Calculates the score of the user.
        '''
        return 10 * int(game_time / 100)
    
    def new_score(self, insert_points):
        '''
        Records the new score.
        '''
        if insert_points <= min(self.points):
            return
        
        self.insert_user = ''
        self.insert_points = insert_points
        for self.index, points in enumerate(self.points):
            if insert_points > points:
                break
    
    @property
    def scores(self):
        '''
        Returns the zip of the users and points.
        '''
        return zip(self.users, self.points)
    
    def update_scores(self):
        '''
        Writes to the highscores table.
        '''
        with open('highscores.txt', 'w') as f:
            for user, points in self.scores:
                f.write(('{},{}\n'.format(user, points)))


class Character():
    '''
    A person which runs about.
    '''
    def __init__(self, char_id, pos):
        '''
        Stores the data about the character.
        '''
        self.id = char_id
        self.pos = np.array(pos)
        if self.id == 'Main':
            self.colour = colours['yellow']
            self.lives = 3
        elif self.id == 'Infected':
            self.colour = colours['green']
        else:
            self.colour = colours['red']
        self.frame = -1 # -1 means the character isn't moving
        self.sprite = 0
        self.distract_time = 0
        self.caught = False
        if self.id == 'Infected' and MAIN.caught:
            self.on_death_target()
        elif self.id in ('Main', 'Infected'):
            self.target = None
        else:
            self.target = np.array((
                randint(1, BOUNDARY_X - 3),
                randint(1, BOUNDARY_Y - 3)
                ))
    
    @property
    def x(self):
        '''
        Returns the x position
        '''
        return self.pos[0]
    
    @property
    def y(self):
        '''
        Returns the y position
        '''
        return self.pos[1]
    
    @x.setter
    def x(self, x):
        '''
        Changes the x position
        '''
        self.pos[0] = x
    
    @y.setter
    def y(self, y):
        '''
        Changes the y position
        '''
        self.pos[1] = y
    
    def distance(self, obj):
        '''
        Calculates the absolute position difference in pixels between two
        objects.
        '''
        return sum(abs(self.pos - obj.pos))
    
    def move_left(self):
        '''
        Moves the character leftwards.
        '''
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.x - self.x + 1) < abs(char.x - self.x) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.x - 1 > 0:
            self.x -= 1
            self.set_animate()
    
    def move_right(self):
        '''
        Moves the character rightwards.
        '''
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.x - self.x - 1) < abs(char.x - self.x) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.x + 1 < BOUNDARY_X - 2:
            self.x += 1
            self.set_animate()
    
    def move_up(self):
        '''
        Moves the character upwards.
        '''
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.y - self.y + 1) < abs(char.y - self.y) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.y - 1 > 0:
            self.y -= 1
            self.set_animate()
    
    def move_down(self):
        '''
        Moves the character downwards.
        '''
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.y - self.y - 1) < abs(char.y - self.y) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.y + 1 < BOUNDARY_Y - 2:
            self.y += 1
            self.set_animate()
    
    def animate(self):
        '''
        Animates the character.
        '''
        if self.frame >= 0:
            self.frame += 1
            if self.frame == 3:
                self.frame = 0
                self.sprite += 1
                if self.sprite == 4:
                    self.sprite = 0
    
    def on_death_target(self):
        '''
        Creates a new target in the top left of the screen when the main
        character dies.
        '''
        self.target = np.random.uniform(1, 10, 2).astype(int)
    
    def new_target(self):
        '''
        Create a new target.
        '''
        self.target = np.array((
            randint(1, BOUNDARY_X - 3),
            randint(1, BOUNDARY_Y - 3)
            ))
    
    def move_ai(self):
        '''
        Moves the NPC.
        '''
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
    
    def distract(self):
        '''
        Occasionally, the infected characters are distracted.
        '''
        if self.id == 'Infected' and self.target is None:
            self.distract_time += 1
            if randint(1, 6000) < self.distract_time - 20:
                self.distract_time = 0
                self.new_target()
                if len(characters) < 100 and randint(1, 10) == 1:
                    eggs.append(Egg(self.pos))
                    sound.layegg_wav.play()
    
    def mainloop(self):
        '''
        Changes the sprite mainloop.
        '''
        if self.id == 'Main':
            self.revive()
            self.flash()
        
        self.distract()
        self.move_ai()
        self.animate()
        self.infect()
    
    def set_animate(self, on=True):
        '''
        Sets the animation on or off.
        '''
        if on and self.frame == -1:
            self.frame = 0
        elif not on:
            self.frame = -1
            self.sprite = 0
    
    def infect(self):
        '''
        Infects all surrounding NPCs.
        '''
        infect_radius = 5
        if self.id != 'Infected':
            return
        
        for char in filter(lambda x: x.id not in ('Infected', 'Main'),
            characters):
            if (abs(char.x - self.x) < infect_radius and
                abs(char.y - self.y) < infect_radius):
                char.colour = colours['green']
                char.id = 'Infected'
                if MAIN.caught:
                    char.on_death_target()
        
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
                    char.on_death_target()
            high_scores.new_score(10 * int(time_passed[0] / 100))


class MainCharacter(Character):
    '''
    The main character who the user controls.
    '''
    def __init__(self, pos):
        super().__init__(char_id='Main', pos=pos)
        self.flash_i = None
        self.mobile = False
    
    def revive(self):
        '''
        If the main character dies, and still has lives, it can be revived.
        '''
        if time_passed[1] == 100 and self.lives > 0:
            self.pos = np.array((90, 90))
            self.colour = colours['yellow']
            self.caught = False
            time_passed[1] = 0
            self.lives -= 1
            self.flash_i = 0

    def flash(self):
        '''
        Upon revival, the main character flashes to alert the user to its
        position. During this time, the user cannot be caught.
        '''
        if self.flash_i is not None:
            self.flash_i += 1
            if self.flash_i == 30:
                self.flash_i = None
    
    def visible(self):
        '''
        Returns True if the main character can be seen.
        '''
        return self.flash_i is None or self.flash_i % 10 < 5

class Shockwave():
    '''
    A shockwave is visibly emitted from an egg.
    '''
    def __init__(self, pos):
        '''
        Stores the shockwave details.
        '''
        self.pos = pos
        self.radius = 1
        sound.shockwave_wav.play()
    
    def draw(self):
        '''
        Draws the shockwave.
        '''
        pygame.draw.lines(PSEUDO_SCREEN, colours['magenta'], True,
            (self.pos + DISP + np.array((self.radius, 0)),
             self.pos + DISP + np.array((0, self.radius)),
             self.pos + DISP + np.array((-self.radius, 0)),
             self.pos + DISP + np.array((0, -self.radius))))
    
    def mainloop(self):
        '''
        Runs the shockwave mainloop.
        '''
        self.radius += 2
        for char in characters:
                if (char.id == 'Infected' and
                    char.distance(self) < self.radius and
                    len(list(filter(lambda x: x.id == 'Infected',
                                    characters))) > 1):
                    char.id = 'Disinfected'
                    char.new_target()
                    char.colour = colours['red']
                    time_passed[0] += 100
        
        if self.radius > 20:
            shockwaves.remove(self)

class Egg():
    '''
    An egg hatches infected characters.
    '''
    def __init__(self, pos):
        '''
        Stores the egg position.
        '''
        self.pos = np.array(pos)
        self.age = 0
        self.colour = colours['blue']
    
    def mainloop(self):
        '''
        Ages the egg appropriately.
        '''
        self.age += 1
        self.flash()
        if self.age <= 200:
            self.collect()
        else:
            self.hatch()
    
    def hatch(self):
        '''
        Hatches the egg.
        '''
        sound.hatch_wav.play()
        eggs.remove(self)
        characters.append(Character(char_id='Infected', pos=self.pos))
    
    def collect(self):
        '''
        If the main character picks up the egg before hatching, it disinfects
        all characters within a radius, unless all of them are within range, in
        which case, one remains infected.
        '''
        if MAIN.distance(self) < 5 and not MAIN.caught:
            eggs.remove(self)
            shockwaves.append(Shockwave(self.pos))
            time_passed[0] += 200
    
    def flash(self):
        '''
        The egg shortly flashes before hatching.
        '''
        if self.age > 150 and self.age % 5 == 0:
            if self.colour is colours['blue']:
                self.colour = colours['cyan']
                sound.crack_wav.play()
            else:
                self.colour = colours['blue']


def draw_heart(pos):
    '''
    Draws a heart, representing a life.
    '''
    pygame.draw.lines(PSEUDO_SCREEN, colours['red'], False,
                      (pos + (0, 1),
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
                       pos + (2, 2)))

def draw_countdown():
    '''
    Draws the countdown on screen.
    '''
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

def register_objects():
    '''
    Runs the mainloop.
    '''
    if MAIN.mobile:
        for character in characters:
            character.mainloop()
        
        for egg in eggs:
            egg.mainloop()
        
        for shockwave in shockwaves:
            shockwave.mainloop()
    
    elif time_passed[2] > 60:
        MAIN.mobile = True

def display_objects():
    '''
    Refreshes the screen
    '''
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
        if char.id == 'Main' and not char.visible():
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

def write_left_align(text, *, y, x=1, colour=colours['green'], size='large'):
    '''
    Draws left aligned text.
    '''
    if size == 'large':
        gap = 10
        char_dict = letters.char_to_func
    else:
        gap = 6
        char_dict = letters.char_to_mini_func
    
    for char in text:
        char_dict[char](PSEUDO_SCREEN, np.array((x, y)), colour=colour)
        x += gap

def write_right_align(text, *, y, x=DIM_X, colour=colours['green'],
                      size='large'):
    '''
    Displays right aligned text.
    '''
    if size == 'large':
        gap = 10
        char_dict = letters.char_to_func
    else:
        gap = 6
        char_dict = letters.char_to_mini_func
    
    for char in str(text)[::-1]:
        x -= gap
        char_dict[char](PSEUDO_SCREEN, np.array((x, y)), colour=colour)

def write_centre_align(text, *, y, colour=colours['green'], size='large'):
    '''
    Displays centre aligned text.
    '''
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

def display_highscores():
    '''
    Displays the highscores onto the screen.
    '''
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
                    np.array((len(high_scores.insert_user) * 10 + 1, y + 8)),
                    np.array((len(high_scores.insert_user) * 10 + 8, y + 8)))
            y += 10
            if i == 8:
                break
        
        write_left_align(user, y=y)
        write_right_align(points, y=y)
        
        y += 10
        if i == 9:
            break
    
    # Enlarges the screen
    SCREEN.blit(pygame.transform.scale(PSEUDO_SCREEN, RESOLUTION * 8), (0, 0))
    pygame.display.flip()

def new_game():
    '''
    Creates a new game.
    '''
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
        x = randint(1, BOUNDARY_X - 2)
        y = randint(1, BOUNDARY_Y - 2)
        characters.append(Character('Disinfected', (x, y)))
    eggs.clear()
    shockwaves.clear()

def type_char(event):
    '''
    Types a character in the credits.
    '''
    if (high_scores.insert_user is not None and
        len(high_scores.insert_user) < 4):
        high_scores.insert_user += letters.event_to_char[event.key]

def delete_char():
    '''
    Removes the last character in the credits.
    '''
    if (high_scores.insert_user is not None and
        len(high_scores.insert_user) > 0):
        high_scores.insert_user = high_scores.insert_user[:-1]

def enter_name():
    '''
    Occurs when the user finishes typing their name and hits enter.
    '''
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

def control_main():
    '''
    Moves the character appropriately.
    '''
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

def increment_time():
    '''
    Adjusts the recorded time appropriately.
    '''
    # Increases the time since the game started (for countdown purposes only)
    if not MAIN.mobile:
        time_passed[2] += 1
    
    # Increases the time since game started
    elif not MAIN.caught:
        time_passed[0] += 1
    
    # Otherwise increases the time since caught
    elif time_passed[1] <= 100:
        time_passed[1] += 1

def handle_key_down():
    '''
    Handles the pressing down of a key.
    '''
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
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

def mainloop():
    '''
    Runs the mainloop for the game.
    '''
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

class StartScreen():
    '''
    Provides a start screen for the player.
    '''
    def __init__(self):
        '''
        Stores the state of being on.
        '''
        self.flash_i = 0
        self.on_start_screen = True
        
        print(listdir)
        
        self.start_img = pygame.image.load(
            path.join('outbreak', 'play_screen.png')
            )
    
    def start_screen(self):
        '''
        Introduces the game to the character.
        '''
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

SS = StartScreen()
MAIN = MainCharacter((90, 90))
characters = []
eggs = []
shockwaves = []

new_game()

high_scores = HighScores()

try:
    while MAIN in characters:
        if SS.on_start_screen:
            SS.start_screen()
        else:
            mainloop()
finally:
    pygame.display.quit()
    pygame.quit()
