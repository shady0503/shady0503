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
    while y<800 or x<600:
        pygame.draw.line(screen, (255,255,255), (0,y), (800,y), width=2)
        y+=50
        pygame.draw.line(screen, (255,255,255), (x,0), (x,600), width=2)
        x+=50
    new_surface = pygame.Surface((50, 50))
    new_surface.fill((255,255,255))
    for x in range(0,800,100):
            for y in range(0,600,100):
                screen.blit(new_surface, (x, y))
    for x in range(50,800,100):
            for y in range(50,600,100):
                screen.blit(new_surface, (x, y))



        




    pygame.display.flip()


