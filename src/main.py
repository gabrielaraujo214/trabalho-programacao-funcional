import pygame
import sys
import random
from carro.carro import Carro
from cenario.cenario import Cenario
from obstaculo.obstaculo import Obstaculo
from pontuacao.pontuacao import Pontuacao

# Inicializa o Pygame
pygame.init()

# Obter a resolução da tela atual
info = pygame.display.Info()
LARGURA_TELA = info.current_w - 50  # Subtraímos alguns pixels para evitar a tela cheia
ALTURA_TELA = info.current_h - 100  # Subtraímos para deixar espaço para as barras do sistema

# Definindo a tela como janela maximizada com a barra de título (não redimensionável)
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Road Fighter")

# Definindo o tamanho do carro de forma proporcional
LARGURA_CARRO = int(LARGURA_TELA * 0.1)  # 10% da largura da tela
ALTURA_CARRO = int(ALTURA_TELA * 0.14)   # 14% da altura da tela
tamanho_carro = (LARGURA_CARRO, ALTURA_CARRO)

# Instanciar o carro
caminho_imagem_carro = "img/carro/carro1.png"
posicoes_fixas = [420, 515, 615]  # Posições fixas para o carro
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

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS (60 quadros por segundo)
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
