import pygame
import sys
import random
from carro.carro1 import Carro
from cenario.cenario1 import Cenario
from obstaculo.obstaculo1 import Obstaculo  # Importando a classe Obstaculo
from pontuacao.pontuacao1 import Pontuacao  # Importando a classe Pontuacao

# Inicializa o Pygame
pygame.init()

# Definindo dimensões da tela
LARGURA_TELA = 1000
ALTURA_TELA = 480
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Road Fighter")

# Instanciar o carro
caminho_imagem_carro = "img/carro/carro1.png"
posicoes_fixas = [420, 515, 615]  # Posições fixas para o carro
tamanho_carro = (80, 50)
carro = Carro(tela, caminho_imagem_carro, posicoes_fixas, tamanho_carro)

# Instanciar o cenário
caminho_imagem_cenario = "img/cenario/cenario1.png"
cenario = Cenario(LARGURA_TELA, ALTURA_TELA, 5, caminho_imagem_cenario)

# Instanciar os obstáculos
caminho_imagem_obstaculo = "img/carro/carro1.png"
obstaculos = []  # Lista para armazenar os obstáculos
for _ in range(2):  # Criando 2 obstáculos iniciais
    obstaculo = Obstaculo(tela, caminho_imagem_obstaculo, random.choice([420, 515, 615]), -100)
    obstaculos.append(obstaculo)

# Instanciar a pontuação
fonte = pygame.font.Font(None, 36)  # Fonte para a pontuação
pontuacao = Pontuacao(fonte)  # Criando a instância da pontuação

# Controlador de FPS
clock = pygame.time.Clock()

# Função para verificar colisões
def verificar_colisao(carro, obstaculos):
    for obstaculo in obstaculos:
        if carro.rect.colliderect(obstaculo.rect):
            return True  # Colisão detectada
    return False

# Loop principal do jogo
rodando = True
while rodando:
    # Checar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Processa eventos do teclado (movimentação do carro)
        carro.processar_eventos(evento)

    # Atualizar o cenário e o carro
    cenario.atualizar()
    cenario.desenhar(tela)
    carro.atualizar_rastro()
    carro.desenhar()

    # Mover os obstáculos
    for obstaculo in obstaculos:
        obstaculo.mover()
        if obstaculo.rect.y > ALTURA_TELA:
            obstaculo.reset()  # Reseta o obstáculo quando ele sai da tela
        obstaculo.desenhar()  # Desenha o obstáculo na tela

    # Atualizar a pontuação
    pontuacao.atualizar()

    # Exibir a pontuação na tela
    pontuacao.mostrar(tela)

    # # Verificar se houve colisão entre o carro e os obstáculos
    # if verificar_colisao(carro, obstaculos):
    #     print("Colisão detectada!")
    #     rodando = False  # Finaliza o jogo em caso de colisão

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS (60 quadros por segundo)
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
