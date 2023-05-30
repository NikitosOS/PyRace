import pygame

class init:
    def window():
        
        screen = pygame.display.set_mode([1024, 720])
        pygame.display.set_caption("PyCar")
        icon = pygame.image.load("img/icon.png")
        pygame.display.set_icon(icon)