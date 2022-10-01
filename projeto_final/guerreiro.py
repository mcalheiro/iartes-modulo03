from heroi import Heroi


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

    def atacar(self):
        pass

    def equipar(self, nova_arma: str) -> None:
        armas_possiveis = ['Espada', 'Adaga', 'Arco e flecha']
        if isinstance(nova_arma, str) and nova_arma in armas_possiveis:
            print(f'{self.nome} equipou {nova_arma}')
            self.arma = nova_arma

