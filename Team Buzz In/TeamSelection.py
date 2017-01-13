import pygame, sys

class TeamBuzzIn(object):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.TeamFile = 'ping.ogg'
        pygame.mixer.music.load(self.TeamFile)

        self.DISPLAY_WIDTH = 1024
        self.DISPLAY_HEIGHT = 768

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GRAY = (184,184,184)
        self.RED = (255,0,0)
        self.GREEN = (50,150,50)
        self.YELLOW = (255,200,0)
        self.BLUE = (0,100,255)

        self.TeamKeyDict = {"Team1":[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d],"Team2":[pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h],
                        "Team3":[pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l],"Team4":[pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p],
                        "Team5":[pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t],"Team6":[pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x]}

        self.clock = pygame.time.Clock()
        self.finished = False

        self.GameDisplay = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.GameDisplay.fill(self.WHITE)
        pygame.display.update()

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    return

    def text_objects(self, text, font, color):
        self.textSurface = font.render(text, True, color)
        return self.textSurface, self.textSurface.get_rect()

    def message_display(self, text, color):
        self.largeText = pygame.font.Font('arial.ttf',144)
        self.TextSurf, self.TextRect = self.text_objects(text, self.largeText, color)
        self.TextRect.center = ((self.DISPLAY_WIDTH/2),(self.DISPLAY_HEIGHT/2))
        self.GameDisplay.blit(self.TextSurf, self.TextRect)

        pygame.display.update()

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key in self.TeamKeyDict["Team1"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 1",self.RED)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.TeamKeyDict["Team2"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 2",self.YELLOW)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.TeamKeyDict["Team3"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 3",self.GREEN)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.TeamKeyDict["Team4"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 4",self.BLUE)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.TeamKeyDict["Team5"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 5",self.BLACK)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.TeamKeyDict["Team6"]:
                        self.GameDisplay.fill(self.WHITE)
                        self.message_display("Team 6",self.GRAY)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()

            self.clock.tick(60)
                        
        pygame.quit()
        quit()

if __name__ == '__main__':
    print("")
    print("Press spacebar to start listening for buzz-ins.")
    print("")
    NewGame = TeamBuzzIn()
    NewGame.run()
