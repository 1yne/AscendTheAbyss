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
    self.width = 343
    self.height = 12.5
    self.hp = player_hp
    self.max_hp = 100
    self.screen = screen

  def draw(self, surface):
    raw_hp_bg = pygame.image.load("./images/PlayerHealthBar.png")
    health_bar_bg = pygame.transform.scale(raw_hp_bg, (400, 40))
    self.screen.blit(health_bar_bg, (self.x, self.y))

    health_ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, GREEN, (self.x + 33.5, self.y + 14, self.width * health_ratio, self.height))

class EnemyHealthBar:
  def __init__(self, screen, enemy_hp, max_enemy_hp):
    self.width = 343
    self.height = 12.5

    self.hp = enemy_hp
    self.max_hp = max_enemy_hp

    self.screen = screen

  def draw(self, surface, SCREEN_WIDTH):
    x = SCREEN_WIDTH

    raw_hp_bg = pygame.image.load("./images/PlayerHealthBar.png")
    health_bar_bg = pygame.transform.flip(pygame.transform.scale(raw_hp_bg, (400, 40)), True, False)
    self.screen.blit(health_bar_bg, (x - 420, 20))

    health_ratio = self.hp / self.max_hp
    ratioed_width = self.width * health_ratio

    pygame.draw.rect(surface, GREEN, (x - 53 - ratioed_width, 34, ratioed_width, self.height))
