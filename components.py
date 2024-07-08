import pygame
from config import *

class Button:
  def __init__(self, x, y, width, height, fg, bg, content, fontsize, screen, main, url):
    self.font = pygame.font.Font("EBGaramond.ttf", fontsize)
    self.image = url

    self.content = content
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.fg = fg
    self.bg = bg
    self.fontsize = fontsize
    self.screen = screen

    self.raw_bg_image = pygame.image.load(self.image)
    self.bg_image = pygame.transform.scale(self.raw_bg_image, (self.width, self.height))

    self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
    self.image.blit(self.bg_image, (0, 0))
    self.rect = self.image.get_rect(center=(self.x, self.y))

    self.screen.blit(self.image, (main.SCREEN_WIDTH / 2 - 190, main.SCREEN_HEIGHT / 3 + 80))
  
  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
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
  def __init__(self, screen, player_hp, player_armor):
    self.x = 20
    self.y = 20
    self.width = 343
    self.height = 12.5

    self.hp = player_hp
    self.max_hp = 100
    self.armor = player_armor
    self.max_armor = 50

    self.screen = screen

  def draw(self, surface):
    raw_hp_bg = pygame.image.load("./images/HealthBar.png")
    health_bar_bg = pygame.transform.scale(raw_hp_bg, (400, 40))
    self.screen.blit(health_bar_bg, (self.x, self.y))

    health_ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, GREEN, (self.x + 33.5, self.y + 14, self.width * health_ratio, self.height))

    armor_ratio = self.armor / self.max_armor
    pygame.draw.rect(surface, GREY_BORDER, (self.x + 33.5, self.y + 40, self.width / 2 + 4, self.height / 2 + 4))
    pygame.draw.rect(surface, GREY, (self.x + 35.5, self.y + 42, self.width / 2 * armor_ratio, self.height / 2))

    font = pygame.font.Font('EBGaramond.ttf', 12)
    health = font.render(str(self.hp), True, WHITE)
    self.screen.blit(health, (self.x + 40, self.y + 11.5))

class EnemyHealthBar:
  def __init__(self, screen, enemy_hp, max_enemy_hp):
    self.width = 343
    self.height = 12.5

    self.hp = enemy_hp
    self.max_hp = max_enemy_hp

    self.screen = screen

  def draw(self, surface, SCREEN_WIDTH):
    x = SCREEN_WIDTH

    raw_hp_bg = pygame.image.load("./images/HealthBar.png")
    health_bar_bg = pygame.transform.flip(pygame.transform.scale(raw_hp_bg, (400, 40)), True, False)
    self.screen.blit(health_bar_bg, (x - 420, 20))

    health_ratio = self.hp / self.max_hp
    ratioed_width = self.width * health_ratio

    pygame.draw.rect(surface, GREEN, (x - 53 - ratioed_width, 34, ratioed_width, self.height))

    font = pygame.font.Font('EBGaramond.ttf', 12)
    health = font.render(str(self.hp), True, WHITE)
    self.screen.blit(health, (x - 70, 31.5))

class RemainingPile:
  def __init__(self, screen):
    self.card_url = pygame.transform.scale(pygame.image.load("./images/RemainingCards.png"), (80, 80))
    self.screen = screen
    self.rect = self.card_url.get_rect()

  def draw(self, height):
    self.screen.blit(self.card_url, (20, height - 100))
    self.rect.x = 20
    self.rect.y = height - 100

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False

class DiscardPile:
  def __init__(self, screen):
    self.card_url = pygame.transform.scale(pygame.image.load("./images/DiscardedCards.png"), (80, 80))
    self.screen = screen
    self.rect = self.card_url.get_rect()

  def draw(self, width, height):
    self.screen.blit(self.card_url, (width - 100, height - 100))
    self.rect.x = width - 100
    self.rect.y = height - 100

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False
  
class BackArrow:
  def __init__(self, screen, pos, width):
    self.screen = screen
    self.back_arrow = pygame.transform.scale(pygame.image.load("./images/BackArrow.png"), (50, 50))
    self.rect = self.back_arrow.get_rect()
    self.rect.y = 20

    if pos == "left":
      self.screen.blit(self.back_arrow, (20, 20))
      self.rect.x = 20
    else:
      self.back_arrow = pygame.transform.flip(self.back_arrow, True, False)
      self.screen.blit(self.back_arrow, (width - 60, 20))
      self.rect.x = width - 60

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False

class Card:
  def __init__(self, pos, card_type, width, height, screen, main, enemy_hp):
    self.pos = pos
    self.card_type = card_type
    self.raw_card_url = pygame.image.load("./images/cards/" + card_type + ".png")
    self.card_url = pygame.transform.scale(self.raw_card_url, (300, 450))
    self.screen = screen
    self.rect = self.card_url.get_rect()

    self.width = width
    self.height = height
    self.main = main

    self.enemy_hp = enemy_hp
    self.damage_inflicted = 0
    self.damage_received = 0

    self.x_val = 0

    if pos == "left":
      self.x_val = self.width / 2 - 400
    elif pos == "mid":
      self.x_val = self.width / 2 - 150
    elif pos == "right":
      self.x_val = self.width / 2 + 100  
    elif pos == "ml":
      self.x_val = self.width / 2 - 300
    elif pos == "mr":
      self.x_val = self.width / 2 

    self.y_val = self.height - 250

    self.screen.blit(self.card_url, (self.x_val, self.y_val))

    self.rect.x = self.x_val
    self.rect.y = self.y_val

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        if self.card_type == "Defend":
          self.main.player_armor += 5
          if self.main.player_armor > self.main.max_player_armor:
            self.main.player_armor = self.main.max_player_armor

        if self.card_type == "Feed":
          self.main.player_hp += 7
          self.damage_received -= 7
          if self.main.player_hp > 100:
            self.main.player_hp = 100

        if self.card_type == "BladeDance":
          self.enemy_hp -= 6
          self.damage_inflicted += 6

        if self.card_type == "LimitBreak":
          self.enemy_hp -= 20
          self.main.player_hp -= 5
          self.damage_inflicted += 20
          self.damage_received += 5

        if self.card_type == "PerfectStrike":
          self.enemy_hp -= 12
          self.damage_inflicted += 12
        
        if self.card_type == "Barricade":
          self.main.player_armor += 14
          if self.main.player_armor > self.main.max_player_armor:
            self.main.player_armor = self.main.max_player_armor

        if self.card_type == "BodySlam":
          self.main.player_armor += 10
          if self.main.player_armor > self.main.max_player_armor:
            self.main.player_armor = self.main.max_player_armor
          self.enemy_hp -= 10
          self.damage_inflicted += 10
        
        if self.card_type == "Carnage":
          self.enemy_hp -= 30
          self.main.player_hp -= 15
          self.damage_inflicted += 30
          self.damage_received += 15
        
        if self.card_type == "FeelNoPain":
          self.main.player_armor += 20
          if self.main.player_armor > self.main.max_player_armor:
            self.main.player_armor = self.main.max_player_armor

        if self.card_type == "GhostArmour":
          self.main.player_armor += 20
          if self.main.player_armor > self.main.max_player_armor:
            self.main.player_armor = self.main.max_player_armor
          self.main.player_hp -= 5
          self.damage_received += 5
          
        return True
      return False
    return False
  
  def draw(self):
    self.screen.blit(self.card_url, (self.x_val, self.y_val))

    self.rect.x = self.x_val
    self.rect.y = self.y_val
  
  def is_hovered(self):
    mouse_pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(mouse_pos):
      self.y_val -= 150
      self.draw()
  
class CardGrid:
  def __init__(self, card_list, screen, width, height, card_type):
    self.list = card_list
    self.screen = screen
    self.margin = 100
    self.y_val = 100
    self.x_val = 100
    self.gap = ((width - 200) - 1200) / 4
    self.card_type = card_type
    self.width = width
    self.height = height

    for card in self.list:
      raw_card_url = pygame.image.load("./images/cards/" + card + ".png")
      card_url = pygame.transform.scale(raw_card_url, (300, 450))
      self.x_val = self.margin + self.list.index(card) * 300 + self.gap

      if len(self.list) > 4:
        if self.list.index(card) == 4:
          self.y_val += 400
          self.x_val = 100

      self.screen.blit(card_url, (self.x_val, self.y_val))

    if len(self.list) == 0:
      font = pygame.font.Font('EBGaramond.ttf', 20)
      title = font.render("No Remaining Cards" if card_type == "r" else "No Discarded Cards", True, WHITE)
      title_coords = title.get_rect(center=(self.width / 2, self.height / 8))
      self.screen.blit(title, title_coords)
  