import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Configurações de tela
LARGURA_TELA, ALTURA_TELA = 800, 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Road Fighter")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Fontes
fonte_titulo = pygame.font.Font(None, 74)
fonte_menu = pygame.font.Font(None, 50)

# Função para exibir o texto centralizado
def desenhar_texto(texto, fonte, cor, superficie, x, y):
    objeto_texto = fonte.render(texto, True, cor)
    retangulo_texto = objeto_texto.get_rect(center=(x, y))
    superficie.blit(objeto_texto, retangulo_texto)

# Função para o menu principal
def menu_principal():
    while True:
        tela.fill(AZUL)
        desenhar_texto("Road Fighter", fonte_titulo, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 4)
        
        # Desenhando botões
        botao_iniciar = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 50, 200, 50)
        botao_ranking = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 20, 200, 50)
        botao_creditos = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 90, 200, 50)
        
        pygame.draw.rect(tela, VERDE, botao_iniciar)
        pygame.draw.rect(tela, VERMELHO, botao_ranking)
        pygame.draw.rect(tela, BRANCO, botao_creditos)
        
        desenhar_texto("Iniciar", fonte_menu, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2 - 25)
        desenhar_texto("Ranking", fonte_menu, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2 + 45)
        desenhar_texto("Créditos", fonte_menu, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2 + 115)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_iniciar.collidepoint(evento.pos):
                    iniciar_jogo()
                elif botao_ranking.collidepoint(evento.pos):
                    exibir_ranking()
                elif botao_creditos.collidepoint(evento.pos):
                    exibir_creditos()
        
        pygame.display.flip()

# Função para iniciar o jogo
def iniciar_jogo():
    jogando = True
    while jogando:
        tela.fill(AZUL)
        desenhar_texto("Iniciando o Jogo...", fonte_titulo, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                jogando = False

        pygame.display.flip()

# Função para exibir o ranking
def exibir_ranking():
    ranking = ["1. Jogador1 - 1000 pontos", "2. Jogador2 - 800 pontos", "3. Jogador3 - 600 pontos"]
    exibindo = True
    while exibindo:
        tela.fill(AZUL)
        desenhar_texto("Ranking", fonte_titulo, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 4)
        
        # Exibir a lista de ranking
        for i, pontuacao in enumerate(ranking):
            desenhar_texto(pontuacao, fonte_menu, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 3 + i * 50)
        
        # Desenhando o botão "Voltar"
        botao_voltar = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA - 80, 200, 50)
        pygame.draw.rect(tela, VERMELHO, botao_voltar)
        desenhar_texto("Voltar", fonte_menu, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA - 55)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    exibindo = False
        
        pygame.display.flip()

# Função para exibir os créditos
def exibir_creditos():
    exibindo = True
    while exibindo:
        tela.fill(AZUL)
        desenhar_texto("Créditos", fonte_titulo, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 4)
        desenhar_texto("Desenvolvido por:...", fonte_menu, BRANCO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2)
        
        # Desenhando o botão "Voltar"
        botao_voltar = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA - 80, 200, 50)
        pygame.draw.rect(tela, VERMELHO, botao_voltar)
        desenhar_texto("Voltar", fonte_menu, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA - 55)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    exibindo = False
        
        pygame.display.flip()

# Iniciar o menu principal
menu_principal()
