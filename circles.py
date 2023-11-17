import pygame
import numpy as np
# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")
Running = True
# Main game loop
while Running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            
    screen.fill((0, 0, 0))
    theta=0
    while theta<=2*np.pi:
        x=200*np.cos(theta)+400
        y=200*np.sin(theta)+300
        pygame.draw.circle(screen, ((255, 255, 255)), (x,y), 100, width=1)
        theta+=np.pi/30




        




    pygame.display.flip()


