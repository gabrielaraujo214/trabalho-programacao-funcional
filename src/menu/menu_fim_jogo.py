import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Define dimensões da tela
LARGURA_TELA = 600
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Menu de Fim de Jogo")

# Fonte para o texto
fonte = pygame.font.Font(None, 50)

# Função para desenhar o texto na tela
def desenhar_texto(texto, fonte, cor, superficie, x, y):
    textoobj = fonte.render(texto, True, cor)
    textorect = textoobj.get_rect()
    textorect.center = (x, y)
    superficie.blit(textoobj, textorect)

# Função para o menu de fim de jogo
def menu_fim_jogo(pontuacao_final, recorde):
    while True:
        tela.fill(BRANCO)

        # Exibe o título "Fim de Jogo"
        desenhar_texto("Fim de Jogo", fonte, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 4)

        # Exibe a pontuação e o recorde
        desenhar_texto(f"Sua Pontuação: {pontuacao_final}", fonte, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2 - 20)
        desenhar_texto(f"Recorde: {recorde}", fonte, PRETO, tela, LARGURA_TELA // 2, ALTURA_TELA // 2 + 40)

        # Botões
        botao_reiniciar = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 100, 200, 50)
        botao_menu_principal = pygame.Rect(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 170, 200, 50)

        # Desenha os botões na tela
        pygame.draw.rect(tela, VERDE, botao_reiniciar)
        pygame.draw.rect(tela, VERMELHO, botao_menu_principal)

        # Adiciona o texto aos botões
        desenhar_texto("Reiniciar", fonte, BRANCO, tela, botao_reiniciar.centerx, botao_reiniciar.centery)
        desenhar_texto("Menu Principal", fonte, BRANCO, tela, botao_menu_principal.centerx, botao_menu_principal.centery)

        # Captura eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_reiniciar.collidepoint(event.pos):
                    return "reiniciar"  # Reiniciar o jogo
                elif botao_menu_principal.collidepoint(event.pos):
                    return "menu_principal"  # Voltar ao menu principal

        # Atualiza a tela
        pygame.display.flip()

# Função principal para simular o uso do menu de fim de jogo
def main():
    pontuacao_final = 150  # Exemplo de pontuação final
    recorde = 300  # Exemplo de recorde

    acao = menu_fim_jogo(pontuacao_final, recorde)
    if acao == "reiniciar":
        print("O jogo será reiniciado.")
        # Código para reiniciar o jogo
    elif acao == "menu_principal":
        print("Voltando ao menu principal.")
        # Código para voltar ao menu principal

# Executa o jogo
main()
pygame.quit()
