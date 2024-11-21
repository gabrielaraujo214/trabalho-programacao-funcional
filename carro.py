import pygame

class Carro:
    def __init__(self, tela, caminho_imagem, posicoes_fixas, tamanho_carro):
        self.tela = tela
        self.imagem = self._carregar_imagem(caminho_imagem, tamanho_carro)
        self.posicoes_fixas = posicoes_fixas
        self.posicao_atual = 1  # Posição inicial no meio
        self.y = self.tela.get_height() / 2
        self.rastro = []
        self.rastro_surface = pygame.Surface((tela.get_width(), tela.get_height()), pygame.SRCALPHA)

    def _carregar_imagem(self, caminho, tamanho):
        imagem = pygame.image.load(caminho)
        return pygame.transform.scale(imagem, tamanho)

    def processar_eventos(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in {pygame.K_a, pygame.K_LEFT} and self.posicao_atual > 0:
                self.posicao_atual -= 1
            elif evento.key in {pygame.K_d, pygame.K_RIGHT} and self.posicao_atual < len(self.posicoes_fixas) - 1:
                self.posicao_atual += 1

    def atualizar_rastro(self):
        carro_central_x = self.posicoes_fixas[self.posicao_atual] + self.imagem.get_width() // 2
        carro_central_y = self.y + self.imagem.get_height() // 2
        self.rastro.append((carro_central_x, carro_central_y))
        if len(self.rastro) > 25:
            self.rastro.pop(0)

    def desenhar_rastro(self):
        self.rastro_surface.fill((0, 0, 0, 0))  # Limpa a superfície com transparência
        for i in range(len(self.rastro) - 1):
            opacidade = int(255 * (i / 25))
            pygame.draw.line(self.rastro_surface, (255, 0, 0, opacidade), self.rastro[i], self.rastro[i + 1], 5)

    def desenhar(self):
        self.desenhar_rastro()
        self.tela.blit(self.rastro_surface, (0, 0))
        self.tela.blit(self.imagem, (self.posicoes_fixas[self.posicao_atual], self.y))

    def get_rect(self):
        """Retorna o retângulo (Rect) de colisão do carro."""
        return self.imagem.get_rect(topleft=(self.posicoes_fixas[self.posicao_atual], self.y))
