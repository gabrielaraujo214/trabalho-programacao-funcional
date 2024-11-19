import pygame
import sys
import random
from carro.carro import Carro
from cenario.cenario import Cenario
from obstaculo.obstaculo import Obstaculo
from pontuacao.pontuacao import Pontuacao

pygame.init()

info = pygame.display.Info()
LARGURA_TELA = info.current_w - 50
ALTURA_TELA = info.current_h - 100

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Super Speed Racer")

LARGURA_CARRO = int(LARGURA_TELA * 0.1)
ALTURA_CARRO = int(ALTURA_TELA * 0.14)
tamanho_carro = (LARGURA_CARRO, ALTURA_CARRO)

posicoes_fixas = [
    int(LARGURA_TELA * 0.375),
    int(LARGURA_TELA * 0.475),
    int(LARGURA_TELA * 0.575) 
]

caminho_imagem_carro = "img/carro/carro1.png"
carro = Carro(tela, caminho_imagem_carro, posicoes_fixas, tamanho_carro)

caminho_imagem_cenario = "img/cenario/cenario1.png"
cenario = Cenario(LARGURA_TELA, ALTURA_TELA, 5, caminho_imagem_cenario)

caminho_imagem_obstaculo = "img/carro/carro1.png"
obstaculos = []
for _ in range(2):
    pos_x_inicial = random.choice(posicoes_fixas)
    obstaculo = Obstaculo(tela, caminho_imagem_obstaculo, pos_x_inicial, -100)
    obstaculo.rect.x = pos_x_inicial
    obstaculos.append(obstaculo)

fonte = pygame.font.Font(None, 36)
pontuacao = Pontuacao(fonte)

clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        carro.processar_eventos(evento)

    cenario.atualizar()
    cenario.desenhar(tela)
    carro.atualizar_rastro()
    carro.desenhar()

    for obstaculo in obstaculos:
        obstaculo.mover()
        if obstaculo.rect.y > ALTURA_TELA:
            obstaculo.reset()
            obstaculo.rect.x = random.choice(posicoes_fixas)
        obstaculo.desenhar()

        # Detecção de colisão
        if carro.get_rect().colliderect(obstaculo.rect):
            print("Colisão detectada! Encerrando o jogo.")
            rodando = False  # Sai do loop principal

    pontuacao.atualizar()
    pontuacao.mostrar(tela)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
