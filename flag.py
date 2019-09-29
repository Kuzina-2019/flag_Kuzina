import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)

def draw1():
    rect_color = pygame.Color("brown")
    rect_width = 0
    rect_point = [(20, 10), (30, 280)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

draw1()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()


