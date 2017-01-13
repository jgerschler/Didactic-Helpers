import pygame, sys

TeamFile = 'ping.ogg'

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(TeamFile)

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768

#color assignments
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (184,184,184)
RED = (255,0,0)
GREEN = (50,150,50)
YELLOW = (255,200,0)
BLUE = (0,100,255)

#team key assignments
Team1Keys = [pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d]
Team2Keys = [pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h]
Team3Keys = [pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l]
Team4Keys = [pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p]
Team5Keys = [pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t]
Team6Keys = [pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x]

clock = pygame.time.Clock()

finished = False

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
gameDisplay.fill(WHITE)
pygame.display.update()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                return

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color):
    largeText = pygame.font.Font('arial.ttf',72)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

def run(self):
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.KEYUP:
                if event.key in Team1Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 1",RED)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()
                elif event.key in Team2Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 2",YELLOW)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()
                elif event.key in Team3Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 3",GREEN)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()
                elif event.key in Team4Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 4",BLUE)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()
                elif event.key in Team5Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 5",BLACK)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()
                elif event.key in Team6Keys:
                    gameDisplay.fill(WHITE)
                    message_display("Team 6",GRAY)
                    pygame.display.update()
                    pygame.mixer.music.play()
                    wait()

        clock.tick(60)
                    
    pygame.quit()
    quit()
