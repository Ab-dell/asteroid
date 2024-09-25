import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init() #initialize pygame
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,updatable,drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a GUI to display the game
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0

    while True:
        #Stop the game if the GUI is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        for item in updatable:
            item.update(dt)
            
        for item in asteroids:
            if player.check_for_collision(item):
                print("Game over!")
                return
        
            for obj in shots:
                if item.check_for_collision(obj):
                    item.split()
                    obj.kill()

        dt = clock.tick(60) / 1000
        pygame.display.flip()
        
        
        

if __name__ == "__main__":
    main()