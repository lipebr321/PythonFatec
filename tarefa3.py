# 13 - Ordenar dois números
n1 = float(input("Informe o número: "))
n2 = float(input("Informe o número: "))

if n1 > n2:
    print(n2, n1)
else:
    print(n1, n2)

# 14 - Metade ou número ao quadrado
n1 = float(input("\nInforme o número: "))

if n1 > 0:
    print("Metade:", n1 / 2)
else:
    print("Ao quadrado:", n1 ** 2)

# 15 - Verificar se o número é maior que 10
n1 = int(input("\nInforme o número: "))

if n1 > 10:
    print("É MAIOR QUE 10!")
else:
    print("NÃO É MAIOR QUE 10!")

# 16 - Média de quatro notas
n1 = float(input("\nInforme a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))
n4 = float(input("Informe a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 8:
    print("Aprovado")
else:
    print("Reprovado")

# 17 - Custo total das maçãs
n1 = int(input("\nInforme o número de maçãs: "))

if n1 >= 12:
    total = n1 * 1.00
else:
    total = n1 * 1.30

print("Valor da compra:", total)

# 18 - Verificar múltiplo de 9
n1 = int(input("\nInforme o número: "))

if n1 % 9 == 0:
    print("Número múltiplo de 9")
else:
    print("Número não múltiplo de 9")

# 19 - Média ponderada de três provas
n1 = float(input("\nInforme a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))

media = (n1 * 2 + n2 * 3 + n3 * 5) / 10

if media >= 9:
    print("Aprovado")
else:
    print("Reprovado")

# 20 - Verificar se pode votar
ano_atual = int(input("\nInforme o ano atual: "))
ano_nasc = int(input("Informe o ano de nascimento: "))

idade = ano_atual - ano_nasc

if idade >= 16:
    print("Você pode votar este ano")
else:
    print("Você não pode votar este ano")

# 21 - Antecessor e sucessor
n1 = int(input("\nInforme o número inteiro: "))

print("Antecessor:", n1 - 1, ", Número:", n1, ", Sucessor:", n1 + 1)

# 22 - Calcular minutos desde o início do dia
hora = int(input("\nInforme a hora do dia: "))
minutos = int(input("Informe os minutos: "))

total_minutos = hora * 60 + minutos

print("Se passaram", total_minutos, "minutos hoje.")
