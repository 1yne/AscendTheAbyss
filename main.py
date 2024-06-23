import pygame
from pygame.locals import *
from components import *
from config import *
from functions import *
from screens.map_screen import *
from screens.intro_screen import *
from screens.fight_screen import *

class Game: 
  def __init__(main):
    pygame.init()
    pygame.display.set_caption("Ascend the Abyss")
    
    main.screen = pygame.display.set_mode((800, 700), RESIZABLE)
    main.font = pygame.font.Font('EBGaramond.ttf', 96)
    main.running = True
    main.SCREEN_WIDTH, main.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    main.raw_intro_background = pygame.image.load("./images/Background.jpeg")
    main.raw_map_background = pygame.image.load("./images/MapBackground.jpeg")
    main.raw_fight_background = pygame.image.load("./images/FightBackground.jpeg")

    main.player_hp = 100
    main.player_armor = 50

  def new(main):
    # print("new() runs")
    main.playing = True

  def events(main):
    # print("event() running")
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        main.playing = False
        main.running = False
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(main.intro_background, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']
    intro_screen(main)
    victory = fight_screen(main, 40, "MobOne")
    map_screen(main)
  
  def draw(main):
    # print("draw() running")
    main.screen.fill(BLACK)
    pygame.display.update()

  def main(main):
    # print("main() running", main.playing)
    while main.playing:
      main.events()
      main.draw()
    main.running = False

g = Game()
g.new()

while g.running:
  g.main()

pygame.quit()
