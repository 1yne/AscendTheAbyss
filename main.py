import pygame
from pygame.locals import *
from components import *
from config import *
from functions import *
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
    main.raw_fight_background = pygame.image.load("./images/FightBackground.jpeg")
    main.raw_victory_background = pygame.image.load("./images/MapBackground.png")

    main.player_hp = 100
    main.player_armor = 50
    main.max_player_armor = 50

  def new(main):
    main.playing = True

  def events(main):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        main.playing = False
        main.running = False
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(main.intro_background, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    def play_mus(src):
      mixer.music.pause()  
      mixer.music.load("./music/" + src + "Music.mp3") 
      mixer.music.set_volume(0.7) 
      mixer.music.play()

    pygame.mixer.init()
    play_mus("Intro")
    intro_screen(main)

    mob_list = ["enemy_one", "enemy_two", "enemy_three", "enemy_four", "boss"]
    enemy_list = {
      "enemy_one": 40, 
      "enemy_two": 50, 
      "enemy_three": 70, 
      "enemy_four": 80,
      "boss": 100
    }

    current_mob_index = 0
    current_mob = mob_list[current_mob_index]
    
    should_restart = True

    while should_restart:
      current_mob = mob_list[current_mob_index]
      if current_mob == "enemy_three" or current_mob == "boss":
        rest_screen(main)
      if "enemy" in current_mob:
        play_mus("Mob")
      else:
        play_mus("Boss")
      data = fight_screen(main, enemy_list[current_mob], current_mob)
      play_mus("Intro")
      victory_screen(main, data)

      if data[0] == True:
        if current_mob == "boss":
          should_restart = False
        current_mob_index += 1
      elif data[0] == False:
        current_mob_index = 0
        main.player_armor = main.max_player_armor
        main.player_hp = 100
  
    intro_screen(main)
    
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
