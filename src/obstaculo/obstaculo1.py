import pygame
import random

# Constantes para o obstáculo
OBSTACLE_WIDTH = 140
OBSTACLE_HEIGHT = 100
VELOCIDADE_OBSTACULO = 5

class Obstaculo:
    def __init__(self, tela, caminho_imagem, pos_x, pos_y=0):
        """Inicializa o obstáculo com uma imagem e uma posição inicial"""
        self.tela = tela
        self.image = pygame.image.load(caminho_imagem)
        self.image = pygame.transform.scale(self.image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.rect = pygame.Rect(pos_x - OBSTACLE_WIDTH / 2, pos_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    def mover(self):
        """Move o obstáculo para baixo"""
        self.rect.y += VELOCIDADE_OBSTACULO

    def reset(self):
        """Reseta a posição do obstáculo quando ele sai da tela"""
        self.rect.y = -OBSTACLE_HEIGHT
        self.rect.x = random.choice([420, 515, 615])  # Posições aleatórias

    def desenhar(self):
        """Desenha o obstáculo na tela"""
        self.tela.blit(self.image, (self.rect.x, self.rect.y))
