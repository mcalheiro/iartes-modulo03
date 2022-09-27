import re


class Validador(object):

    def __init__(self):
        self._pattern_arroba = re.compile(r'@', re.I)
        self._pattern_id = re.compile(r'^[^@]+', re.I)
        self._pattern_dominio = re.compile(r'(?<=@)(.*?)(?=\.)', re.I)
        self._pattern_digitos = re.compile(r'^[0-9]*$', re.I)

    def validar_email(self, email):
        """
        Verifica se endereco de email e valido.
        :param email: str
        :return: bool, str
        """
        email_arroba = re.findall(self._pattern_arroba, email)
        email_id = re.findall(self._pattern_id, email)
        email_dominio = re.findall(self._pattern_dominio, email)

        if not email_arroba:
            return False, 'Email nao contem @'

        elif not email_id:
            return False, 'Email nao contem identificador'

        elif len(email_id[0]) > 64:
            return False, 'Identificador muito longo < 64'

        elif not email_dominio:
            return False, 'Dominio invalido'

        else:
            return True, 'Email valido'

    def _cpf_calcular_verificador(self, cpf):
        """
        Calcula digito verificador de CPF.
        :param cpf: str
        :return:
        """
        digitos = list(self._cpf_digitos(cpf))
        resultado = []
        for i in range(len(digitos)):
            resultado.append((i + 1) * int(digitos[i]))

        verificador_1 = sum(resultado) % 11

        if verificador_1 >= 10:
            verificador_1 = 0

        resultado = []
        digitos.append(str(verificador_1))
        for i in range(len(digitos)):
            resultado.append(i * int(digitos[i]))

        verificador_2 = sum(resultado) % 11

        if verificador_2 >= 10:
            verificador_2 = 0

        return f'{verificador_1}{verificador_2}'

    def _cpf_remover_tracos_e_pontos(self, cpf):
        """
        Remove tracos e pontos do CPF,
        deixando somente digitos.
        :param cpf: str
        :return: str
        """
        pattern = r'\.|-'
        return re.sub(pattern, '', cpf)

    def _cpf_digitos(self, cpf):
        """
        Obtém somente digitos do CPF.
        :param cpf: str
        :return: str
        """

        cpf = self._cpf_remover_tracos_e_pontos(cpf)
        return cpf[:-2]

    def _cpf_verificador(self, cpf):
        """
        Obtém somente verificador do CPF.
        :param cpf: str
        :return: str
        """

        cpf = self._cpf_remover_tracos_e_pontos(cpf)
        return cpf[-2:]

    def validar_cpf(self, cpf):
        """
        Verifica se CPF e valido.
        :param cpf: str
        :return: bool, str
        """
        cpf = self._cpf_remover_tracos_e_pontos(cpf)
        cpf_digitos = self._cpf_digitos(cpf)
        cpf_verificador = self._cpf_verificador(cpf)
        cpf_verificador_ = self._cpf_calcular_verificador(cpf)

        if len(cpf_digitos) < 9:
            return False, 'CPF muito curto'

        elif len(cpf_digitos) > 9:
            return False, 'CPF muito longo'

        elif cpf_verificador != cpf_verificador_:
            return False, f'Verificador incorreto ({cpf_verificador} != {cpf_verificador_})'

        else:
            return True, 'CPF valido'
