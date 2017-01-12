import pygame, time, argparse
from random import randint

class RandomNumberGenerator(object):
    def __init__(self, LowerLimit, UpperLimit):
        self.DISPLAY_WIDTH = 1024
        self.DISPLAY_HEIGHT = 768

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

        self.Finished = False
        
        self.LowerLimit = LowerLimit
        self.UpperLimit = UpperLimit

        pygame.init()
        
        self.GameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        pygame.display.set_caption('Random Number Generator')
        self.GameDisplay.fill(self.WHITE)
        pygame.display.update()
        
    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.BLACK)
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
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display(str(randint(self.LowerLimit,self.UpperLimit)))
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
    NewNumber = RandomNumberGenerator(int(args.lower),int(args.upper))
    NewNumber.main_loop()