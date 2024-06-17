import pygame
from pygame.locals import *
from functions import *

def map_screen(self):
  map_running = True
  map_background = pygame.transform.scale(self.raw_map_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

  fade_in(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, map_background)

  while map_running:
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        map_running = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(map_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']
    
    pygame.display.update()