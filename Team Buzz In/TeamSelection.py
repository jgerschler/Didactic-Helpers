import pygame, sys

class TeamBuzzIn(object):
    DISPLAY_WIDTH = 1024
    DISPLAY_HEIGHT = 768

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GRAY = (184,184,184)
    RED = (255,0,0)
    GREEN = (50,150,50)
    YELLOW = (255,200,0)
    BLUE = (0,100,255)
    
    buzz_sound = 'ping.ogg'
        
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        pygame.mixer.music.load(TeamBuzzIn.buzz_sound)

        self.team_key_dict = {"Team1":[pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d],"Team2":[pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h],
                        "Team3":[pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l],"Team4":[pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p],
                        "Team5":[pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t],"Team6":[pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x]}

        self.clock = pygame.time.Clock()
        self.finished = False

        self.game_display = pygame.display.set_mode((TeamBuzzIn.DISPLAY_WIDTH, TeamBuzzIn.DISPLAY_HEIGHT))
        self.game_display.fill(TeamBuzzIn.WHITE)
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
        self.text_surface = font.render(text, True, color)
        return self.text_surface, self.text_surface.get_rect()

    def message_display(self, text, color):
        self.large_text = pygame.font.Font('arial.ttf',144)
        self.text_surf, self.text_rect = self.text_objects(text, self.large_text, color)
        self.text_rect.center = ((TeamBuzzIn.DISPLAY_WIDTH/2),(TeamBuzzIn.DISPLAY_HEIGHT/2))
        self.game_display.blit(self.text_surf, self.text_rect)

        pygame.display.update()

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                if event.type == pygame.KEYUP:
                    if event.key in self.team_key_dict["Team1"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 1",TeamBuzzIn.RED)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.team_key_dict["Team2"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 2",TeamBuzzIn.YELLOW)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.team_key_dict["Team3"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 3",TeamBuzzIn.GREEN)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.team_key_dict["Team4"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 4",TeamBuzzIn.BLUE)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.team_key_dict["Team5"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 5",TeamBuzzIn.BLACK)
                        pygame.display.update()
                        pygame.mixer.music.play()
                        self.wait()
                    elif event.key in self.team_key_dict["Team6"]:
                        self.game_display.fill(TeamBuzzIn.WHITE)
                        self.message_display("Team 6",TeamBuzzIn.GRAY)
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
    new_game = TeamBuzzIn()
    new_game.run()
