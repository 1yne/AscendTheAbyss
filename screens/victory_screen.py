import pygame
from pygame.locals import *
from functions import *
from config import *

def victory_screen(main, data):
  victory = True

  victory_background = pygame.transform.scale(main.raw_victory_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
  fade_in(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, victory_background)

  victory_image = pygame.transform.scale(pygame.image.load("./images/Victory.png").convert_alpha(), (420, 382))
  defeat_image = pygame.transform.scale(pygame.image.load("./images/Defeat.png").convert_alpha(), (500, 382))

  start_time = pygame.time.get_ticks()

  font = pygame.font.Font('EBGaramond.ttf', 36)
  damage_inflicted = data[1]
  damage_received = data[2]

  if data[0]:
    main.max_player_armor += 10

  def display_text():
    if data[0] == True:
      title = main.font.render("VICTORY", True, WHITE)
    else:
      title = main.font.render("DEFEAT", True, WHITE)
    title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 2 + 80))
    main.screen.blit(title, title_coords)

  def display_damage():
    dmg_infl_text = font.render("Damage Inflicted: " + str(damage_inflicted), True, WHITE)
    dmg_infl_text_coords = dmg_infl_text.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 2 + 200))
    main.screen.blit(dmg_infl_text, dmg_infl_text_coords)

    dmg_recv_text = font.render("Damage Received: " + str(damage_received), True, WHITE)
    dmg_recv_text_coords = dmg_recv_text.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 2 + 270))
    main.screen.blit(dmg_recv_text, dmg_recv_text_coords)

    armor_buff_text = font.render("Max Armor Buff: +10" if data[0] else "Max Armor Buff: +0", True, WHITE)
    armor_buff_coords = armor_buff_text.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 2 + 340))
    main.screen.blit(armor_buff_text, armor_buff_coords)


  while victory:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        victory = False
        main.running = False
        main.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(victory_background, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    victory_background = pygame.transform.scale(main.raw_victory_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
    main.screen.blit(victory_background, (0, 0))

    if data[0]:
      main.screen.blit(victory_image, (main.SCREEN_WIDTH / 2 - 210, 50))
    else:
      main.screen.blit(defeat_image, (main.SCREEN_WIDTH / 2 - 210, 50))

    display_text()
    display_damage()

    if pygame.time.get_ticks() - start_time > 5000:
      victory = False
      fade_out(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    pygame.display.update()