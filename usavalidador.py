import validador as val


def main():

    v = val.Validador()

    base_dados = []
    x = int(input('Quantas vezes deseja testar? '))

    for i in range(x):
        email = input(f'Email {i+1}: ')
        cpf = input(f'CPF {i+1}: ')
        result1, msg1 = v.validar_email(email)
        result2, msg2 = v.validar_cpf(cpf)

        if not result1:
            print(f'Email invalido: {msg1}')
        if not result2:
            print(f'CPF invalido: {msg2}')
        else:
            entrada = {'email': email, 'cpf': cpf}
            base_dados.append(entrada)

    print(base_dados)


if __name__ == "__main__":
    main()
