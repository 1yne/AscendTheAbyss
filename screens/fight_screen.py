import pygame
from pygame.locals import *
from config import *
from functions import *
from components import *

def fight_screen(self):
  fight = True
  fight_background = pygame.transform.scale(self.raw_fight_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

  fade_in(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, fight_background)

  health_bar = PlayerHealthBar(20, 20, 300, 20, 100, self.screen)

  while fight:
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        intro = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(fight_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    health_bar.hp = self.player_hp
    health_bar.draw(self.screen)

    pygame.display.update()
