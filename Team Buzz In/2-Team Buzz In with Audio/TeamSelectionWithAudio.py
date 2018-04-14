#!/usr/bin/env python
import pygame
import sys


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


        
pygame.init()
pygame.mixer.init()

team_1_sound = pygame.mixer.Sound('audio\\equipo1.ogg')
team_2_sound = pygame.mixer.Sound('audio\\equipo2.ogg')

team_key_dict = {"Team1":[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d],"Team2":[pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h]}

clock = pygame.time.Clock()
finished = False

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen.fill(WHITE)
pygame.display.update()

def wait(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                return

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.finished = True
        if event.type == pygame.KEYUP:
            if event.key in self.team_key_dict["Team1"]:
                self.game_display.fill(TeamBuzzIn.WHITE)
                self.message_display("Team 1",TeamBuzzIn.RED)
                pygame.display.update()
                pygame.mixer.music.play()
                self.wait()
            elif event.key in self.team_key_dict["Team2"]:
                self.game_display.fill(TeamBuzzIn.WHITE)
                self.message_display("Team 2",TeamBuzzIn.YELLOW)
                pygame.display.update()
                pygame.mixer.music.play()
                self.wait()

    self.clock.tick(60)
                
pygame.quit()

