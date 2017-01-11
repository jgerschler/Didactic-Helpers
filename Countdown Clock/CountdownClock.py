import pygame, time, sys
from random import randint

class CountdownClock(object):
    def __init__(self, startTime):
        self.display_width = 1024
        self.display_height = 768

        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)

        self.finished = False

        self.GameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.pygame.display.set_caption('Countdown Clock')
        self.GameDisplay.fill(self.white)
        self.pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def red_text_objects(self, text, font):
        textSurface = font.render(text, True, red)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('arial.ttf',240)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        self.GameDisplay.blit(TextSurf, TextRect)

    def urgent_message_display(self, text):
        largeText = pygame.font.Font('arial.ttf',240)
        TextSurf, TextRect = red_text_objects(text, largeText)
        TextRect.center = ((self.display_width/2),(self.display_height/2))
        self.GameDisplay.blit(TextSurf, TextRect)    

    def times_up(self):
        pygame.quit()
        sys.exit()

    def main_loop(self):
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        for t in range(starttime,-1,-1):
                            GameDisplay.fill(white)
                            minutes = t / 60
                            seconds = t % 60
                            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                            if t < 10:
                                urgent_message_display(sf)
                            else:
                                message_display(sf)
                            pygame.event.get()
                            time.sleep(1)
                            pygame.display.update()
                            
                        TimesUpSound.play()
                        time.sleep(4)
                        times_up()
                        
        pygame.quit()
        quit()


starttime = int(raw_input('How many seconds?'))


TimesUpFile = "TimesUp.ogg"
pygame.init()
pygame.mixer.init()
TimesUpSound = pygame.mixer.Sound(TimesUpFile)