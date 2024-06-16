import pygame
from config import *

def fade_out(self, width, height):
  fade = pygame.Surface((width, height))
  for alpha in range(0, 155):
    fade.set_alpha(alpha)
    self.screen.blit(fade, (0, 0))
    pygame.display.update()
    pygame.time.delay(8)