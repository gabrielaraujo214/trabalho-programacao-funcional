import pygame
from pygame.locals import *
from sys import exit

pygame.init()

relogio = pygame.time.Clock()
largura = 640
altura = 460
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
carro = pygame.image.load('trabalho-programacao-funcional/carro5-2.png')
carro_l = 250
carro_a = 150
carro = pygame.transform.scale(carro, (carro_l, carro_a))
pista = pygame.image.load('trabalho-programacao-funcional/pista5.png')
x = 270
y = altura / 2

pygame.display.set_caption('teste carro')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN or event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        x -= 5
    if keys[K_d]:
        x += 5

    tela.blit(pista, (0, 0))
    tela.blit(carro, (x, y))
    
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()