#!/usr/bin/env python
import pygame, time, winsound
from random import randint, sample
from pygame.locals import *

class PointsGame(object):
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED=(255,0,0)
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.finished = False

        self.sound_loss_0 = pygame.mixer.Sound('audio\\Laugh0.ogg')
        self.sound_loss_1 = pygame.mixer.Sound('audio\\Laugh1.ogg')
        self.sound_loss_2 = pygame.mixer.Sound('audio\\Laugh2.ogg')
        self.sound_loss_3 = pygame.mixer.Sound('audio\\Laugh3.ogg')
        self.sound_loss_4 = pygame.mixer.Sound('audio\\Laugh4.ogg')
        self.sound_loss_5 = pygame.mixer.Sound('audio\\Laugh5.ogg')

        self.sound_loss_files = [self.sound_loss_0,self.sound_loss_1,
                                 self.sound_loss_2,self.sound_loss_3,
                                 self.sound_loss_4,self.sound_loss_5]

        self.points_list = ["10 points","20 points","30 points","40 points","-50 points","LOSE TURN"]

        self.game_display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Random Points Game")
        self.game_display.fill(PointsGame.WHITE)
        pygame.display.update()

        self.actual_display_width = self.game_display.get_width()
        self.actual_display_height = self.game_display.get_height()

    def text_objects(self, text, font):
        self.text_surface = font.render(text, True, PointsGame.BLACK)
        return self.text_surface, self.text_surface.get_rect()

    def message_display(self, text):
        self.large_text = pygame.font.Font('arial.ttf',180)
        self.text_surf, self.text_rect = self.text_objects(text, self.large_text)
        self.text_rect.center = ((self.actual_display_width/2),(self.actual_display_height/2))
        self.game_display.blit(self.text_surf, self.text_rect)

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        listindex = randint(0,5)
                        if listindex in (4,5):
                            self.game_display.fill(PointsGame.RED)
                            self.message_display(self.points_list[listindex])
                            sample(self.sound_loss_files,1)[0].play()
                        else:
                            self.game_display.fill(PointsGame.WHITE)
                            self.message_display(self.points_list[listindex])
                            winsound.Beep(2000,500)
                        pygame.display.update()
                        
        pygame.quit()
        quit()

if __name__ == '__main__':
    NewGame = PointsGame()
    NewGame.run()
