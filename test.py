import pygame
from pygame.locals import *

class PaintIo:
    def __init__(self):
        self.surface = pygame.display.set_mode((500, 500))
        
    
    def start(self):
        # Display current user info
        
        # Prompt connect user
        
        # Select color prompt
        while True:
            event = pygame.event.wait()
            if event.type is pygame.QUIT:
                pygame.display.quit()
                return
            elif event.type is pygame.KEYUP:
                print(event.__dict__['key'])
    
    def update(self):
        rect = pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(25, 25, 25, 25))
        pygame.display.update(rect)

def main():
    pygame.init()
    game = PaintIo()
    game.start()

if __name__ == "__main__":
    main()