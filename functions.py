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

def fade_in_victory(self, width, height, background):
  fade = pygame.Surface((width, height), pygame.SRCALPHA)
  fade.fill((0, 0, 0))
  for alpha in range(0, 100):
    fade.set_alpha(alpha)
    self.screen.blit(fade, (0, 0))
    pygame.display.update()
    pygame.time.delay(8)

def show_card(self, pos, height, card_img):
  x_val = 400 if pos == "left" else 600 if pos == "mid" else 800
  y_val = height - 350
  card = pygame.transform.scale(card_img, (300, 450))
  self.screen.blit(card, (x_val, y_val))
