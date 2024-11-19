import pygame
import random

class Obstaculo:
    def __init__(self, tela, caminho_imagem, pos_x, pos_y=0):
        """Inicializa o obstáculo com uma imagem e uma posição inicial"""

        # Obter o tamanho da tela para ajustar o tamanho dos obstáculos
        self.tela = tela
        largura_tela = self.tela.get_width()
        altura_tela = self.tela.get_height()

        # Definir largura e altura do obstáculo de forma proporcional à tela
        self.OBSTACLE_WIDTH = int(largura_tela * 0.1)  # 10% da largura da tela
        self.OBSTACLE_HEIGHT = int(altura_tela * 0.14)  # 14% da altura da tela

        # Carregar e dimensionar a imagem do obstáculo
        self.image = pygame.image.load(caminho_imagem)
        self.image = pygame.transform.scale(self.image, (self.OBSTACLE_WIDTH, self.OBSTACLE_HEIGHT))

        # Definir a posição e o retângulo do obstáculo
        self.rect = pygame.Rect(pos_x - self.OBSTACLE_WIDTH / 2, pos_y, self.OBSTACLE_WIDTH, self.OBSTACLE_HEIGHT)

    def mover(self):
        """Move o obstáculo para baixo"""
        self.rect.y += 5  # Velocidade fixa de movimento para baixo

    def reset(self):
        """Reseta a posição do obstáculo quando ele sai da tela"""
        self.rect.y = -self.OBSTACLE_HEIGHT
        self.rect.x = random.choice([420, 515, 615])  # Posições aleatórias

    def desenhar(self):
        """Desenha o obstáculo na tela"""
        self.tela.blit(self.image, (self.rect.x, self.rect.y))
