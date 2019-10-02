import pygame

pygame.init()
screen = pygame.display.set_mode((610, 610))
done = False

while not done:
    w = 60
    h = 60
    for i in range (10):
        for j in range(10):
            pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(i*w+1+i, j*h+1+j, w, h))

    pygame.draw.circle(screen,(255,0,0),(30,30),20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
