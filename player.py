import pygame
from pygame.locals import *

class Player():
  def __init__(self, screen):
    self.size = 192
    self.screen = screen
    self.frame = 0
    self.scale = 3.5
    self.animation_list = self.load_images(self.scale)
    self.image = self.animation_list[self.frame]
    self.update_time = pygame.time.get_ticks()

  def load_images(self, scale):
    sprite_sheet = pygame.image.load("./images/SlashAttack.png").convert_alpha()

    img_list = []
    for x in range(0, 6):
      temp_img = sprite_sheet.subsurface(x * self.size, 0, self.size, self.size)
      img_list.append(pygame.transform.scale(temp_img, (self.size * scale, self.size * scale)))

    return img_list

  def draw(self):
    self.screen.blit(self.image, (0, 80))

  def update(self):
    self.image = self.animation_list[self.frame]
    animation_cooldown = 150

    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame += 1
      self.update_time = pygame.time.get_ticks()
      self.screen.blit(self.image, (0, 80))
    if self.frame >= len(self.animation_list):
      self.frame = 0

