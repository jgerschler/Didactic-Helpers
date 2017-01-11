import pygame, time
from random import randint

class RandomNumberGenerator(object):
    def __init__(self, LowerLimit, UpperLimit)
        self.DISPLAY_WIDTH = 1024
        self.DISPLAY_HEIGHT = 768

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.Finished = False

        pygame.init()
        
        self.GameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption('Random Number Generator')
        self.GameDisplay.fill(self.WHITE)
        pygame.display.update()
        
    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, black)
        return self.textSurface, self.textSurface.get_rect()

    def message_display(self, text):
        self.LargeText = pygame.font.Font('arial.ttf',432)
        self.TextSurf, self.TextRect = self.text_objects(text, self.LargeText)
        self.TextRect.center = ((self.DISPLAY_WIDTH/2),(self.DISPLAY_HEIGHT/2))
        self.GameDisplay.blit(self.TextSurf, self.TextRect)

    def main_loop(self):
        while not self.Finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        GameDisplay.fill(white)
                        self.message_display(str(randint(lowint,highint)))
                        pygame.display.update()
                        
        pygame.quit()
        quit()        
        


lowint = int(raw_input('Lower Limit?'))
highint = int(raw_input('Upper Limit?'))

