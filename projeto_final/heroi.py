from personagem import Personagem


class Heroi(Personagem):
    """
    Possui todos os atributos de Personagem + raca.
    Racas: humano, elfo, anao, etc.
    """
    def __init__(self, raca: str, nome: str, nivel: int):
        super().__init__(nome, nivel)
        self.raca = raca

    @property
    def raca(self):
        return self._raca

    @property
    def nome(self):
        return self._nome

    @property
    def nivel(self):
        return self._nivel

    @raca.setter
    def raca(self, raca_personagem):
        self._raca = raca_personagem

    @nome.setter
    def nome(self, nome_personagem):
        self._nome = nome_personagem

    @nivel.setter
    def nivel(self, nivel_personagem):
        self._nivel = nivel_personagem

    def atacar(self, sucesso) -> str:
        if sucesso in range(6, 11):
            return f'{self.nome} atacou.'
        else:
            return 'Ataque sem efeito.'

    def defender(self, sucesso) -> str:
        if sucesso in range(7, 11):
            return f'{self.nome} defendeu.'
        else:
            return 'Tentativa de defesa falha.'

    def fugir(self, sucesso) -> str:
        if sucesso in range(8, 11):
            return f'{self.nome} fugiu da luta.'
        else:
            return 'Impossível fugir.'

    def evoluir(self) -> None:
        if self.nivel < 100:
            self.nivel += 1
            return f'{self.nome} subiu para o nivel {self.nivel}.'
        else:
            return f'{self.nome} ja esta no nivel maximo.'

