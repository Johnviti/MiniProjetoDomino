class Ficha:
    all_fichas = []


    def __init__(self, cara_A, cara_B):
        self._disponivel = None
        self._cara_A = cara_A # Lado A
        self._cara_B = cara_B # Lado B
        self.all_fichas.append(self) # Adiciona cada instância à lista


    def obterA(self):
        return self._cara_A


    def obterB(self):
        return self._cara_B


    def definirDisponivel(self, disponivel):
        self._disponivel = disponivel


    def obterDisponivel(self):
        return self._disponivel


    @classmethod
    def obterFichas(cls):
        return cls.all_fichas