#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH

from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.score = 0

    def move(self):
        keys = pygame.key.get_pressed()  # Pega o estado de todas as teclas pressionadas
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

