import pygame
from pygame.locals import *
from sys import exit


pygame.init()

relogio = pygame.time.Clock()
largura = 1000
altura = 480
tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)
carro = pygame.image.load('carro5-2.png')
carroE = pygame.image.load('carroE5-2.png')
carroD = pygame.image.load('carroD5-2.png')
carro_l = 250
carro_a = 150
carro = pygame.transform.scale(carro, (carro_l, carro_a))
carroE = pygame.transform.scale(carroE, (carro_l, carro_a))
carroD = pygame.transform.scale(carroD, (carro_l, carro_a))

pista = pygame.image.load('pista5.png')
x = 270
y = altura / 2

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
                
                '''def movimento_carro():'''
            elif event.key == K_a:
                x -= 50
                carro_atual = carroE
            elif event.key == K_d:
                x += 50
                carro_atual = carroD

    # Se nenhuma tecla for pressionada, mantenha a imagem do carro padrão
    if not (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d]):
        carro_atual = carro
    '''return x'''

    '''def imagem_carro():'''
    tela.blit(pista, (0, 0))
    tela.blit(carro_atual, (x, y))
    
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
