import pygame
from pygame.locals import *
from sys import exit

pygame.init()

relogio = pygame.time.Clock()
largura = 1000
altura = 480
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
carro = pygame.image.load('carro6.png')
carro_l = 250
carro_a = 150
carro = pygame.transform.scale(carro, (80, 50))
pista = pygame.image.load('pista5.png')
y = altura / 2

fixed_positions = [420, 515, 615]  # Três posições fixas na horizontal
posicao_atual = 1  # Posição inicial (meio)

pygame.display.set_caption('teste carro')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_a and posicao_atual > 0:
                posicao_atual -= 1
            elif event.key == K_d and posicao_atual < 2:
                posicao_atual += 1

    # Desenhe os objetos na tela
    tela.blit(pista, (largura, altura))
    tela.blit(carro, (fixed_positions[posicao_atual], y))

    pygame.display.flip()
    relogio.tick(60)
