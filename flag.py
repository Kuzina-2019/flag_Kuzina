import pygame

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)

def draw1():
    rect_color = pygame.Color("brown")
    rect_width = 0
    rect_point = [(20, 10), (30, 280)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

def draw3():
    rect_color = pygame.Color("blue")
    rect_width = 0
    rect_point = [(50, 60), (200, 50)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


def draw2():
    rect_color = pygame.Color("white")
    rect_width = 0
    rect_point = [(50, 10), (200, 50)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)

def draw4():
    rect_color = pygame.Color("red")
    rect_width = 0
    rect_point = [(50, 110), (200, 50)]
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


draw1()
draw2()
draw3()
draw4()
draw3()


while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()


