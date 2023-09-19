from collections import deque
from random import sample
class Partida:

    def __init__(self, jogadores, fichas):
        self._jogadores = jogadores # Lista de jogadores
        self._fichas = fichas # Lista de fichas
        self._tabuleiro = deque([])
        self._vencedor = None


    def distribuirFichas(self):
        for jogador in self._jogadores:
            fichas_selecionadas = sample(self._fichas, 7)
            self._fichas = list(filter(lambda x: x not in fichas_selecionadas, self._fichas))
            jogador.definirFichas(fichas_selecionadas)


    def verificarVencedor(self, jogador):
        if jogador.contarFichas() == 0:
            self._vencedor = jogador


    def fichaDireita(self, ficha):
        self._tabuleiro.append(ficha)


    def fichaEsquerda(self, ficha):
        self._tabuleiro.appendleft(ficha)


    def obterPosiveis(self):
        return self._tabuleiro[0].obterDisponivel(), self._tabuleiro[-1].obterDisponivel()


    def obterFichas(self):
        return self._fichas


    def obterTabuleiro(self):
        return self._tabuleiro


    def adicionarFicha(self, ficha):
        self._tabuleiro.append(ficha)


    def obterVencedor(self):
        return self._vencedor


    def mostrarTabuleiro(self, fichas):
        arr_saida = []
        for ind in range(len(fichas)):
            if ind == (len(fichas) - 1): # Última ficha
                fichaA, fichaB = fichas[ind - 1], fichas[ind]
                if fichaB.obterA() == fichaA.obterA() or fichaB.obterA() == fichaA.obterB():
                    arr_saida.append("[" + str(fichaB.obterA()) + "|" + str(fichaB.obterB()) + "]")
                else:
                    arr_saida.append("[" + str(fichaB.obterB()) + "|" + str(fichaB.obterA()) + "]")
            else:
                fichaA, fichaB = fichas[ind], fichas[ind + 1]
                if fichaA.obterA() == fichaB.obterA() or fichaA.obterA() == fichaB.obterB():
                    arr_saida.append("[" + str(fichaA.obterB()) + "|" + str(fichaA.obterA()) + "]")
                else:
                    arr_saida.append("[" + str(fichaA.obterA()) + "|" + str(fichaA.obterB()) + "]")
        print("\n", "-"*(((len(arr_saida)*5)-3)//2), "TABULEIRO", "-"*(((len(arr_saida)*5)-3)//2), sep="")
        print("|", " "*((len(arr_saida)*5)+2), "|", sep="")
        print("|", "".join(arr_saida), "|")
        print("|", " "*((len(arr_saida)*5)+2), "|", sep="")
        print("-"*((len(arr_saida)*5)+4),"\n")
