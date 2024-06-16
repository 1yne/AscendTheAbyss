import pygame
from pygame.locals import *
from components import *
from config import *
from functions import *
from screens.map_screen import *
from screens.intro_screen import *

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
    intro_screen(self)
    map_screen(self)
  
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

g = Game()
g.new()

while g.running:
  g.main()

pygame.quit()
