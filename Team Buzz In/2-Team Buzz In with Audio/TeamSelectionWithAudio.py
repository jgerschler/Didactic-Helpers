#!/usr/bin/env python
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
finished = False
        
pygame.init()
pygame.mixer.init()

team_1_sound = pygame.mixer.Sound('audio\\equipo1.ogg')
team_2_sound = pygame.mixer.Sound('audio\\equipo2.ogg')

team_key_dict = {"Team1":[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d],"Team2":[pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h]}

clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_width()

font = pygame.font.Font(None, 128)

screen.fill(WHITE)
pygame.display.update()


def wait(finished):
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                return
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                finished = True
    return finished
                
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key in team_key_dict["Team1"]:
                screen.fill(WHITE)
                team_text = font.render("1", 1, (255, 0, 0))
                team_text_rect = team_text.get_rect()
                team_text_rect.topright = (screen_width, 0)
                screen.blit(team_text, team_text_rect)
                pygame.display.update()
                team_1_sound.play()
                finished = wait(finished)
            if event.key in team_key_dict["Team2"]:
                screen.fill(WHITE)
                team_text = font.render("2", 1, (255, 0, 0))
                team_text_rect = team_text.get_rect()
                team_text_rect.topright = (screen_width, 0)
                screen.blit(team_text, team_text_rect)
                pygame.display.update()
                team_2_sound.play()
                finished = wait(finished)
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True

    clock.tick(60)
                
pygame.quit()

