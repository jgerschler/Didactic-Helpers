import pygame, time, winsound
from random import randint, sample
from pygame.locals import *

pygame.init()
pygame.mixer.init()

self.DISPLAY_WIDTH = 1024# add to set_mode if a desired resolution is required.
self.DISPLAY_HEIGHT = 768

self.BLACK = (0,0,0)
self.WHITE = (255,255,255)
self.RED=(255,0,0)

finished = False

self.SoundLoss0 = pygame.mixer.Sound("Laugh0.ogg")
self.SoundLoss1 = pygame.mixer.Sound("Laugh1.ogg")
self.SoundLoss2 = pygame.mixer.Sound("Laugh2.ogg")
self.SoundLoss3 = pygame.mixer.Sound("Laugh3.ogg")

self.SoundLossFiles = [self.SoundLoss0,self.SoundLoss1,self.SoundLoss2,self.SoundLoss3]

self.PointsList = ["10 points","20 points","30 points","40 points","-50 points","LOSE TURN"]

self.GameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("""Jared's ESL Wheel of Fortune""")
self.GameDisplay.fill(self.WHITE)
pygame.display.update()

actualDisplayWidth = self.GameDisplay.get_width()
actualDisplayHeight = self.GameDisplay.get_height()

def text_objects(text, font):
    textSurface = font.render(text, True, self.BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('arial.ttf',180)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((actualDisplayWidth/2),(actualDisplayHeight/2))
    self.GameDisplay.blit(TextSurf, TextRect)

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                listindex = randint(0,5)
                if listindex in (4,5):
                    self.GameDisplay.fill(self.RED)
                    message_display(self.PointsList[listindex])
                    sample(self.SoundLossFiles,1)[0].play()
                else:
                    self.GameDisplay.fill(self.WHITE)
                    message_display(self.PointsList[listindex])
                    winsound.Beep(2000,500)
                pygame.display.update()
                
pygame.quit()
quit()

