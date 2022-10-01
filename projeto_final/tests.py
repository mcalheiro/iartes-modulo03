from personagem import Heroi, Guerreiro


class TestGuerreiro:

    def test_equipar_arma_invalida(self):
        g = Guerreiro('Coelho', 'Pernalonga', 10)
        arma = 'Pistola'
        g.equipar('Pistola')
        assert g.arma is not arma

    def test_equipar_arma_numero(self):
        g = Guerreiro('Coelho', 'Pernalonga', 10)
        arma = 42
        g.equipar(arma)
        assert g.arma is not arma

    def test_equipar_arma_valida(self):
        g = Guerreiro('Coelho', 'Pernalonga', 10)
        arma = 'Adaga'
        g.equipar(arma)
        assert g.arma is arma

    def test_atacar_sucesso_fora_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.atacar(-1) == 'Ataque sem efeito.'
        assert h.atacar(5) == 'Ataque sem efeito.'
        assert h.atacar(11) == 'Ataque sem efeito.'

    def test_atacar_sucesso_dentro_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.atacar(7) == f'{h.nome} atacou.'

    def test_defender_sucesso_fora_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.defender(-1) == 'Tentativa de defesa falha.'
        assert h.defender(6) == 'Tentativa de defesa falha.'
        assert h.defender(11) == 'Tentativa de defesa falha.'

    def test_defender_sucesso_dentro_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.defender(8) == f'{h.nome} defendeu.'

    def test_fugir_sucesso_fora_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.fugir(-1) == 'Impossível fugir.'
        assert h.fugir(7) == 'Impossível fugir.'
        assert h.fugir(11) == 'Impossível fugir.'

    def test_fugir_sucesso_dentro_do_intervalo(self):
        h = Heroi('Coelho', 'Pernalonga', 10)
        assert h.fugir(9) == f'{h.nome} fugiu da luta.'
