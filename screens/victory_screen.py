import pygame
from pygame.locals import *
from functions import *
from config import *

def victory_screen(main):
  victory = True
  black_bg = pygame.Surface((main.SCREEN_WIDTH, main.SCREEN_HEIGHT), pygame.SRCALPHA)
  black_bg.fill((0, 0, 0, 200))
  fade_in_victory(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, black_bg)
  start_time = pygame.time.get_ticks()

  def display_text():
    title = main.font.render("VICTORY", True, WHITE)
    title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, main.SCREEN_HEIGHT / 5))
    main.screen.blit(title, title_coords)

  while victory:
    main.screen.blit(black_bg, (0, 0))
    events = pygame.event.get()
    for event in events:
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        victory = False
        main.running = False
        main.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    display_text()

    if pygame.time.get_ticks() - start_time > 2000:
      victory = False
      fade_out(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    pygame.display.update()