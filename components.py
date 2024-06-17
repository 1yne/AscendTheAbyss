import pygame
from config import *

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

class PlayerHealthBar:
  def __init__(self, screen, player_hp):
    self.x = 20
    self.y = 20
    self.width = 300
    self.height = 20
    self.hp = player_hp
    self.max_hp = 100
    self.screen = screen

  def draw(self, surface):
    font = pygame.font.Font('EBGaramond.ttf', 16)
    
    def show_display_text():
      title = font.render(str(self.hp), True, BLACK)
      self.screen.blit(title, (self.x + 10, self.y + 0.5))

    health_ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, GOLD, (self.x, self.y, self.width + 6, self.height + 6))
    pygame.draw.rect(surface, "red", (self.x + 3, self.y + 3, self.width, self.height))
    pygame.draw.rect(surface, "green", (self.x + 3, self.y + 3, self.width * health_ratio, self.height))

    show_display_text()

class EnemyHealthBar:
  def __init__(self, screen, enemy_hp, max_enemy_hp):
    self.width = 300
    self.height = 20

    self.hp = enemy_hp
    self.max_hp = max_enemy_hp

    self.screen = screen

  def draw(self, surface, SCREEN_WIDTH):
    x = SCREEN_WIDTH

    font = pygame.font.Font('EBGaramond.ttf', 16)
    
    def show_display_text():
      title = font.render(str(self.hp), True, BLACK)
      self.screen.blit(title, (x - 45, 20.5))

    health_ratio = self.hp / self.max_hp
    ratioed_width = self.width * health_ratio

    pygame.draw.rect(surface, GOLD, (x - 320, 20, self.width + 6, self.height + 6))
    pygame.draw.rect(surface, "red", (x - 317, 23, self.width, self.height))
    pygame.draw.rect(surface, "green", (x - 17 - ratioed_width, 23, ratioed_width, self.height))

    show_display_text()
