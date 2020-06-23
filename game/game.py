import pygame
import sys

from .config import *
from .platform import Platform

class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITLE)

        self.running=True
        
    def start(self):
        self.new()
    
    def new(self):
        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform=Platform()

        self.sprites=pygame.sprite.Group()
        self.sprites.add(self.platform)
        
    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()
            
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.running=False
                pygame.quit()
                sys.exit()
                
    def draw(self):
        self.surface.fill(BLACK)

        self.sprites.draw(self.surface)
        
    def update(self):
        # pygame.display.update()
        pygame.display.flip()
        
    def stop(self):
        pass