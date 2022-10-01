"""
Personagem: Heroi, Monstro
Heroi: Mago, Guerreiro
Monstro: Orc, Dragao
"""

from abc import ABC, abstractmethod


class Personagem(ABC):
    """
    Classe abstrata.
    Possui nome e nivel.
    Pode atacar ou defender.
    """
    def __init__(self, nome: str, nivel: int):
        self.nome = nome
        self.nivel = nivel

    @abstractmethod
    def atacar(self): pass

    @abstractmethod
    def defender(self): pass


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

    def atacar(self, sucesso):
        if sucesso in range(6, 11):
            return f'{self.nome} atacou.'
        else:
            return 'Ataque sem efeito.'

    def defender(self, sucesso):
        if sucesso in range(7, 11):
            return f'{self.nome} defendeu.'
        else:
            return 'Tentativa de defesa falha.'

    def fugir(self, sucesso):
        if sucesso in range(8, 11):
            return f'{self.nome} fugiu da luta.'
        else:
            return 'Impossível fugir.'


class Guerreiro(Heroi):
    """
    Possui todos os atributos de Personagem e Heroi + arma e HP
    Pode evoluir nivel e equipar outras armas.
    Arma padrao: espada
    HP padrao: 100
    """
    def __init__(self, raca: str, nome: str, nivel: int):
        super().__init__(raca, nome, nivel)
        self.arma = 'Espada'
        self.hp = 100

    def equipar(self, nova_arma: str):
        armas_possiveis = ['Espada', 'Adaga', 'Arco e flecha']
        if isinstance(nova_arma, str) and nova_arma in armas_possiveis:
            print(f'{self.nome} equipou {nova_arma}')
            self.arma = nova_arma

