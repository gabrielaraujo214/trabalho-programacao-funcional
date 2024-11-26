import pygame

class MedidorVelocidade:
    def __init__(self, fonte, cor_texto=(255, 255, 255), cor_fundo=(0, 0, 0)):
        """
        Inicializa o medidor de velocidade.
        :param fonte: Fonte usada para o texto.
        :param cor_texto: Cor do texto exibido.
        :param cor_fundo: Cor do fundo do medidor.
        """
        self.fonte = fonte
        self.cor_texto = cor_texto
        self.cor_fundo = cor_fundo

        # Posições relativas ao tamanho da tela
        self.pos_x = 20  # Distância da borda esquerda da tela

    def desenhar(self, tela, velocidade):
        """
        Desenha o medidor de velocidade na tela.
        :param tela: A tela onde o medidor será exibido.
        :param velocidade: Velocidade atual dos obstáculos, a ser exibida.
        """
        # Calcula a posição X e Y diretamente dentro do método desenhar
        pos_x = 0.05 * tela.get_width()  # 5% da largura da tela
        pos_y = tela.get_height() - 40  # 40 pixels de distância da parte inferior

        # Texto que exibe a velocidade
        texto_velocidade = f"Velocidade: {int(velocidade)} km/h"
        texto = self.fonte.render(texto_velocidade, True, self.cor_texto)
        
        # Desenha o fundo do medidor
        largura_texto, altura_texto = texto.get_size()
        pygame.draw.rect(tela, self.cor_fundo, (pos_x - 10, pos_y - 5, largura_texto + 20, altura_texto + 10))
        
        # Desenha o texto
        tela.blit(texto, (pos_x, pos_y))