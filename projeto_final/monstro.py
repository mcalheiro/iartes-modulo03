from personagem import Personagem


class Monstro(Personagem):
    """
    Possui todos os atributos de Personagem + tipo.
    Tipos: comum, chefao
    """
    def __init__(self, tipo: str, nome: str, nivel: int):
        super().__init__(nome, nivel)
        self.tipo = tipo

    @property
    def tipo(self):
        return self._raca

    @property
    def nome(self):
        return self._nome

    @property
    def nivel(self):
        return self._nivel

    @tipo.setter
    def tipo(self, raca_personagem):
        self._raca = raca_personagem

    @nome.setter
    def nome(self, nome_personagem):
        self._nome = nome_personagem

    @nivel.setter
    def nivel(self, nivel_personagem):
        self._nivel = nivel_personagem

    def atacar(self, sucesso) -> str:
        if sucesso in range(5, 11):
            return f'{self.nome} atacou.'
        else:
            return 'Ataque sem efeito.'

    def defender(self, sucesso) -> str:
        if sucesso in range(6, 11):
            return f'{self.nome} defendeu.'
        else:
            return 'Tentativa de defesa falha.'

    def curar(self, sucesso) -> str:
        if sucesso in range(8, 11):
            return f'{self.nome} restaurou HP.'
        else:
            return 'Tentativa de cura falhou.'
