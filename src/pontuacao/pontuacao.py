import pygame

# Definir constantes para a pontuação
INTERVALO_PONTUACAO = 1000  # Intervalo para aumentar a pontuação em milissegundos
AUMENTO_PONTUACAO = 10

class Pontuacao:
    def __init__(self, fonte, cor_texto=(255, 255, 255)):
        """Inicializa a classe Pontuacao com a fonte e a cor do texto."""
        self.pontos = 0
        self.ultimo_tempo = pygame.time.get_ticks()
        self.fonte = fonte
        self.cor_texto = cor_texto

    def atualizar(self):
        """Atualiza a pontuação a cada segundo."""
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tempo >= INTERVALO_PONTUACAO:
            self.pontos += AUMENTO_PONTUACAO
            self.ultimo_tempo = tempo_atual

    def mostrar(self, screen):
        """Exibe a pontuação na tela."""
        texto_pontos = self.fonte.render(f"Pontos: {self.pontos}", True, self.cor_texto)
        screen.blit(texto_pontos, (10, 10))
