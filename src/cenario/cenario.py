import pygame

class Cenario:
    def __init__(self, largura_tela, altura_tela, caminho_imagem):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.pista_y = 0

        # Carregar e redimensionar a imagem do cenário
        self.cenario = pygame.image.load(caminho_imagem)
        self.cenario = pygame.transform.scale(self.cenario, (largura_tela, altura_tela))

    def atualizar(self, velocidade_pista):
        """Atualiza a posição da pista de acordo com a velocidade dos obstáculos."""
        self.pista_y += velocidade_pista
        if self.pista_y >= self.altura_tela:
            self.pista_y = 0  # Reseta a posição da pista quando ela ultrapassa a tela

    def desenhar(self, tela):
        """Desenha o cenário na tela."""
        tela.blit(self.cenario, (0, self.pista_y))  # Pista superior
        tela.blit(self.cenario, (0, self.pista_y - self.altura_tela))  # Pista inferior (se repete)
