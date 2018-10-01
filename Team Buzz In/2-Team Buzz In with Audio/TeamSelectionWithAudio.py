#!/usr/bin/env python
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
finished = False
        
pygame.init()
pygame.mixer.init()

team_1_sound = pygame.mixer.Sound('audio\\equipo1.ogg')
team_2_sound = pygame.mixer.Sound('audio\\equipo2.ogg')
incorrect_sound = pygame.mixer.Sound('audio\\incorrect.ogg')
correct_sound = pygame.mixer.Sound('audio\\correct.ogg')
sad_sound = pygame.mixer.Sound('audio\\trombone.ogg')

left_arrow = pygame.image.load('images\\left_arrow.png')
right_arrow = pygame.image.load('images\\right_arrow.png')

team_key_dict = {"Team1":[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d],
                 "Team2":[pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h]}

clock = pygame.time.Clock()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen_width = screen.get_width()
screen_height = screen.get_height()

font = pygame.font.Font(None, 512)

team_text_1 = font.render("1", 1, (255, 0, 0))
team_text_rect_1 = team_text_1.get_rect()
team_text_rect_1.center = (screen_width / 2, screen_height / 2)

team_text_2 = font.render("2", 1, (255, 0, 0))
team_text_rect_2 = team_text_2.get_rect()
team_text_rect_2.center = (screen_width / 2, screen_height / 2)

left_arrow_rect = left_arrow.get_rect()
right_arrow_rect = right_arrow.get_rect()

left_arrow_rect.midleft = (30, screen_height / 2)
right_arrow_rect.midright = (screen_width - 30, screen_height / 2)

screen.fill(WHITE)
pygame.display.update()


def wait(finished):
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_l:
                    screen.fill(WHITE)
                    pygame.display.update()
                    return
                if event.key == pygame.K_i:
                    incorrect_sound.play()
                if event.key == pygame.K_j:
                    sad_sound.play()
                if event.key == pygame.K_k:
                    correct_sound.play()
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
                screen.blit(team_text_1, team_text_rect_1)
                screen.blit(left_arrow, left_arrow_rect)
                pygame.display.update()
                team_1_sound.play()
                finished = wait(finished)
            if event.key in team_key_dict["Team2"]:
                screen.fill(WHITE)
                screen.blit(team_text_2, team_text_rect_2)
                screen.blit(right_arrow, right_arrow_rect)
                pygame.display.update()
                team_2_sound.play()
                finished = wait(finished)
            if event.key == pygame.K_i:
                incorrect_sound.play()
            if event.key == pygame.K_j:
                sad_sound.play()
            if event.key == pygame.K_k:
                correct_sound.play()
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True

    clock.tick(60)
                
pygame.quit()

