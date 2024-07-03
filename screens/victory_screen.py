import pygame
from pygame.locals import *
from functions import *
from config import *

def victory_screen(main, data):
  victory = True
  black_bg = pygame.Surface((main.SCREEN_WIDTH, main.SCREEN_HEIGHT), pygame.SRCALPHA)
  black_bg.fill((0, 0, 0, 200))
  fade_in_victory(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)
  start_time = pygame.time.get_ticks()
  font = pygame.font.Font('EBGaramond.ttf', 45)
  damage_inflicted = data[1]
  damage_received = data[2]

  def display_text():
    if data[0] == True:
      title = main.font.render("VICTORY", True, WHITE)
    else:
      title = main.font.render("DEFEAT", True, WHITE)
    title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 5))
    main.screen.blit(title, title_coords)

  def display_damage():
    dmg_infl_text = font.render("Damage Inflicted: " + str(damage_inflicted), True, WHITE)
    dmg_infl_text_coords = dmg_infl_text.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 5 + 150))
    main.screen.blit(dmg_infl_text, dmg_infl_text_coords)

    dmg_recv_text = font.render("Damage Received: " + str(damage_received), True, WHITE)
    dmg_recv_text_coords = dmg_recv_text.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 5 + 220))
    main.screen.blit(dmg_recv_text, dmg_recv_text_coords)

  while victory:
    main.screen.blit(black_bg, (0, 0))
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        victory = False
        main.running = False
        main.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    display_text()
    display_damage()

    if pygame.time.get_ticks() - start_time > 2000:
      victory = False
      fade_out(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    pygame.display.update()