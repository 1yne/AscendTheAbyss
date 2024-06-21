import pygame
from pygame.locals import *
from config import *
from functions import *
import pygame_widgets
from pygame_widgets.button import Button

def intro_screen(self):
  self.intro = True
  intro_background = pygame.transform.scale(self.raw_intro_background, (800, 700))
  self.button_font = pygame.font.Font("EBGaramond.ttf", 20)

  # print("Intro screen running")
  self.screen.blit(intro_background, (0, 0))

  def show_display_text():
    title = self.font.render("Ascend the Abyss", True, WHITE)
    title_coords = title.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 5))
    self.screen.blit(title, title_coords)

  def button_is_pressed():
    self.intro = False
    fade_out(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

  while self.intro:
    events = pygame.event.get()
    for event in events:
      # print("pygame events: ", event.type, pygame.QUIT)
      if event.type == pygame.QUIT:
        self.intro = False
        self.running = False
        self.playing = False
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(intro_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    button = Button(
      self.screen,
      self.SCREEN_WIDTH / 2 - 190,
      self.SCREEN_HEIGHT / 2,
      380,
      40,
      text="PLAY",
      inactiveColour=BROWN,
      hoverColour=BROWN_HOVER,
      radius=8,
      textColour=WHITE,
      font=self.button_font,
      onClick=lambda: button_is_pressed()
    )
      
    if self.intro:
      show_display_text()
    else:
      self.screen.fill(BLACK)

    pygame_widgets.update(events)

    pygame.display.update()