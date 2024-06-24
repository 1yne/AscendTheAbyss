import pygame
from pygame.locals import *
from config import *
class Mob:
  def __init__(self, url, screen, width):
    self.url = url
    self.screen = screen
    self.width = width
    self.image = pygame.image.load("./images/mobs/" + self.url + ".PNG")
    self.x_val = width / 4 * 3
    self.y_val = 350

    if url == "enemy_one":
      self.image = pygame.transform.scale(self.image, (300, 175))
    elif url == "enemy_two":
      self.x_val = width / 2 + 200
      self.y_val = 205
    elif url == "enemy_three":
      self.x_val = width / 2 + 200
      self.y_val = 230
    elif url == "enemy_four":
      self.image = pygame.transform.scale(self.image, (300, 250))
      self.x_val = width / 4 * 3 - 80
      self.y_val = 280

    self.screen.blit(self.image, (self.x_val, self.y_val))
