import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definir as configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sistema de Pontuação")

# Definir a fonte para exibir a pontuação
fonte = pygame.font.Font(None, 36)
cor_texto = (255, 255, 255)  # Cor do texto (branco)

# Função para gerenciar a pontuação
def atualizar_pontuacao(pontos, ultimo_tempo):
    tempo_atual = pygame.time.get_ticks()
    # Aumentar a pontuação a cada segundo (1000 ms)
    if tempo_atual - ultimo_tempo >= 1000:
        pontos += 10
        ultimo_tempo = tempo_atual  # Atualiza o último tempo
    return pontos, ultimo_tempo

# Função para exibir a pontuação na tela
def mostrar_pontuacao(screen, pontos):
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, cor_texto)
    screen.blit(texto_pontos, (10, 10))  # Posição do texto

# Variáveis de pontuação e tempo
pontos = 0
ultimo_tempo = pygame.time.get_ticks()  # Tempo inicial

# Loop principal do jogo
while True:
    # Verifica eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar a pontuação usando a função
    pontos, ultimo_tempo = atualizar_pontuacao(pontos, ultimo_tempo)

    # Limpar a tela
    screen.fill((0, 0, 0))  # Cor de fundo preta

    # Exibir a pontuação
    mostrar_pontuacao(screen, pontos)

    # Atualizar a tela
    pygame.display.flip()
