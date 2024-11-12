import pygame

class Cenario:
    def __init__(self, largura_tela, altura_tela, velocidade_pista, caminho_imagem):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.velocidade_pista = velocidade_pista
        self.pista_y = 0

        # Carregar e redimensionar a imagem do cenário
        self.cenario = pygame.image.load(caminho_imagem)
        self.cenario = pygame.transform.scale(self.cenario, (largura_tela, altura_tela))

    def atualizar(self):
        """Atualiza a posição da pista."""
        self.pista_y += self.velocidade_pista
        if self.pista_y >= self.altura_tela:
            self.pista_y = 0

    def desenhar(self, tela):
        """Desenha o cenário na tela."""
        tela.blit(self.cenario, (0, self.pista_y))
        tela.blit(self.cenario, (0, self.pista_y - self.altura_tela))
