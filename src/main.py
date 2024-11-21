import pygame
import sys
import random
import os

from carro.carro import Carro
from cenario.cenario import Cenario
from obstaculo.obstaculo import Obstaculo
from pontuacao.pontuacao import Pontuacao
from medidor_velocidade.medidor_velocidade import MedidorVelocidade 

# Função para lidar com caminhos de recursos
def get_resource_path(relative_path):
    """Resolve caminhos de recursos para compatibilidade com executáveis."""
    if hasattr(sys, '_MEIPASS'):
        # Quando empacotado no PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    # Durante o desenvolvimento
    return os.path.join(os.path.abspath("."), relative_path)

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

# Caminhos de imagens ajustados com `get_resource_path`
caminho_imagem_carro = get_resource_path("src/img/carro1.png")
carro = Carro(tela, caminho_imagem_carro, posicoes_fixas, tamanho_carro)

caminho_imagem_cenario = get_resource_path("src/img/cenario1.png")
cenario = Cenario(LARGURA_TELA, ALTURA_TELA, caminho_imagem_cenario)

caminho_imagem_obstaculo = get_resource_path("src/img/carro3.png")
obstaculos = []
for _ in range(2):
    pos_x_inicial = random.choice(posicoes_fixas)
    obstaculo = Obstaculo(tela, caminho_imagem_obstaculo, pos_x_inicial, -100)
    obstaculo.rect.x = pos_x_inicial
    obstaculos.append(obstaculo)

fonte = pygame.font.Font(None, 36)
pontuacao = Pontuacao(fonte)

# Instanciando o medidor de velocidade
medidor_velocidade = MedidorVelocidade(fonte)

clock = pygame.time.Clock()
rodando = True

# Variável que controla a velocidade dos obstáculos
velocidade_obstaculos = 5  # Velocidade inicial dos obstáculos
tempo_decorrido = 0  # Tempo decorrido em segundos

while rodando:
    delta_time = clock.get_time() / 1000  # Tempo em segundos desde o último frame
    tempo_decorrido += delta_time

    # Aumenta a velocidade dos obstáculos a cada 5 segundos
    if tempo_decorrido >= 5:
        velocidade_obstaculos += 0.5  # Aumenta a velocidade mais rápido
        if velocidade_obstaculos > 15:  # Limita a velocidade máxima
            velocidade_obstaculos = 15
        tempo_decorrido = 0  # Reset o tempo decorrido

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        carro.processar_eventos(evento)

    cenario.atualizar(velocidade_obstaculos)
    cenario.desenhar(tela)
    carro.atualizar_rastro()
    carro.desenhar()

    for obstaculo in obstaculos:
        obstaculo.mover(velocidade_obstaculos)  # Passa a velocidade como argumento
        if obstaculo.rect.y > ALTURA_TELA:
            obstaculo.reset(posicoes_fixas)  # Reset da posição do obstáculo
        obstaculo.desenhar()

        # Detecção de colisão
        if carro.get_rect().colliderect(obstaculo.rect):
            print("Colisão detectada! Encerrando o jogo.")
            print(f"Pontuação final: {pontuacao.pontos}")  # Exibe a pontuação final
            rodando = False  # Sai do loop principal

    pontuacao.atualizar()
    pontuacao.mostrar(tela)

    # Atualizando e desenhando o medidor de velocidade
    medidor_velocidade.desenhar(tela, velocidade_obstaculos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
