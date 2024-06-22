import pygame
from pygame.locals import *
from config import *
class Mob:
  def __init__(self, url, screen, width):
    self.url = url
    self.screen = screen
    self.width = width
    pygame.draw.rect(screen, BROWN, pygame.Rect(width / 4 * 3, 350, 100, 200))