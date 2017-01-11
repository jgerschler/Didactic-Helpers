import pygame, time, sys
from random import randint

class countdownClock(object):
    def __init__(self, startTime):
        





timeupfile = "timesUp.ogg"


pygame.init()

pygame.mixer.init()

timeupsound = pygame.mixer.Sound(timeupfile)

display_width = 1024
display_height = 768

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

finished = False

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Countdown Clock')
gameDisplay.fill(white)
pygame.display.update()

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
    gameDisplay.blit(TextSurf, TextRect)

def urgent_message_display(self, text):
    largeText = pygame.font.Font('arial.ttf',240)
    TextSurf, TextRect = red_text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)    

def time_up(self):
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
                        gameDisplay.fill(white)
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
                        
                    timeupsound.play()
                    time.sleep(4)
                    time_up()
                    
    pygame.quit()
    quit()


starttime = int(raw_input('How many seconds?'))

