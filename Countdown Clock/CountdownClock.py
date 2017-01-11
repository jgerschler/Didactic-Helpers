import pygame, time, sys
from random import randint

class CountdownClock(object):
    def __init__(self, StartTime):
        self.DISPLAY_WIDTH = 1024
        self.DISPLAY_HEIGHT = 768

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)

        self.Finished = False
        self.StartTime = StartTime
        
        pygame.init()
        pygame.mixer.init()
        self.TimesUpFile = "TimesUp.ogg"
        self.TimesUpSound = pygame.mixer.Sound(self.TimesUpFile)
        
        self.GameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption('Countdown Clock')
        self.GameDisplay.fill(self.WHITE)
        pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.BLACK)
        return textSurface, textSurface.get_rect()

    def red_text_objects(self, text, font):
        textSurface = font.render(text, True, self.RED)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        largeText = pygame.font.Font('arial.ttf',240)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
        self.GameDisplay.blit(TextSurf, TextRect)

    def urgent_message_display(self, text):
        largeText = pygame.font.Font('arial.ttf',240)
        TextSurf, TextRect = red_text_objects(text, largeText)
        TextRect.center = ((self.DISPLAY_WIDTH/2),(self.DISPLAY_HEIGHT/2))
        self.GameDisplay.blit(TextSurf, TextRect)    

    def times_up(self):
        pygame.quit()
        sys.exit()

    def main_loop(self):
        while not self.Finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        for t in range(self.StartTime,-1,-1):
                            self.GameDisplay.fill(self.WHITE)
                            minutes = t / 60
                            seconds = t % 60
                            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
                            if t < 10:
                                self.urgent_message_display(sf)
                            else:
                                self.message_display(sf)
                            pygame.event.get()
                            time.sleep(1)
                            pygame.display.update()
                            
                        self.TimesUpSound.play()
                        time.sleep(4)
                        self.times_up()
                        
        pygame.quit()
        quit()


#starttime = int(raw_input('How many seconds?'))
NewClock = CountdownClock(10)
NewClock.main_loop()



