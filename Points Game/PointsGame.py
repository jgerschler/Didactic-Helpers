import pygame, time, winsound
from random import randint, sample
from pygame.locals import *

class PointsGame(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.DISPLAY_WIDTH = 1024# add to set_mode if a desired resolution is required.
        self.DISPLAY_HEIGHT = 768

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED=(255,0,0)

        self.finished = False

        self.SoundLoss0 = pygame.mixer.Sound('audio\\Laugh0.ogg')
        self.SoundLoss1 = pygame.mixer.Sound('audio\\Laugh1.ogg')
        self.SoundLoss2 = pygame.mixer.Sound('audio\\Laugh2.ogg')
        self.SoundLoss3 = pygame.mixer.Sound('audio\\Laugh3.ogg')

        self.SoundLossFiles = [self.SoundLoss0,self.SoundLoss1,self.SoundLoss2,self.SoundLoss3]

        self.PointsList = ["10 points","20 points","30 points","40 points","-50 points","LOSE TURN"]

        self.GameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        pygame.display.set_caption("Random Points Game")
        self.GameDisplay.fill(self.WHITE)
        pygame.display.update()

        self.ActualDisplayWidth = self.GameDisplay.get_width()
        self.ActualDisplayHeight = self.GameDisplay.get_height()

    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.BLACK)
        return self.textSurface, self.textSurface.get_rect()

    def message_display(self, text):
        self.largeText = pygame.font.Font('arial.ttf',180)
        self.TextSurf, self.TextRect = self.text_objects(text, self.largeText)
        self.TextRect.center = ((self.ActualDisplayWidth/2),(self.ActualDisplayHeight/2))
        self.GameDisplay.blit(self.TextSurf, self.TextRect)

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        listindex = randint(0,5)
                        if listindex in (4,5):
                            self.GameDisplay.fill(self.RED)
                            self.message_display(self.PointsList[listindex])
                            sample(self.SoundLossFiles,1)[0].play()
                        else:
                            self.GameDisplay.fill(self.WHITE)
                            self.message_display(self.PointsList[listindex])
                            winsound.Beep(2000,500)
                        pygame.display.update()
                        
        pygame.quit()
        quit()

if __name__ == '__main__':
    NewGame = PointsGame()
    NewGame.run()
