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
    
    def play_intro_mus(type):
      if type == "first":
        mixer.music.load("./music/IntroMusic.mp3") 
        mixer.music.set_volume(0.7) 
        mixer.music.play()
      else:
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
    play_intro_mus("first")
    intro_screen(main)

    
    play_mob_mus()
    data = fight_screen(main, 40, "enemy_one")
    victory_screen(main, data)
    
    if data[0]:
      play_intro_mus("second")
      play_mob_mus()
      data = fight_screen(main, 50, "enemy_two")
      victory_screen(main, data)
      if data[0]:
        play_intro_mus("second")
        victory_screen(main, data)
        rest_screen(main)
        play_mob_mus()
        data = fight_screen(main, 70, "enemy_three")
        victory_screen(main, data)
        if data[0]:
          play_intro_mus("second")
          victory_screen(main, data)
          play_mob_mus()
          data = fight_screen(main, 80, "enemy_four")
          victory_screen(main, data)
          if data[0]:
            play_intro_mus("second")
            victory_screen(main, data)
            rest_screen(main),
            play_boss_mus()
            data = fight_screen(main, 100, "boss")
            victory_screen(main, data)
            if data[0]:
              intro_screen(main)
            else:
              data = fight_screen(main, 40, "boss")
              victory_screen(main, data)
          else:
            data = fight_screen(main, 40, "enemy_four")
            victory_screen(main, data)
        else:
          data = fight_screen(main, 40, "enemy_three")
          victory_screen(main, data)
      else:
        data = fight_screen(main, 40, "enemy_two")
        victory_screen(main, data)
    else:
      data = fight_screen(main, 40, "enemy_one")
      victory_screen(main, data)
    
  
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
