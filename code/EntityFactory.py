#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Background':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Background{i}', (0, 0)))
                    list_bg.append(Background(f'Background{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT / 2))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 80)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(80, WIN_HEIGHT - 80)))