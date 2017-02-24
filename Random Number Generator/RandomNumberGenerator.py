#!/usr/bin/env python
import pygame, time, argparse
from random import randint

class RandomNumberGenerator(object):
    DISPLAY_WIDTH = 1024
    DISPLAY_HEIGHT = 768

    BLACK = (0,0,0)
    WHITE = (255,255,255)

    def __init__(self, lower_limit, upper_limit):
        self.finished = False
        
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        pygame.init()
        
        self.game_display = pygame.display.set_mode((RandomNumberGenerator.DISPLAY_WIDTH, RandomNumberGenerator.DISPLAY_HEIGHT))
        pygame.display.set_caption('Random Number Generator')
        self.game_display.fill(RandomNumberGenerator.WHITE)
        pygame.display.update()
        
    def text_objects(self, text, font):
        self.text_surface = font.render(text, True, RandomNumberGenerator.BLACK)
        return self.text_surface, self.text_surface.get_rect()

    def message_display(self, text):
        self.large_text = pygame.font.Font('arial.ttf',432)
        self.text_surf, self.text_rect = self.text_objects(text, self.large_text)
        self.text_rect.center = ((RandomNumberGenerator.DISPLAY_WIDTH/2),(RandomNumberGenerator.DISPLAY_HEIGHT/2))
        self.game_display.blit(self.text_surf, self.text_rect)

    def main_loop(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.game_display.fill(RandomNumberGenerator.WHITE)
                        self.message_display(str(randint(self.lower_limit,self.upper_limit)))
                        pygame.display.update()
                        
        pygame.quit()
        quit()        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RandomNumberGenerator.py v1.0 A large-font graphical random number generator. (c) J.J. Gerschler")
    parser.add_argument("-l", "--lower", help="Lower limit (inclusive)")
    parser.add_argument("-u", "--upper", help="Upper limit (inclusive)")
    args = parser.parse_args()
    
    print("")
    print("When screen loads, press the spacebar to generate a random number!")
    print("")
    new_number = RandomNumberGenerator(int(args.lower),int(args.upper))
    new_number.main_loop()
