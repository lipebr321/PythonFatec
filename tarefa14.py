def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))


    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False


    def calcular_digito(cpf, peso_inicial):
        soma = 0
        i = 0
        while i < peso_inicial - 1:
            soma += int(cpf[i]) * (peso_inicial - i)
            i += 1
        digito = 11 - (soma % 11)
        return 0 if digito >= 10 else digito


    return calcular_digito(cpf, 10) == int(cpf[9]) and calcular_digito(cpf, 11) == int(cpf[10])


cpf = input("Digite o CPF: ")
print("CPF válido." if validar_cpf(cpf) else "CPF inválido.")