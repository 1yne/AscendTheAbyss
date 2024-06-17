import pygame
from config import *

def fade_out(self, width, height):
  fade = pygame.Surface((width, height))
  for alpha in range(0, 155):
    fade.set_alpha(alpha)
    self.screen.blit(fade, (0, 0))
    pygame.display.update()
    pygame.time.delay(8)

def fade_in(self, width, height, background):
  fade = pygame.Surface((width, height))
  fade.blit(background, (0, 0))
  for alpha in range(0, 255):
    fade.set_alpha(alpha)
    self.screen.blit(fade, (0, 0))
    pygame.display.update()
    pygame.time.delay(8)