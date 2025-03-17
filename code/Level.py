#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, TIMEOUT_LEVEL, C_ORANGE, C_PURPLE, C_YELLOW
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Background'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load('./asset/Level1.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # Decrementa o timeout a cada quadro (em milissegundos)
            self.timeout -= clock.get_time()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(18, f'{'Level'} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
           # self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
           # self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            # Exibe o score do jogador
            for ent in self.entity_list:
                if isinstance(ent, Player):  # Encontra o jogador
                    self.level_text(22, f'Score: {ent.score}', C_WHITE, (10, 30))  # Exibe o score

            if self.timeout <= 0:
                self.level_text(50, "Time Out!", C_PURPLE, (10, WIN_HEIGHT - 50))
                pygame.display.flip()
                pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
                self.game_over()  # Chama a função para encerrar o jogo ou reiniciar
                break  # Encerra o loop principal do nível.
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def game_over(self):
        self.level_text(110, "GAME OVER", C_YELLOW, (WIN_HEIGHT // 2 - 100, WIN_HEIGHT // 2 - 20))
        pygame.display.flip()
        pygame.time.delay(6000)  # Exibe a mensagem de fim de jogo por 6 segundos.
        pygame.quit()
        sys.exit()  # Finaliza o jogo completamente.

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
