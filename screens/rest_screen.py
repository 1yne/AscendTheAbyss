import pygame
from pygame.locals import *
from functions import *
from config import *

def rest_screen(main):
  rest_screen = True
  background_img = pygame.transform.scale(pygame.image.load("./images/RestBackground.png"), (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
  heal_pic = pygame.image.load("./images/Heal.png")
  defend_pic = pygame.image.load("./images/Defend.png")
  heal_rect = heal_pic.get_rect()
  defend_rect = defend_pic.get_rect()

  font = pygame.font.Font('EBGaramond.ttf', 28)

  fade_in(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, background_img)

  def is_pressed(card):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if card.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False
  
  def display_heal_pic():
    main.screen.blit(heal_pic, (main.SCREEN_WIDTH / 4 * 3, main.SCREEN_HEIGHT / 4))
    heal_rect.x, heal_rect.y = main.SCREEN_WIDTH / 4 * 3, main.SCREEN_HEIGHT / 4
    heal_text = font.render("Heal Full Health", True, BLACK)
    main.screen.blit(heal_text, (main.SCREEN_WIDTH / 4 * 3 - 40, main.SCREEN_HEIGHT / 4 + 90))
  
  def display_defend_pic():
    main.screen.blit(defend_pic, (main.SCREEN_WIDTH / 4 * 3, main.SCREEN_HEIGHT / 2))
    defend_rect.x, defend_rect.y = main.SCREEN_WIDTH / 4 * 3, main.SCREEN_HEIGHT / 2
    defend_text = font.render("Restore Full Armor", True, BLACK)
    main.screen.blit(defend_text, (main.SCREEN_WIDTH / 4 * 3 - 50, main.SCREEN_HEIGHT / 2 + 90))

  while rest_screen:
    events = pygame.event.get()

    for event in events:
      if event.type == pygame.QUIT:
        rest_screen = False
        main.running = False
        main.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(background_img, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    display_heal_pic()
    display_defend_pic()

    if is_pressed(heal_rect):
      main.player_hp = 100
      rest_screen = False

    if is_pressed(defend_rect):
      main.player_armor = main.max_player_armor
      rest_screen = False

    pygame.display.update()