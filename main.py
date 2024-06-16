import pygame
from pygame.locals import *
from components import *
from config import *

class Game: 
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("Test")
    self.screen = pygame.display.set_mode((800, 700), RESIZABLE)
    self.font = pygame.font.Font('EBGaramond.ttf', 96)
    self.running = True
    self.raw_intro_background = pygame.image.load("./images/Background.jpg")
    self.intro_background = pygame.transform.scale(self.raw_intro_background, (800, 700))
    self.SCREEN_WIDTH, self.SCREEN_HEIGHT = pygame.display.get_surface().get_size()
    self.window = self.screen.get_rect


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
      title = self.font.render("Welcome to Test", True, WHITE)
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

      play_button = Button(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2, 380, 120, WHITE, BROWN, 'PLAY', 24)

      mouse_pos = pygame.mouse.get_pos()
      mouse_pressed = pygame.mouse.get_pressed()

      if play_button.is_pressed(mouse_pos, mouse_pressed):
        intro = False
      
      if play_button.is_hovering():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
      
      if play_button.is_not_hovering():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
      show_display_text()

      pygame.display.update()
      self.screen.blit(play_button.image, play_button.rect)

g = Game()
g.new()

while g.running:
  g.main()

pygame.quit()
