import pygame
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
    x,y=(0,0)
    while x<800 and y<600:
        pygame.draw.line(screen,(255,255,255),(x,y),(y,600))
        x+=0.1
        y+=15
    


        




    pygame.display.flip()


