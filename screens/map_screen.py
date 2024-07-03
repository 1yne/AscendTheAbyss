import pygame
from pygame.locals import *
from functions import *
from config import *

def map_screen(main, current_state):
  map_running = True
  
  map_background = pygame.transform.scale(main.raw_map_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
  enemy_pic = pygame.transform.scale(pygame.image.load("./images/map/Enemy.png").convert_alpha(), (80, 80))
  rest_pic = pygame.transform.scale(pygame.image.load("./images/map/Rest.png").convert_alpha(), (80, 80))
  treasure_pic = pygame.transform.scale(pygame.image.load("./images/map/Treasure.png").convert_alpha(), (80, 80))  
  boss_pic = pygame.transform.scale(pygame.image.load("./images/map/Boss.png").convert_alpha(), (386, 415))  

  enemy_one = enemy_pic.get_rect()
  enemy_two = enemy_pic.get_rect()
  enemy_three = enemy_pic.get_rect()
  enemy_four = enemy_pic.get_rect()

  treasure_one = treasure_pic.get_rect()
  treasure_two = treasure_pic.get_rect()

  rest_one = rest_pic.get_rect()
  rest_two = rest_pic.get_rect()

  boss_one = boss_pic.get_rect()

  def is_pressed(entity):
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if entity.collidepoint(mouse_pos):
      if mouse_pressed[0]:
        return  True
      return False
    return False

  def place_icons(x, y):
    main.screen.blit(enemy_pic, (150, y - 150))
    enemy_one.x, enemy_one.y = 150, y - 150

    main.screen.blit(enemy_pic, (200, y - 400))
    enemy_two.x, enemy_two.y = 200, y - 400

    pygame.draw.line(main.screen, BLACK, (190, y - 150), (240, y - 320), 4)

    main.screen.blit(treasure_pic, (300, y - 580))
    treasure_one.x, treasure_one.y = 300, y - 580

    pygame.draw.line(main.screen, BLACK, (240, y - 400), (340, y - 500), 4)

    main.screen.blit(enemy_pic, (450, 220))
    enemy_three.x, enemy_three.y = 450, 220

    pygame.draw.line(main.screen, BLACK, (380, y - 580), (450, 300), 4)

    main.screen.blit(rest_pic, (475, 520))
    rest_one.x, rest_one.y = 475, 520

    pygame.draw.line(main.screen, BLACK, (490, 300), (515, 520), 4)

    main.screen.blit(enemy_pic, (550, 660))
    enemy_four.x, enemy_four.y = 550, 660

    pygame.draw.line(main.screen, BLACK, (515, 600), (590, 660), 4)

    main.screen.blit(treasure_pic, (750, 280))
    treasure_two.x, treasure_two.y = 750, 280

    pygame.draw.line(main.screen, BLACK, (630, 660), (790, 360), 4)

    main.screen.blit(rest_pic, (825, 600))
    rest_two.x, rest_two.y = 825, 600

    pygame.draw.line(main.screen, BLACK, (790, 360), (865, 600), 4)

    main.screen.blit(boss_pic, (1000, 100))
    boss_one.x, boss_one.y = 1000, 100

    pygame.draw.line(main.screen, BLACK, (905, 600), (985, 550), 4)

  fade_in(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, map_background)

  while map_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        map_running = False
        main.running = False
        main.playing = False
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(map_background, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    surface = pygame.Surface((main.SCREEN_WIDTH, main.SCREEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(surface, (30,224,33,100), (250,100) ,10)
    
    place_icons(main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    pygame.display.update()