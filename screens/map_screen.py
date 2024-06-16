import pygame
from pygame.locals import *

def map_screen(self):
  map_running = True

  def fade_in(width, height):
    map_background = pygame.transform.scale(self.raw_map_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    fade = pygame.Surface((width, height))
    fade.blit(map_background, (0, 0))
    for alpha in range(0, 255):
      fade.set_alpha(alpha)
      self.screen.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(8)
  

  fade_in(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

  while map_running:
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        map_running = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(self.map_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']
    
    pygame.display.update()