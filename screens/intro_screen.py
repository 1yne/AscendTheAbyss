import pygame
from pygame.locals import *
from config import *
from functions import *
from components import *

def intro_screen(self):
  self.intro = True
  intro_background = pygame.transform.scale(self.raw_intro_background, (800, 700))

  self.screen.blit(intro_background, (0, 0))

  def show_display_text():
    title = self.font.render("Ascend the Abyss", True, WHITE)
    title_coords = title.get_rect(center=(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 5))
    self.screen.blit(title, title_coords)

  while self.intro:
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        self.intro = False
        self.running = False
        self.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        self.screen.blit(pygame.transform.scale(intro_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    play_button = Button(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2, 380, 120, WHITE, BROWN, 'PLAY', 24, self.screen, self, "./images/PlayButton.png")

    if play_button.is_pressed():
      self.intro = False
      
    if play_button.is_hovering():
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    if play_button.is_not_hovering():
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
      
    if self.intro:
      show_display_text()
    else:
      self.screen.fill(BLACK)

    pygame.display.update()