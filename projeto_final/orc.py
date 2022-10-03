from monstro import Monstro


class Orc(Monstro):

    def __init__(self, tipo: str, nome: str, nivel: int):
        super().__init__(tipo, nome, nivel)

    def emboscar(self, inimigo) -> None:
        self.atk *= 1.50
        inimigo.hp -= self.atk
        print(f'A emboscada de {self.nome} funcionou'
              f'Resta apenas {inimigo.hp} HP para {inimigo.nome}.')
