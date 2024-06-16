import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
  def __init__(self, game):
    self.game = game

class Button:
  def __init__(self, x, y, width, height, fg, bg, content, fontsize, image):
    self.font = pygame.font.Font("EBGaramond.ttf", fontsize)

    self.content = content
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.fg = fg
    self.bg = bg
    self.fontsize = fontsize

    self.image = image
    self.raw_bg_image = pygame.image.load(self.image)
    self.bg_image = pygame.transform.scale(self.raw_bg_image, (self.width, self.height))

    self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
    self.image.blit(self.bg_image, (0, 0))
    self.rect = self.image.get_rect(center=(self.x, self.y))

    self.text = self.font.render(self.content, True, self.fg)
    self.text_coords = self.text.get_rect(center=(self.width / 2, self.height / 2))
    self.image.blit(self.text, self.text_coords)
  
  def is_pressed(self, pos, pressed):
    if self.rect.collidepoint(pos):
      if pressed[0]:
        return True
      return False
    return False

  def is_hovering(self):
    if self.rect.collidepoint(pygame.mouse.get_pos()):
      return True
  
  def is_not_hovering(self):
    if self.rect.collidepoint(pygame.mouse.get_pos()) == False:
      return True