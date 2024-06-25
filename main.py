import pygame
from pygame.locals import *
from components import *
from config import *
from functions import *
from screens.map_screen import *
from screens.intro_screen import *
from screens.fight_screen import *
from screens.victory_screen import *
from screens.rest_screen import *
from pygame import mixer 

class Game: 
  def __init__(main):
    pygame.init()
    pygame.display.set_caption("Ascend the Abyss")
    
    main.screen = pygame.display.set_mode((800, 700), RESIZABLE)
    main.font = pygame.font.Font('EBGaramond.ttf', 96)
    main.running = True
    main.SCREEN_WIDTH, main.SCREEN_HEIGHT = pygame.display.get_surface().get_size()

    main.raw_intro_background = pygame.image.load("./images/Background.jpeg")
    main.raw_map_background = pygame.image.load("./images/MapBackground.png")
    main.raw_fight_background = pygame.image.load("./images/FightBackground.png")

    main.player_hp = 100
    main.player_armor = 50

    main.current_state = "enemy_one"

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
    
    def play_intro_mus():
      mixer.music.pause()  
      mixer.music.load("./music/IntroMusic.mp3") 
      mixer.music.set_volume(0.7) 
      mixer.music.play()
    
    def play_mob_mus():
      mixer.music.pause()      
      mixer.music.load("./music/MobMusic.mp3") 
      mixer.music.set_volume(0.7) 
      mixer.music.play() 

    def play_boss_mus():
      mixer.music.pause()      
      mixer.music.load("./music/BossMusic.mp3") 
      mixer.music.set_volume(0.7) 
      mixer.music.play() 

    pygame.mixer.init()
    play_intro_mus()
    intro_screen(main)

    mob_list = ["enemy_one", "enemy_two", "enemy_three", "enemy_four", "boss"]
    enemy_list = {"enemy_one": 40, "enemy_two": 50, "enemy_three": 70, "enemy_four": 80, "boss": 100}

    current_mob_index = 0
    current_mob = mob_list[current_mob_index]
    
    should_restart = True

    while should_restart:
      current_mob = mob_list[current_mob_index]
      if current_mob == "enemy_three" or current_mob == "boss":
        rest_screen(main)
        current_mob_index += 1
        continue
      if "enemy" in current_mob:
        play_mob_mus()
      else:
        play_boss_mus()
      data = fight_screen(main, enemy_list[current_mob], current_mob)
      play_intro_mus()
      victory_screen(main, data)
      if data[0] == True:
        current_mob_index += 1
      elif data[0] == False:
        current_mob_index = 0
        main.player_armor = 50
        main.player_hp = 100
    
  
  def draw(main):
    main.screen.fill(BLACK)
    pygame.display.update()

  def main(main):
    while main.playing:
      main.events()
      main.draw()
    main.running = False

g = Game()
g.new()

while g.running:
  g.main()

pygame.quit()
