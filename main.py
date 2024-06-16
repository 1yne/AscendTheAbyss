import pygame
from pygame.locals import *
from components import *
from config import *

class Game: 
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Ascend the Abyss")
    self.screen = pygame.display.set_mode((800, 700), RESIZABLE)
    self.font = pygame.font.Font('EBGaramond.ttf', 96)
    self.running = True
    self.raw_intro_background = pygame.image.load("./images/Background.jpeg")
    self.intro_background = pygame.transform.scale(self.raw_intro_background, (800, 700))
    self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    self.raw_map_background = pygame.image.load("./images/MapBackground.jpeg")

  def fade_out(self, width, height):
    fade = pygame.Surface((width, height))
    for alpha in range(0, 155):
      fade.set_alpha(alpha)
      self.screen.blit(fade, (0, 0))
      pygame.display.update()
      pygame.time.delay(8)

  def new(self):
    # print("new() runs")
    self.playing = True

  def events(self):
    # print("event() running")
    for event in pygame.event.get():
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        self.playing = False
        self.running = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(self.intro_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']
    self.intro_screen()
    self.map_screen()
  
  def draw(self):
    # print("draw() running")
    self.screen.fill(BLACK)
    pygame.display.update()

  def main(self):
    # print("main() running", self.playing)
    while self.playing:
      self.events()
      self.draw()
    self.running = False

  def intro_screen(self):
    intro = True
    # print("Intro screen running")
    self.screen.blit(self.intro_background, (0, 0))


    def show_display_text():
      title = self.font.render("Ascend the Abyss", True, WHITE)
      title_coords = title.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 5))
      self.screen.blit(title, title_coords)

    while intro:
      for event in pygame.event.get():
        # print("pygame events: ", event.type, pygame.QUIT)
        if event.type == pygame.QUIT:
          intro = False
          self.running = False
          self.playing = False
        elif event.type == VIDEORESIZE:
          self.screen.blit(pygame.transform.scale(self.intro_background, event.dict['size']), (0, 0))
          self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

      play_button = Button(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2, 380, 120, WHITE, BROWN, 'PLAY', 24,  "./images/ButtonBackgroundBrown.png")

      mouse_pos = pygame.mouse.get_pos()
      mouse_pressed = pygame.mouse.get_pressed()

      if play_button.is_pressed(mouse_pos, mouse_pressed):
        intro = False
        self.fade_out(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
      
      if play_button.is_hovering():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
      
      if play_button.is_not_hovering():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
      if intro:
        show_display_text()
        self.screen.blit(play_button.image, play_button.rect)
      else:
        self.screen.fill(BLACK)

      pygame.display.update()
  
  def map_screen(self):
    map_running = True

    def fade_in(width, height):
      map_background = pygame.transform.scale(self.raw_map_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

      fade = pygame.Surface((width, height))
      fade.blit(map_background, (0, 0))
      for alpha in range(0, 255):
        fade.set_alpha(alpha)
        self.screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(8)
    

    fade_in(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

    while map_running:
      for event in pygame.event.get():
        # print("pygame events: ", event.type, pygame.QUIT)
        if event.type == pygame.QUIT:
          map_running = False
          self.running = False
          self.playing = False
        elif event.type == VIDEORESIZE:
          self.screen.blit(pygame.transform.scale(self.map_background, event.dict['size']), (0, 0))
          self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']
      
      pygame.display.update()

g = Game()
g.new()

while g.running:
  g.main()

pygame.quit()
