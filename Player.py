from Partida import *
from Ficha import *

class Player:
    all_players = []


    def __init__(self, nome=None, bot=True):
        self._fichas = [] # Lista com as fichas
        self._nome = nome if nome else "Bot" # Os virtuais têm nomes predefinidos
        self._turno = False # Muda para True se for a vez do jogador
        self.all_players.append(self) # Adiciona cada jogador criado
        self._bot = bot


    def obterFichas(self):
        return self._fichas


    def definirFichas(self, fichas):
        self._fichas = fichas


    def obterNome(self):
        return self._nome


    def definirNome(self, nome):
        self._nome = nome


    def obterTurno(self):
        return self._fichas


    def definirTurno(self, turno):
        self._turno = turno


    def contarFichas(self):
        return len(self._fichas)


    def eBot(self):
        return self._bot


    def tapicu(self, partida):
        fichas_dobras = list(filter(lambda x: x.obterA() == x.obterB(), self._fichas))
        A, B = partida.obterPosiveis()
        fichasIz = list(filter(lambda x: x.obterA() == A, fichas_dobras))
        fichasDe = list(filter(lambda x: x.obterA() == B, fichas_dobras))
        if len(fichasIz) >=1 and len(fichasDe) >= 1:
            return [True, fichasIz, fichasDe]
        else:
            return [False, fichasIz, fichasDe]


    def inteligenciaBot(self, partida):
        tapicu = self.tapicu(partida) # [Bool, fichasIz, fichasDe]
        A, B = partida.obterPosiveis()


        if tapicu[0] == True: # Pode fazer tapicu
            fichaIz = tapicu[1][0]
            fichaDe = tapicu[2][0]
            # Adiciona as duas fichas ao tabuleiro
            fichaIz.definirDisponivel(fichaIz.obterA())
            fichaDe.definirDisponivel(fichaDe.obterA())
            partida.fichaEsquerda(fichaIz)
            partida.fichaDireita(fichaDe)
            # Remove as duas fichas das fichas do jogador
            self._fichas.remove(fichaIz)
            self._fichas.remove(fichaDe)
            print("-- Tapicu --")
        else:
            # Fichas possíveis de colocar à esquerda
            posiveisIz = list(filter(lambda x: x.obterA() == A or x.obterB() == A, self._fichas))
            # Fichas possíveis de colocar à direita
            posiveisDe = list(filter(lambda x: x.obterA() == B or x.obterB() == B, self._fichas))


            # Certifica-se de que haja pelo menos uma ficha
            if len(posiveisIz) != 0 or len(posiveisDe) != 0:
                if len(posiveisIz) >= len(posiveisDe):
                    # Adiciona a ficha à esquerda
                    ficha = posiveisIz[0]
                    ficha.definirDisponivel(ficha.obterB()) if ficha.obterA() == A else ficha.definirDisponivel(ficha.obterA())
                    partida.fichaEsquerda(ficha)
                    self._fichas.remove(ficha)
                else:
                    # Adiciona a ficha à direita
                    ficha = posiveisDe[0]
                    ficha.definirDisponivel(ficha.obterA()) if ficha.obterB() == B else ficha.definirDisponivel(ficha.obterB())
                    partida.fichaDireita(ficha)
                    self._fichas.remove(ficha)
            else:
                print("-- Passar a vez --")


    @classmethod
    def obterJogadores(cls):
        return cls.all_players

