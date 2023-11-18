import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

def draw_circles():
    num_circles = 10 #kola layer
    rayon = 60
    for i in range(num_circles):
        theta = math.radians(360 / num_circles * i)
        for j in range(1, 6):  # 5 layers dyal circles, modifiable mais zwina haka hhhhhh
            décalage = rayon * j/2 #décalage dyal les centres par rapport (0,0)
            x = width // 2 + int(math.cos(theta) * décalage)  
            y = height // 2 + int(math.sin(theta) * décalage)
            
            pygame.draw.circle(screen, (255, 255, 255), (x, y), rayon, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    draw_circles()

    pygame.display.flip()

pygame.quit()
