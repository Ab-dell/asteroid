import pygame
from constants import *

def main():
    pygame.init() #initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a GUI to display the game
    clock = pygame.time.Clock()
    dt = 0

    while True:
        #Stop the game if the GUI is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()