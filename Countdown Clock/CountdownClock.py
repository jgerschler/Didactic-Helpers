#!/usr/bin/env python
import pygame, time, sys, argparse
from random import randint

class CountdownClock(object):
    DISPLAY_WIDTH = 1024
    DISPLAY_HEIGHT = 768

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    
    def __init__(self, start_time):
        self.finished = False
        self.start_time = start_time
        
        pygame.init()
        pygame.mixer.init()
        self.times_up_file = "TimesUp.ogg"
        self.times_up_sound = pygame.mixer.Sound(self.times_up_file)
        
        self.game_display = pygame.display.set_mode((CountdownClock.DISPLAY_WIDTH, CountdownClock.DISPLAY_HEIGHT))
        pygame.display.set_caption('Countdown Clock')
        self.game_display.fill(CountdownClock.WHITE)
        pygame.display.update()

    def text_objects(self, text, font):
        self.text_surface = font.render(text, True, CountdownClock.BLACK)
        return self.text_surface, self.text_surface.get_rect()

    def red_text_objects(self, text, font):
        self.text_surface = font.render(text, True, CountdownClock.RED)
        return self.text_surface, self.text_surface.get_rect()

    def message_display(self, text):
        self.large_text = pygame.font.Font('Arial.ttf',240)
        self.text_surf, self.text_rect = self.text_objects(text, self.large_text)
        self.text_rect.center = ((CountdownClock.DISPLAY_WIDTH/2),(CountdownClock.DISPLAY_HEIGHT/2))
        self.game_display.blit(self.text_surf, self.text_rect)

    def urgent_message_display(self, text):
        self.large_text = pygame.font.Font('Arial.ttf',240)
        self.text_surf, self.text_rect = self.red_text_objects(text, self.large_text)
        self.text_rect.center = ((CountdownClock.DISPLAY_WIDTH/2),(CountdownClock.DISPLAY_HEIGHT/2))
        self.game_display.blit(self.text_surf, self.text_rect)    

    def times_up(self):
        pygame.quit()
        sys.exit()

    def main_loop(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        for t in range(self.start_time,-1,-1):
                            self.game_display.fill(CountdownClock.WHITE)
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
                            
                        self.times_up_sound.play()
                        time.sleep(4)
                        self.times_up()
                        
        pygame.quit()
        quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CountdownClock.py v1.0 A large-font graphical countdown clock. (c) J.J. Gerschler")
    parser.add_argument("-s", "--seconds", help="Number of seconds to count down.")
    args = parser.parse_args()
    
    print("")
    print("When screen loads, press the spacebar to start the countdown!")
    print("")
    new_clock = CountdownClock(int(args.seconds))
    new_clock.main_loop()

