import pygame
from pygame.locals import *
from config import *

class Mob:
  def __init__(self, url, screen, width, height):
    self.url = url
    self.screen = screen
    self.width = width
    self.image = pygame.transform.scale(pygame.image.load("./images/mobs/" + self.url + ".PNG"), (300, 250))
    self.x_val = width / 6 * 4
    self.y_val = height / 2.75

    self.screen.blit(self.image, (self.x_val, self.y_val))
