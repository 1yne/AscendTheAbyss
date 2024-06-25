import pygame
from pygame.locals import *

class Player():
  def __init__(self, screen, width, height):
    self.size = 192
    self.screen = screen
    self.frame = 0
    self.scale = 3.5
    self.animation_list = self.load_images("Idle")
    self.image = self.animation_list[self.frame]
    self.update_time = pygame.time.get_ticks()
    self.x_val = width / 4 
    self.y_val = height / 3 * 2

  def load_images(self, action_type):
    if action_type == "Attack":
      img_url = "./images/SlashAttack.png" 
      sprite_sheet = pygame.image.load(img_url).convert_alpha()
      size = 192
      self.x_val = 0
      self.y_val = 80

      img_list = []
      for x in range(0, 6):
        temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
        img_list.append(pygame.transform.scale(temp_img, (size * self.scale, size * self.scale)))

      return img_list
    elif action_type == "Idle":
      img_url = "./images/PlayerIdle.png"
      sprite_sheet = pygame.image.load(img_url).convert_alpha()
      size = 64
      self.x_val = 230
      self.y_val = 328

      img_list = []
      for x in range(0, 6):
        temp_img = sprite_sheet.subsurface(x * size, 0, size, size)
        img_list.append(pygame.transform.scale(temp_img, (size * self.scale, size * self.scale)))

      return img_list

  def draw(self):
    self.screen.blit(self.image, (self.x_val, self.y_val))

  def update(self, action_type):
    self.animation_list = self.load_images(action_type)
    self.image = self.animation_list[self.frame]
    animation_cooldown = 150

    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame += 1
      self.update_time = pygame.time.get_ticks()
      self.screen.blit(self.image, (self.x_val, self.y_val))
    if self.frame >= len(self.animation_list):
      self.frame = 0

