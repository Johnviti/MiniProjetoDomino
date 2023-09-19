from random import sample
from Ficha import *
from Player import *
from Partida import *
from collections import deque

#---------------------------------------
# Função para verificar se alguém possui um seis duplo
#---------------------------------------
def preencherFichas():
    """Preenche uma a uma as 28 fichas"""
    fichas = []
    for i in range(7):
        for j in range(i, 7):
            fichas.append(Ficha(i, j))
    return fichas


def verificarSeis(jogadores, partida):
    for i in range(len(jogadores)):
        j = 0
        fichas = jogadores[i].obterFichas()
        for ficha in fichas:
            if ficha.obterA() + ficha.obterB() == 12:
                ficha.definirDisponivel(6)
                partida.fichaDireita(fichas.pop(j))
                return i
            j += 1

#---------------------------------------
# Função para verificar se alguém pode fazer tapicu
#---------------------------------------

def tapicu(fichas, partida, indice_1, indice_2):
    for ficha in fichas:
        fichas_dobras = list(filter(lambda x: x.obterA() == x.obterB(), fichas))
        A, B = partida.obterPosiveis()
        fichas_possiveis = list(filter(lambda x: x.obterA() == A or x.obterA() == B, fichas_dobras))
    if len(fichas_possiveis) >= 2:
        for i in range(0, len(fichas_possiveis)):
            if fichas[indice_1] == fichas_possiveis[i]:
                for j in range(0, len(fichas_possiveis)):
                    if fichas[indice_2] == fichas_possiveis[j]:
                        A, B = partida.obterPosiveis()
                        fichas_dobras = list(filter(lambda x: x.obterA() == x.obterB(), fichas))
                        fichasIz = list(filter(lambda x: x.obterA() == A, fichas_dobras))
                        fichasDe = list(filter(lambda x: x.obterA() == B, fichas_dobras))
                        if len(fichasIz) == 1 and len(fichasDe) == 1:
                            fichaIz = fichasIz[0]
                            fichasDer = fichasDe[0]
                            partida.fichaEsquerda(fichaIz)
                            fichas.remove(fichaIz)
                            partida.fichaDireita(fichasDer)
                            fichas.remove(fichasDer)
                            print("-- Tapicu --")
    else:
        print("-"*100)
        print("Jogada inválida, perde sua vez")
        print("-"*100)

#---------------------------------------
# Função para validar uma jogada
#---------------------------------------

def validarJogada(fichas, indice, lado, partida):
    ficha = fichas[indice]
    A, B = partida.obterPosiveis()
    caraA, caraB = ficha.obterA(), ficha.obterB()
    if (caraA == A or caraB == A) and lado.lower() == "i":
        ficha.definirDisponivel(caraA if caraB == A else caraB)
        partida.fichaEsquerda(fichas.pop(indice))
    elif (caraA == B or caraB == B) and lado.lower() == "d":
        ficha.definirDisponivel(caraA if caraB == B else caraB)
        partida.fichaDireita(fichas.pop(indice))
    else:
        print("Jogada inválida. Você não pode jogar essa ficha")
        print("Você perde sua vez!")
        print("-"*100)
        input("-- Pressione Enter --")
        print("-"*100)

#---------------------------------------
# Função para a jogada do jogador
#---------------------------------------

def jogada(jogador, turno, partida):
    if jogador.eBot():
        print(f"\n-- Vez de {jogador.obterNome()} --")
        jogador.inteligenciaBot(partida)
        tabuleiro = partida.obterTabuleiro()
        partida.mostrarTabuleiro(tabuleiro)
        print(f'-- Fichas restantes: {jogador.contarFichas()} --\n')
        print("-"*100)
        input("-- Pressione Enter --")
        print("-"*100)
    else:
        tabuleiro = partida.obterTabuleiro()
        print("-"*100)
        print(f"\n-- Sua vez, {jogador.obterNome()} --")
        partida.mostrarTabuleiro(tabuleiro)
        fichas = jogador.obterFichas()
        contagem = 1
        print("-- Suas fichas --\n")
        print(f"0. Passar")
        for ficha in fichas:
            print(f"{contagem}. [{ficha.obterA()}|{ficha.obterB()}]")
            contagem += 1
        print(f"{contagem}. Tapicu")
        print("\n", "-"*100, sep="")
        indice = int(input("\n-> Selecione uma ficha para jogar: ")) - 1
        print("\n", "-"*100, sep="")
        if indice < len(fichas) and indice >= 0:
            print("-- Digite 'D' para colocar a ficha no lado direito do tabuleiro --")
            print("-- Digite 'I' para colocar a ficha no lado esquerdo do tabuleiro --")
            print("-"*100, "\n", sep="")
            lado = input("-> Selecione o lado: ")
            print("\n", "-"*100, sep="")
            validarJogada(fichas, indice, lado, partida)
        elif indice == len(fichas):
            print("\n", "-"*100, sep="")
            indice_1 = int(input("\n-> Selecione a primeira ficha: ")) - 1
            print("\n", "-"*100, sep="")
            if indice_1 < len(fichas) and indice_1 >= 0:
                print("-- Digite 'D' para colocar a ficha no lado direito do tabuleiro --")
                print("-- Digite 'I' para colocar a ficha no lado esquerdo do tabuleiro --")
                print("-"*100, "\n", sep="")
                lado = input("-> Selecione o lado: ")
                print("\n", "-"*100, sep="")
            print("\n", "-"*100, sep="")
            indice_2 = int(input("\n-> Selecione a segunda ficha: ")) - 1
            print("\n", "-"*100, sep="")
            if indice_2 < len(fichas) and indice_2 >= 0:
                print("-- Digite 'D' para colocar a ficha no lado direito do tabuleiro --")
                print("-- Digite 'I' para colocar a ficha no lado esquerdo do tabuleiro --")
                print("-"*100, "\n", sep="")
                lado = input("-> Selecione o lado: ")
                print("\n", "-"*100, sep="")

                tapicu(fichas, partida, indice_1, indice_2)
        else:
            if indice == -1:
                print("Você passou a vez!")
                print("-"*100)
                input("-- Pressione Enter --")
                print("-"*100)
            else:
                print("Jogada inválida. Você perde sua vez!")
                print("-"*100)
                input("-- Pressione Enter --")
                print("-"*100)

#---------------------------------------
# Função principal do jogo
#---------------------------------------

if __name__ == "__main__":
    preencherFichas()
    Player("Bot 1", True)
    Player("Bot 2", True)
    Player("Bot 3", True)
    Player(input("Digite seu nome: "), False)
    jogadores = Player.obterJogadores()
    fichas = Ficha.obterFichas()
    partida = Partida(jogadores, fichas)
    partida.distribuirFichas()
    turno = verificarSeis(jogadores, partida)
    tabuleiro = partida.obterTabuleiro()
    while True:
        turno = turno + 1 if turno != 3 else 0
        jogada(jogadores[turno], turno, partida)
        partida.verificarVencedor(jogadores[turno])
        vencedor = partida.obterVencedor()
        if vencedor:
            vencedor = vencedor.obterNome() if vencedor.obterNome() else f"virtual {turno + 1}"
            print(f"\n-- O jogador vencedor é: {vencedor} --")
            break
    print("\n-- JOGO ENCERRADO --")
