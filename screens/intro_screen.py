import pygame
from pygame.locals import *
from config import *
from components import *
from functions import *

def intro_screen(self):
  intro = True
  intro_background = pygame.transform.scale(self.raw_intro_background, (800, 700))

  # print("Intro screen running")
  self.screen.blit(intro_background, (0, 0))

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
        self.screen.blit(pygame.transform.scale(intro_background, event.dict['size']), (0, 0))
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = event.dict['size']

    play_button = Button(self.SCREEN_WIDTH / 2, self.SCREEN_HEIGHT / 2, 380, 120, WHITE, BROWN, 'PLAY', 24,  "./images/ButtonBackgroundBrown.png")

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    if play_button.is_hovering():
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    if play_button.is_not_hovering():
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
  
    if play_button.is_pressed(mouse_pos, mouse_pressed):
      intro = False
      pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
      fade_out(self, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
      
    if intro:
      show_display_text()
      self.screen.blit(play_button.image, play_button.rect)
    else:
      self.screen.fill(BLACK)

    pygame.display.update()