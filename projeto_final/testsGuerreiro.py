from guerreiro import Guerreiro


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
