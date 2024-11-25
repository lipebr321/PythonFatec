# 11 - Ordenação de números

N1 = float(input("Digite o seu primeiro número: "))
N2 = float(input("Digite o seu segundo número: "))
N3 = float(input("Digite o seu terceiro número: "))

if N1 > N2 and N1 > N3 and N2 > N3:
    print("A ordem crescente é:", N3, N2, "e", N1)
elif N1 > N2 and N1 > N3 and N3 > N2:
    print("A ordem crescente é:", N2, N3, "e", N1)
elif N2 > N1 and N2 > N3 and N1 > N3:
    print("A ordem crescente é:", N3, N1, "e", N2)
elif N2 > N1 and N2 > N3 and N3 > N1:
    print("A ordem crescente é:", N1, N3, "e", N2)
elif N3 > N1 and N3 > N2 and N2 > N1:
    print("A ordem crescente é:", N1, N2, "e", N3)
elif N3 > N1 and N3 > N2 and N1 > N2:
    print("A ordem crescente é:", N2, N1, "e", N3)

# 12 - Cálculo de salário com horas extras

HT = float(input("Digite a quantidade de horas trabalhadas: "))
SalarioH = float(input("Digite o valor do seu salário hora: "))

if HT > 160:
    ValorHoraExtra = SalarioH + (SalarioH * 0.5)
    HorasE = HT - 160
    ValorEx = ValorHoraExtra * HorasE
    ValorNormal = SalarioH * 160
    SalarioT = ValorNormal + ValorEx
    print("O valor do salário por hora é:", SalarioH)
    print("O valor das suas horas extras:", ValorEx)
    print("O valor total é de:", SalarioT)
else:
    Salario = SalarioH * HT
    print("O seu salário não terá extras.")
    print("O seu salário normal é de:", Salario)

# 13 - Maior número

N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
N3 = int(input("Digite o terceiro número: "))

if N1 > N2 and N1 > N3:
    print("O maior número dentro desses três é:", N1)
elif N2 > N1 and N2 > N3:
    print("O maior número dentro desses três é:", N2)
else:
    print("O maior número dentro desses três é:", N3)

# 14 - Metade ou quadrado do número

N1 = float(input("Digite um número: "))

if N1 > 0:
    Metade = N1 / 2
    print("A metade desse número é:", Metade)
elif N1 < 0:
    NQ = N1 * N1
    print("O valor desse número ao quadrado é:", NQ)

# 15 - Opção de compra

OPCAOCOMPRA = int(input("Digite em quantas vezes você quer pagar (1, 2 ou 3): "))
VALORPRODUTO = float(input("Digite o valor do produto: "))

if OPCAOCOMPRA == 1:
    ValorAtualizado = VALORPRODUTO - (VALORPRODUTO * 0.05)
    print("Você selecionou o modelo de compra à vista.")
    print("O valor atualizado da sua compra foi de:", ValorAtualizado)
elif OPCAOCOMPRA == 2:
    ValorAtualizado = VALORPRODUTO + (VALORPRODUTO * 0.1)
    ValorParcela = ValorAtualizado / 2
    print("Você selecionou o modelo de duas parcelas para pagamento.")
    print("O valor da sua parcela ficou de:", ValorParcela)
elif OPCAOCOMPRA == 3:
    ValorAtualizado = VALORPRODUTO + (VALORPRODUTO * 0.2)
    ValorParcela = ValorAtualizado / 3
    print("Você selecionou o modelo de três parcelas para pagamento.")
    print("O valor da sua parcela ficou de:", ValorParcela)

# 16 - Conversão de minutos para horas

Minutos = float(input("Digite o número de minutos: "))
Horas = Minutos / 60
print("Os minutos selecionados equivalem a essa quantidade de horas:", Horas)

# 17 - Cálculo do preço do veículo

PrecoF = float(input("Digite o preço de fábrica do veículo: "))
PL = float(input("Digite o percentual do lucro do distribuidor: "))
Imp = float(input("Digite o valor do imposto: "))

PC = PrecoF + (PrecoF * PL / 100) + (PrecoF * Imp / 100)
print("O valor ao consumidor do veículo é:", PC)

# 18 - Cálculo da área de um losango

DM = float(input("Digite o valor da diagonal maior: "))
DN = float(input("Digite o valor da diagonal menor: "))

Area = (DM * DN) / 2
print("O valor da área é:", Area)

# 19 - Valor de bilhetes

OPCAOBILHETE = int(input("Digite a opção do seu bilhete (1, 2 ou 3): "))
Quantidade = int(input("Digite a quantidade de bilhetes comprados: "))

if OPCAOBILHETE == 1:
    ValorF = 2.90 * Quantidade
    print("O valor a ser pago é:", ValorF)
elif OPCAOBILHETE == 2:
    ValorF = 5.60 * Quantidade
    print("O valor a ser pago é:", ValorF)
elif OPCAOBILHETE == 3:
    ValorF = 27.00 * Quantidade
    print("O valor a ser pago é:", ValorF)

# 20 - Multiplicação de números

Num1 = int(input("Digite um número entre 0 e 10: "))
if 0 <= Num1 <= 10:
    print(f"O resultado do número selecionado multiplicado por {Num1}: {Num1 * Num1}")
else:
    print("Número fora do intervalo.")
