import validador as val


class TestEmail:
    """
    Verificar se endereco de email é valido.
    Fonte: https://help.returnpath.com/hc/en-us/articles/220560587-What-are-the-rules-for-email-address-syntax-
    """


    def test_email_sem_arroba(self):
        email = 'mauriciocalheiro95gmail.com'
        v = val.Validador()
        assert v.validar_email(email)[0] is False


    def test_email_sem_identificador(self):
        email = '@gmail.com'
        v = val.Validador()
        assert v.validar_email(email)[0] is False


    def test_email_idenficador_longo(self):
        email = 'mauriciocalheiro95'*4 + '@gmail.com'
        v = val.Validador()
        assert v.validar_email(email)[0] is False


class TestCPF:
    """
    Verificar se CPF é valido.
    Fonte: https://www.calculadorafacil.com.br/computacao/validar-cpf
    """


    def test_cpf_curto(self):
        cpf = '011931-43'
        v = val.Validador()
        assert v.validar_cpf(cpf)[0] is False


    def test_cpf_longo(self):
        cpf = '011931542434-34'
        v = val.Validador()
        assert v.validar_cpf(cpf)[0] is False

    def test_cpf_validador(self):
        cpf = '123456789-01'
        v = val.Validador()
        assert v.validar_cpf(cpf)[0] is False
