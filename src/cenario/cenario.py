import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Definindo dimensões da tela
LARGURA_TELA = 1000
ALTURA_TELA = 480
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Carrinho com Pista em Movimento")

# Definindo cores
BRANCO = (255, 255, 255)

# Velocidade do movimento da pista
VELOCIDADE_PISTA = 5

# Carregar imagem do cenário
cenario = pygame.image.load("img\cenario\cenario1.png")
cenario = pygame.transform.scale(cenario, (LARGURA_TELA, ALTURA_TELA))

# Função principal
def jogo():
    pista_y = 0  # Posição inicial da pista

    # Controlador de FPS
    clock = pygame.time.Clock()

    # Loop principal do jogo
    rodando = True
    while rodando:
        # Checar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Atualizar posição da pista
        pista_y += VELOCIDADE_PISTA
        if pista_y >= ALTURA_TELA:
            pista_y = 0  # Quando a pista sair da tela, volta para o topo

        # Desenhar fundo e elementos
        tela.blit(cenario, (0, 0))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar FPS (60 quadros por segundo)
        clock.tick(60)

    # Encerrar o Pygame
    pygame.quit()
    sys.exit()

# Rodar o jogo
if __name__ == "__main__":
    jogo()
