import pygame
from pygame.locals import *
from config import *
from functions import *
from components import *
from player import *
from mob import *
import random
from threading import Timer

def fight_screen(main, max_enemy_hp, mob_url):
  fight = True
  discard_screen = False
  remaining_screen = False
  victory = False

  damage_received = 0
  damage_inflicted = 0

  action_type = "Idle"
  attack_cards = ["BladeDance", "LimitBreak", "PerfectStrike", "BodySlam", "Carnage"]
  current_turn = "player"

  remaining_cards = ALL_CARDS.copy()
  random.shuffle(remaining_cards)
  discarded_cards = []
  current_deck = remaining_cards[0:3]
  del remaining_cards[0:3]

  deck_title = pygame.font.Font("EBGaramond.ttf", 45)

  fight_background = pygame.transform.scale(main.raw_fight_background, (main.SCREEN_WIDTH, main.SCREEN_HEIGHT))
  enemy_hp = max_enemy_hp

  fade_in(main, main.SCREEN_WIDTH, main.SCREEN_HEIGHT, fight_background)

  discard_pile = DiscardPile(main.screen)  
  remaining_pile = RemainingPile(main.screen)

  def display_black_bg(screen_type):
    nonlocal remaining_screen, discard_screen
    main.screen.blit(black_bg, (0, 0))
    if screen_type == "r":
      remaining_screen = True
    else:
      discard_screen = True
  
  def display_enemy_turn():
    title = deck_title.render("Enemy's Turn", True, WHITE)
    title_coords = title.get_rect(center=(main.SCREEN_WIDTH / 2, 40))
    main.screen.blit(title, title_coords)

  def attack(card):
    nonlocal enemy_hp, fight, victory, damage_received, damage_inflicted, action_type
    discarded_cards.append(card.card_type)
    current_deck.remove(card.card_type)

    enemy_hp = card.enemy_hp
    main.player_hp = card.main.player_hp
    main.player_armor = card.main.player_armor
    damage_received += card.damage_received
    damage_inflicted += card.damage_inflicted

    if enemy_hp <= 0:
      victory = True
      fight = False
    
    if main.player_hp <= 0:
      victory = False
      fight = False

  def switch_turn():
    nonlocal enemy_hp, fight, victory, damage_inflicted, damage_received

    chosen_cards = random.sample(ALL_CARDS, 3)

    for chosen_card in chosen_cards:
      if chosen_card == "Feed":
        if max_enemy_hp - enemy_hp > 7:
          enemy_hp += 7
          damage_inflicted -= 7
      if chosen_card == "BladeDance":
        if main.player_armor > 0:
          main.player_armor -= 6
          if main.player_armor < 0:
            main.player_hp -= abs(main.player_armor)
            damage_received += abs(main.player_armor)
        else:
          main.player_hp -= 6
          damage_received += 6
      if chosen_card == "LimitBreak":
        if main.player_armor > 0:
          main.player_armor -= 20
          if main.player_armor < 0:
            main.player_hp -= abs(main.player_armor)
            damage_received += abs(main.player_armor)
        else:
          main.player_hp -= 20
          damage_received += 20
        enemy_hp -= 5
      if chosen_card == "PerfectStrike":
        if main.player_armor > 0:
          main.player_armor -= 12
          if main.player_armor < 0:
            main.player_hp -= abs(main.player_armor)
            damage_received += abs(main.player_armor)
        else:
          main.player_hp -= 12
          damage_received += 12
      if chosen_card == "BodySlam":
        if main.player_armor > 0:
          main.player_armor -= 10
          if main.player_armor < 0:
            main.player_hp -= abs(main.player_armor)
            damage_received += abs(main.player_armor)
        else:
          main.player_hp -= 10
          damage_received += 10
      if chosen_card == "Carnage":
        if main.player_armor > 0:
          main.player_armor -= 30
          if main.player_armor < 0:
            main.player_hp -= abs(main.player_armor)
            damage_received += abs(main.player_armor)
        else:
          main.player_hp -= 30
          damage_received += 30
        enemy_hp -= 15
    
    if enemy_hp <= 0:
      victory = True
      fight = False

    if main.player_hp <= 0:
      victory = False
      fight = False

  player = Player(main.screen, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)
    
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

    Mob(mob_url, main.screen, main.SCREEN_WIDTH, main.SCREEN_HEIGHT)

    discard_pile.draw(main.SCREEN_WIDTH, main.SCREEN_HEIGHT)
    remaining_pile.draw(main.SCREEN_HEIGHT)
    
    left_card = None
    mid_card = None
    right_card = None 
    ml_card = None
    mr_card = None

    if current_turn == "player":
      if len(current_deck) == 3:
        left_card = Card("left", current_deck[0], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
        mid_card = Card("mid", current_deck[1], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
        right_card = Card("right", current_deck[2], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
      elif len(current_deck) == 2:
        ml_card = Card("ml", current_deck[0], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
        mr_card = Card("mr", current_deck[1], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
      elif len(current_deck) == 1:
        mid_card = Card("mid", current_deck[0], main.SCREEN_WIDTH, main.SCREEN_HEIGHT, main.screen, main, enemy_hp)
    elif current_turn == "enemy":
      display_enemy_turn()

    if left_card and left_card.is_pressed():
      if left_card.card_type in attack_cards:
        action_type = "Attack"
        def switch():
          nonlocal action_type 
          action_type = "Idle"
        t = Timer(1.0, switch)
        t.start()
      attack(left_card)

    if mid_card and mid_card.is_pressed():
      if mid_card.card_type in attack_cards:
        action_type = "Attack"
        def switch():
          nonlocal action_type 
          action_type = "Idle"
        t = Timer(1.0, switch)
        t.start()
      attack(mid_card)
      if len(current_deck) == 0:
        current_turn = "enemy"
        def switch():
          nonlocal current_turn 
          current_turn = "player"
          switch_turn()
        t = Timer(3.0, switch)
        t.start()
        if len(remaining_cards) >= 3:
          current_deck = remaining_cards[0:3]
          del remaining_cards[0:3]
        else:
          if len(remaining_cards) == 0:
            remaining_cards = ALL_CARDS
            random.shuffle(remaining_cards)
            discarded_cards = []
            current_deck = remaining_cards[0:3]
          else:
            current_deck = remaining_cards
            remaining_cards = []

    if right_card and right_card.is_pressed():
      if right_card.card_type in attack_cards:
        action_type = "Attack"
        def switch():
          nonlocal action_type 
          action_type = "Idle"
        t = Timer(1.0, switch)
        t.start()
      attack(right_card)

    if ml_card and ml_card.is_pressed():
      if ml_card.card_type in attack_cards:
        action_type = "Attack"
        def switch():
          nonlocal action_type 
          action_type = "Idle"
        t = Timer(1.0, switch)
        t.start()
      attack(ml_card)

    if mr_card and mr_card.is_pressed():
      if mr_card.card_type in attack_cards:
        action_type = "Attack"
        def switch():
          nonlocal action_type 
          action_type = "Idle"
        t = Timer(1.0, switch)
        t.start()
      attack(mr_card)

    if left_card: left_card.is_hovered()
    if mid_card: mid_card.is_hovered()
    if right_card: right_card.is_hovered()
    if ml_card: ml_card.is_hovered()
    if mr_card: mr_card.is_hovered()

    if remaining_pile.is_pressed():
      display_black_bg("r")

    if discard_pile.is_pressed():
      display_black_bg("d")

    player.update(action_type)
    player.draw()

    pygame.display.update()

    if fight == False:
      return [victory, damage_inflicted, damage_received]
