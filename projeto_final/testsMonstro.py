from monstro import Monstro


class TestMonstro:

    def test_atacar_sucesso_fora_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.atacar(-1) == 'Ataque sem efeito.'
        assert m.atacar(4) == 'Ataque sem efeito.'
        assert m.atacar(11) == 'Ataque sem efeito.'

    def test_atacar_sucesso_dentro_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.atacar(6) == f'{m.nome} atacou.'

    def test_defender_sucesso_fora_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.defender(-1) == 'Tentativa de defesa falha.'
        assert m.defender(5) == 'Tentativa de defesa falha.'
        assert m.defender(11) == 'Tentativa de defesa falha.'

    def test_defender_sucesso_dentro_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.defender(7) == f'{m.nome} defendeu.'

    def test_curar_sucesso_fora_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.curar(-1) == 'Tentativa de cura falhou.'
        assert m.curar(7) == 'Tentativa de cura falhou.'
        assert m.curar(11) == 'Tentativa de cura falhou.'

    def test_curar_sucesso_dentro_do_intervalo(self):
        m = Monstro('Comum', 'Gaguinho', 10)
        assert m.curar(9) == f'{m.nome} restaurou HP.'
