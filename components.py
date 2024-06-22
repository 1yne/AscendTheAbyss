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
  def __init__(self, screen, player_hp, player_armor):
    self.x = 20
    self.y = 20
    self.width = 343
    self.height = 12.5
    self.hp = player_hp
    self.max_hp = 100
    self.screen = screen
    self.armor = player_armor
    self.max_armor = 50

  def draw(self, surface):
    raw_hp_bg = pygame.image.load("./images/HealthBar.png")
    health_bar_bg = pygame.transform.scale(raw_hp_bg, (400, 40))
    self.screen.blit(health_bar_bg, (self.x, self.y))

    health_ratio = self.hp / self.max_hp
    pygame.draw.rect(surface, GREEN, (self.x + 33.5, self.y + 14, self.width * health_ratio, self.height))

    armor_ratio = self.armor / self.max_armor
    pygame.draw.rect(surface, GREY_BORDER, (self.x + 33.5, self.y + 40, self.width / 2 + 4, self.height / 2 + 4))
    pygame.draw.rect(surface, GREY, (self.x + 35.5, self.y + 42, self.width / 2 * armor_ratio, self.height / 2))

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

class RemainingPile:
  def __init__(self, screen):
    self.card_url = pygame.transform.scale(pygame.image.load("./images/RemainingCards.png"), (80, 80))
    self.screen = screen
    self.rect = self.card_url.get_rect()

  def draw(self, width, height):
    self.screen.blit(self.card_url, (20, height - 100))
    self.rect.x = 20
    self.rect.y = height - 100

  def is_pressed(self, pos, pressed):
    if self.rect.collidepoint(pos):
      if pressed[0]:
        return  True
      return False
    return False
  
  # def slide(self, screen_width, background):
  #   for x in range(screen_width):
  #     # self.screen.blit(background, (x - screen_width, 0))
  #     pygame.display.update()

class DiscardPile:
  def __init__(self, screen):
    self.card_url = pygame.transform.scale(pygame.image.load("./images/DiscardedCards.png"), (80, 80))
    self.screen = screen
    self.rect = self.card_url.get_rect()

  def draw(self, width, height):
    self.screen.blit(self.card_url, (width - 100, height - 100))
    self.rect.x = width - 100
    self.rect.y = height - 100

  def is_pressed(self, pos, pressed):
    if self.rect.collidepoint(pos):
      if pressed[0]:
        return  True
      return False
    return False
  
  def slide(self, screen_width, background):
    for x in range(screen_width):
      self.screen.blit(background, (screen_width - x, 0))
      pygame.display.update()

  
class BackArrow:
  def __init__(self, screen, pos, width):
    self.screen = screen
    self.back_arrow = pygame.transform.scale(pygame.image.load("./images/BackArrow.png"), (50, 50))
    self.rect = self.back_arrow.get_rect()
    if pos == "left":
      self.screen.blit(self.back_arrow, (20, 20))
      self.rect.x = 20
    else:
      self.back_arrow = pygame.transform.flip(self.back_arrow, True, False)
      self.screen.blit(self.back_arrow, (width - 60, 20))
      self.rect.x = width - 60
    self.rect.y = 20

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False

class Card:
  def __init__(self, pos, card_type, width, height, screen):
    self.pos = pos
    self.card_type = card_type
    self.raw_card_url = pygame.image.load("./images/cards/" + card_type + ".png")
    self.card_url = pygame.transform.scale(self.raw_card_url, (300, 450))
    self.screen = screen
    self.rect = self.card_url.get_rect()
    self.width = width
    self.height = height

    self.x_val = self.width / 2 - 400 if pos == "left" else self.width / 2 - 150 if pos == "mid" else self.width / 2 + 100  
    self.y_val = self.height - 350

    self.screen.blit(self.card_url, (self.x_val, self.y_val))

    self.rect.x = self.x_val
    self.rect.y = self.y_val

  def is_pressed(self):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if self.rect.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False
  
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
  