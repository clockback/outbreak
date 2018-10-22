import random

import numpy as np
import pygame

RESOLUTION = np.array((125, 100))
PSEUDO_SCREEN = pygame.Surface(RESOLUTION)
SCREEN = pygame.display.set_mode(RESOLUTION * 8)

CLOCK = pygame.time.Clock()


class Character():
    '''
    A person which runs about.
    '''
    def __init__(self, char_id, pos, colour):
        '''
        Stores the data about the character.
        '''
        self.id = char_id
        self.pos = np.array(pos)
        self.colour = colour
        self.frame = -1 # -1 means the character isn't moving
        self.sprite = 0
        self.distract_time = 0
        self.caught = False
        if self.id in ('Main', 'Infected'):
            self.target = None
        else:
            self.target = np.array((
                random.randint(1, 122),
                random.randint(1, 97)
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
    
    def distance(self, character):
        """
        Calculates the absolute position difference in pixels between two
        characters.
        """
        return sum(abs(self.pos - character.pos))
    
    def move_left(self):
        """
        Moves the character leftwards.
        """
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
        """
        Moves the character rightwards.
        """
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.x - self.x - 1) < abs(char.x - self.x) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.x + 1 < 123:
            self.x += 1
            self.set_animate()
    
    def move_up(self):
        """
        Moves the character upwards.
        """
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
        """
        Moves the character downwards.
        """
        if self.id == 'Infected':
            for char in filter(lambda x: x.id == 'Infected', characters):
                if abs(char.x - self.x) < 2 and abs(char.y - self.y) < 2:
                    if abs(char.y - self.y - 1) < abs(char.y - self.y) < 2:
                        if self.distance(MAIN) > 5 and self.target is None:
                            return
        if self.y + 1 < 98:
            self.y += 1
            self.set_animate()
    
    def animate(self):
        """
        Animates the character.
        """
        if self.frame >= 0:
            self.frame += 1
            if self.frame == 3:
                self.frame = 0
                self.sprite += 1
                if self.sprite == 4:
                    self.sprite = 0
    
    def new_target(self):
        """
        Create a new target.
        """
        self.target = np.array((
            random.randint(1, 122),
            random.randint(1, 97)
            ))
    
    def move_ai(self):
        """
        Moves the NPC.
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
    
    def distract(self):
        '''
        Occasionally, the infected characters are distracted.
        '''
        if self.id == 'Infected' and self.target is None:
            self.distract_time += 1
            if random.randint(1, 6000) < self.distract_time - 20:
                self.distract_time = 0
                self.new_target()
                if len(characters) < 100 and random.randint(1, 10) == 1:
                    eggs.append(Egg(self.pos))
    
    def mainloop(self):
        '''
        Changes the sprite mainloop.
        '''
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
        if self.id == 'Infected':
            for char in filter(lambda x: x.id not in ('Infected', 'Main'),
                characters):
                if abs(char.x - self.x) < 5 and abs(char.y - self.y) < 5:
                    char.colour = (0, 255, 0)
                    char.id = 'Infected'
            
            if abs(MAIN.x - self.x) < 5 and abs(MAIN.y - self.y) < 5:
                MAIN.colour = (0, 100, 0)
                MAIN.caught = True


class MainCharacter(Character):
    '''
    The main character who the user controls.
    '''
    def __init__(self, pos):
        super().__init__(char_id='Main', pos=pos, colour=(255, 255, 0))


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
    
    def mainloop(self):
        '''
        Ages the egg appropriately.
        '''
        self.age += 1
        if self.age > 100:
            self.hatch()
    
    def hatch(self):
        '''
        Hatches the egg.
        '''
        eggs.remove(self)
        characters.append(Character(char_id='Infected', pos=self.pos,
                                    colour=(0, 255, 0)))

def register_objects():
    '''
    Runs the mainloop.
    '''
    for character in characters:
        character.mainloop()
    
    for egg in eggs:
        egg.mainloop()

def display():
    '''
    Refreshes the screen
    '''
    # Refreshes the screen
    PSEUDO_SCREEN.fill((0, 0, 0))

    # Displays the boundaries
    pygame.draw.line(PSEUDO_SCREEN, (100, 0, 0), (0, 0), (125, 0))
    pygame.draw.line(PSEUDO_SCREEN, (100, 0, 0), (0, 99), (125, 99))
    pygame.draw.line(PSEUDO_SCREEN, (100, 0, 0), (0, 1), (0, 98))
    pygame.draw.line(PSEUDO_SCREEN, (100, 0, 0), (124, 1), (124, 98))
    
    # Displays the eggs
    for egg in eggs:
        pygame.draw.rect(PSEUDO_SCREEN, (0, 0, 255), (egg.pos, np.array((2, 2))))
    
    # Displays the characters on the screen
    for char in characters:
        pygame.draw.rect(PSEUDO_SCREEN, char.colour, (char.pos, np.array((2, 2))))
        if char.sprite == 1:
            PSEUDO_SCREEN.set_at(char.pos + np.array((0, -1)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((-1, 0)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((1, 2)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((2, 1)), char.colour)
        elif char.sprite == 3:
            PSEUDO_SCREEN.set_at(char.pos + np.array((1, -1)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((-1, 1)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((0, 2)), char.colour)
            PSEUDO_SCREEN.set_at(char.pos + np.array((2, 0)), char.colour)
    
    # Enlarges the screen
    SCREEN.blit(pygame.transform.scale(PSEUDO_SCREEN, RESOLUTION * 8), (0, 0))
    pygame.display.flip()

MAIN = MainCharacter((90, 90))
characters = [
    MAIN,
    Character('Infected', (10, 10), (0, 255, 0)),
    Character('Tom', (20, 20), (255, 0, 0)),
    Character('Moe', (90, 10), (255, 0, 0)),
    Character('Sue', (10, 90), (255, 0, 0)),
    Character('Jim', (20, 90), (255, 0, 0)),
    Character('Fred', (30, 90), (255, 0, 0)),
    Character('Sally', (40, 90), (255, 0, 0)),
    Character('Chuck', (50, 90), (255, 0, 0)),
    Character('Boris', (60, 90), (255, 0, 0)),
    Character('Nancy', (70, 90), (255, 0, 0)),
    Character('Dylan', (80, 90), (255, 0, 0)),
    Character('Susanna', (90, 90), (255, 0, 0)),
    ]
eggs = []

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            RUNNING = False
            break
    
    pressed = pygame.key.get_pressed()
    if not MAIN.caught:
        if pressed[pygame.K_LEFT]:
            MAIN.move_left()
        elif pressed[pygame.K_RIGHT]:
            MAIN.move_right()
        if pressed[pygame.K_UP]:
            MAIN.move_up()
        elif pressed[pygame.K_DOWN]:
            MAIN.move_down()
    
    if not any((
        pressed[pygame.K_LEFT],
        pressed[pygame.K_RIGHT],
        pressed[pygame.K_UP],
        pressed[pygame.K_DOWN],
        )):
        MAIN.set_animate(False)
    
    register_objects()
    display()
    CLOCK.tick(25)

pygame.display.quit()
pygame.quit()
