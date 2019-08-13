import pygame
from pygame.locals import *

class PaintIo:
    def __init__(self):
        self.surface = pygame.display.set_mode((500, 500))
        
    
    def start(self):
        # Display current user info
        font = pygame.font.Font(None, 16)
        text = font.render("Would you like to start? (y/n)", 1, (255, 255, 255))
        textpos = text.get_rect(centerx = self.surface.get_width() / 2, centery = self.surface.get_height() / 2)
        self.surface.blit(text, textpos)
        pygame.display.update()
        
        # Prompt connect user
        
        # Select color prompt
        while True:
            event = pygame.event.wait()
            if event.type is pygame.QUIT:
                pygame.display.quit()
                return
            elif event.type is pygame.KEYUP:
                print(event.__dict__['key'])
                if event.__dict__['key'] == ord('y'):
                    self.surface.fill(pygame.Color("black"))
                    pygame.display.update()
                    break
                elif event.__dict__['key'] == ord('n'):
                    pygame.display.quit()
                    return
    
    def update(self):
        rect = pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(25, 25, 25, 25))
        pygame.display.update(rect)

def main():
    pygame.init()
    game = PaintIo()
    game.start()

if __name__ == "__main__":
    main()