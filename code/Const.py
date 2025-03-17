# C
import pygame

C_RED = (255, 0, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Background0': 0,
    'Background1': 0.5,
    'Background2': 1,
    'Background3': 1.5,
    'Background4': 2,
    'Background5': 2.5,
    'Background6': 3,
    'Background7': 3.5,
    'Player': 3,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_HEALTH = {
    'Background0': 999,
    'Background1': 999,
    'Background2': 999,
    'Background3': 999,
    'Background4': 999,
    'Background5': 999,
    'Background6': 999,
    'Background7': 999,
    'Player': 200,
    'Enemy1': 50,
    'Enemy2': 60,
}
ENTITY_DAMAGE = {
    'Background0': 0,
    'Background1': 0,
    'Background2': 0,
    'Background3': 0,
    'Background4': 0,
    'Background5': 0,
    'Background6': 0,
    'Background7': 0,
    'Player': 1,
    'Enemy1': 1,
    'Enemy2': 1,
}

ENTITY_SCORE = {
    'Background0': 0,
    'Background1': 0,
    'Background2': 0,
    'Background3': 0,
    'Background4': 0,
    'Background5': 0,
    'Background6': 0,
    'Background7': 0,
    'Player': 0,
    'Enemy1': 100,
    'Enemy2': 125,
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEYS = {
    'Player': {
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT
    }
}

# S
SPAWN_TIME = 3000

# T
TIMEOUT_LEVEL = 15000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
