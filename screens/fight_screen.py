import pygame
from pygame.locals import *
import pygame_widgets
from pygame_widgets.button import Button as PyButton
from config import *
from functions import *
from components import *
from player import *
from mob import *
import random

def fight_screen(main, max_enemy_hp, mob_url):
  fight = True
  discard_screen = False
  remaining_screen = False
  current_turn = "player"

  button_font = pygame.font.Font("EBGaramond.ttf", 20)

  remaining_cards = ["BladeDance", "Defend", "Feed", "LimitBreak", "PerfectStrike", "StrikeCard"]
  discarded_cards = []

  deck_title = pygame.font.Font("EBGaramond.ttf", 45)

  fight_background = pygame.transform.scale(main.raw_fight_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
  enemy_hp = 10

  fade_in(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, fight_background)

  discard_pile = DiscardPile(main.screen)  
  remaining_pile = RemainingPile(main.screen)

  def switch_turn():
    nonlocal current_turn, enemy_hp
    current_turn = "enemy"

    title = deck_title.render("Enemy's Turn", True, WHITE)
    title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, 40))
    main.screen.blit(title, title_coords)

    chosen_cards = random.sample(ALL_CARDS, 3)
    for chosen_card in chosen_cards:
      if chosen_card == "Feed":
        if max_enemy_hp - enemy_hp > 7:
          enemy_hp += 7
      if chosen_card == "BladeDance":
        if main.player_armor > 0:
          main.player_armor -= 6
          main.player_hp -= abs(main.player_armor)
        else:
          main.player_hp -= 6
      if chosen_card == "LimitBreak":
        if main.player_armor > 0:
          main.player_armor -= 20
          main.player_hp -= abs(main.player_armor)
        else:
          main.player_hp -= 20
        enemy_hp -= 5
      if chosen_card == "PerfectStrike":
        if main.player_armor > 0:
          main.player_armor -= 12
          main.player_hp -= abs(main.player_armor)
        else:
          main.player_hp -= 12
      if chosen_card == "StrikeCard":
        if main.player_armor > 0:
          main.player_armor -= 6
          main.player_hp -= abs(main.player_armor)
        else:
          main.player_hp -= 6
    
  while fight:
    while remaining_screen:
      events = pygame.event.get()

      for event in events:
        if event.type == pygame.QUIT:
          fight = False
          main.running = False
          main.playing = False
          pygame.quit()
        elif event.type == VIDEORESIZE:
          main.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
          main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

      back_arrow = BackArrow(main.screen, "left", main.SCREEN_WIDTH)

      title = deck_title.render("Remaining Cards", True, WHITE)
      title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, 40))
      main.screen.blit(title, title_coords)

      CardGrid(remaining_cards, main.screen, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, "r")

      if back_arrow.is_pressed():
        remaining_screen = False
        main.screen.blit(fight_background, (0, 0))

      pygame.display.update()

    ###############################
      
    while discard_screen:
      events = pygame.event.get()

      for event in events:
        if event.type == pygame.QUIT:
          fight = False
          main.running = False
          main.playing = False
          pygame.quit()
        elif event.type == VIDEORESIZE:
          main.screen.blit(pygame.transform.scale(black_bg, event.dict['size']), (0, 0))
          main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

      back_arrow = BackArrow(main.screen, "right", main.SCREEN_WIDTH)

      title = deck_title.render("Discarded Cards", True, WHITE)
      title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, 40))
      main.screen.blit(title, title_coords)

      CardGrid(discarded_cards, main.screen, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, "d")

      if back_arrow.is_pressed():
        discard_screen = False
        main.screen.blit(fight_background, (0, 0))

      pygame.display.update()

    ##############################
      
    events = pygame.event.get()
    for event in events:
      if event.type == pygame.QUIT:
        fight = False
        main.running = False
        main.playing = False
        pygame.quit()
      elif event.type == VIDEORESIZE:
        main.screen.blit(pygame.transform.scale(fight_background, event.dict['size']), (0, 0))
        main.SCREEN_WIDTH, main.SCREEN_HEIGHT = event.dict['size']

    player_health_bar = PlayerHealthBar(main.screen, main.player_hp, main.player_armor)
    enemy_health_bar = EnemyHealthBar(main.screen, enemy_hp, max_enemy_hp)
    
    black_bg = pygame.Surface((main.SCREEN_WIDTH, main.SCREEN_HEIGHT), pygame.SRCALPHA)
    black_bg.fill((0, 0, 0, 200))

    fight_background = pygame.transform.scale(main.raw_fight_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
    main.screen.blit(fight_background, (0, 0))

    player_health_bar.draw(main.screen)
    enemy_health_bar.draw(main.screen, main.SCREEN_WIDTH)

    Mob(mob_url, main.screen, main.SCREEN_WIDTH)

    end_turn = PyButton(
      main.screen,
      main.SCREEN_WIDTH - 300,
      main.SCREEN_HEIGHT - 300,
      160,
      40,
      text="End Turn",
      inactiveColour=GREY,
      radius=8,
      textColour=WHITE,
      font=button_font,
      onClick=lambda: switch_turn()
    )

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    discard_pile.draw(main.SCREEN_WIDTH, main.SCREEN_HEIGHT)
    remaining_pile.draw(main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    left_card = Card("left", remaining_cards[0], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main)
    mid_card = Card("mid", remaining_cards[1], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main)
    right_card = Card("right", remaining_cards[2], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main)

    if left_card.is_pressed():
      remaining_cards.remove(left_card.card_type)
      discarded_cards.append(left_card.card_type)
      pygame.time.delay(250)

    if mid_card.is_pressed():
      remaining_cards.remove(mid_card.card_type)
      discarded_cards.append(mid_card.card_type)
      pygame.time.delay(250)

    if right_card.is_pressed():
      remaining_cards.remove(right_card.card_type)
      discarded_cards.append(right_card.card_type)
      pygame.time.delay(250)

    if remaining_pile.is_pressed(mouse_pos, mouse_pressed):
      main.screen.blit(black_bg, (0, 0))
      remaining_screen = True

    if discard_pile.is_pressed(mouse_pos, mouse_pressed):
      main.screen.blit(black_bg, (0, 0))
      discard_screen = True

    pygame_widgets.update(events)
    pygame.display.update()
