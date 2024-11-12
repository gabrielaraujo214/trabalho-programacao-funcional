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
pista = pygame.transform.scale(pista, (1000, 480))
y = altura / 2

fixed_positions = [420, 515, 615]  # Três posições fixas na horizontal
posicao_atual = 1  # Posição inicial (meio)
rastro = []  # Lista para armazenar as posições anteriores do carro

pygame.display.set_caption('teste carro')

rastro_surface = pygame.Surface((largura, altura), pygame.SRCALPHA)

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
            elif event.key == K_LEFT and posicao_atual > 0:
                posicao_atual -= 1
            elif event.key == K_RIGHT and posicao_atual < 2:
                posicao_atual += 1

    # Adicione a posição atual do carro à lista de rastros
    carro_central_x = fixed_positions[posicao_atual] + carro.get_width() // 2
    carro_central_y = y + carro.get_height() // 2
    rastro.append((carro_central_x, carro_central_y))

    # Limite o número de posições armazenadas para o rastro
    if len(rastro) > 25:
        rastro.pop(0)

    # Reduza a opacidade do rastro
    rastro_surface.fill((0, 0, 0, 0))
    for i in range(len(rastro) - 1):
        opacidade = int(255 * (i / 50))  # Reduz a opacidade ao longo do tempo
        pygame.draw.line(rastro_surface, (255, 0, 0, opacidade), rastro[i], rastro[i + 1], 5)

    # Desenhe os objetos na tela
    tela.blit(pista, (0, 0))
    tela.blit(rastro_surface, (0, 0))  # Desenhe a superfície do rastro
    tela.blit(carro, (fixed_positions[posicao_atual], y))

    pygame.display.flip()
    relogio.tick(60)
