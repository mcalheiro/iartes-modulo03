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
    def atacar(self) -> None: pass

    @abstractmethod
    def defender(self) -> None: pass
