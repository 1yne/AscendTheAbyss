import pygame
from pygame.locals import *
from config import *
from functions import *
from components import *

def fight_screen(self, max_enemy_hp):
  fight = True
  fight_background = pygame.transform.scale(self.raw_fight_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
  enemy_hp = 10

  fade_in(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, fight_background)

  player_health_bar = PlayerHealthBar(self.screen, self.player_hp)
  enemy_health_bar = EnemyHealthBar(self.screen, enemy_hp, max_enemy_hp)

  while fight:
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        fight = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(fight_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    player_health_bar.draw(self.screen)
    enemy_health_bar.draw(self.screen, self.SCREEN_WIDTH)

    pygame.display.update()
