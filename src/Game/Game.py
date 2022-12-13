import random
from src.Game.Player import Player, CarPlayer
import pygame


class Game:
    def __init__(self, screen, clock, AIs):
        self.screen: pygame.Surface = screen
        self.clock = clock
        rand = random.choice([1, 0])   # alternate between player 1 and 2
        self.player_1 = CarPlayer(AIs[0], rand)
        # self.player_2 = Player(AIs[1], 1-rand)
        self.dt = 0

    def start(self):
        self.game_loop()

    def draw_background(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.line(self.screen, (0, 255, 255), (0, 480), (1080, 480))

    def draw_hud(self):
        pass

    def input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player_1.car.activate_speeding(1)
            elif event.key == pygame.K_DOWN:
                self.player_1.car.activate_speeding(-1)
            elif event.key == pygame.K_b:
                self.player_1.shoot()

            if event.key == pygame.K_SPACE:
                self.player_1.car.activate_brakes()
                print("frena")

            if event.key == pygame.K_RIGHT:
                self.player_1.car.activate_steering(-1, True)
            elif event.key == pygame.K_LEFT:
                self.player_1.car.activate_steering(1, True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player_1.car.activate_speeding(0, False)
            if event.key == pygame.K_SPACE:
                self.player_1.car.activate_brakes(0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.player_1.car.activate_steering(0, False)

    def refresh(self):
        self.draw_background()
        self.player_1.draw(self.screen)
        # self.player_2.draw(self.screen)
        pygame.display.update()

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                self.input(event)

            self.player_1.update(self.dt)
            self.refresh()
            self.dt = self.clock.tick()/1000
