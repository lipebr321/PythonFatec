# 0.

populacao_a = 90000 
populacao_b = 200000
taxa_crescimento_a = 0.03 
taxa_crescimento_b = 0.015 
anos = 0 


while populacao_a < populacao_b:

    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1 


print("A população do país A ultrapassará ou igualará a do país B em", anos, "anos.")

# 1.

total_habitantes = 2
salarios = 0
filhos_total = 0
maior_salario = 0
menor_salario = float('inf') 
contagem_salario_baixo = 0  


contador = 0
while contador < total_habitantes:

    salario = float(input("Digite o salário do habitante: R$ "))
    filhos = int(input("Digite o número de filhos do habitante: "))
    

    salarios += salario
    filhos_total += filhos
    
    
    if salario > maior_salario:
        maior_salario = salario
    if salario < menor_salario:
        menor_salario = salario
    
   
    if salario < 1200:
        contagem_salario_baixo += 1
    
    contador += 1  


media_salario = salarios / total_habitantes
media_filhos = filhos_total / total_habitantes
percentual_salario_baixo = (contagem_salario_baixo / total_habitantes) * 100


print("Média de salário da população: R$ {:.2f}".format(media_salario))
print("Média do número de filhos: {:.2f}".format(media_filhos))
print("Maior salário: R$ {:.2f}".format(maior_salario))
print("Menor salário: R$ {:.2f}".format(menor_salario))
print("Percentual de pessoas com salário menor que R$ 1200,00: {:.2f}%".format(percentual_salario_baixo))




#  2.

total_funcionarios = 0
idade_masculino_total = 0
peso_feminino_total = 0
altura_total = 0
peso_total = 0
idade_total = 0
contador_masculino = 0
contador_feminino = 0


while True:
    idade = int(input("Digite a idade do funcionário (ou -1 para encerrar): "))
    
    if idade == -1:
        break

    sexo = int(input("Digite o sexo do funcionário (1 - masculino, 2 - feminino): "))
    peso = float(input("Digite o peso do funcionário (kg): "))
    altura = float(input("Digite a altura do funcionário (m): "))
    
    total_funcionarios += 1
    altura_total += altura
    peso_total += peso
    idade_total += idade

    if sexo == 1:
        idade_masculino_total += idade
        contador_masculino += 1
    elif sexo == 2:
        peso_feminino_total += peso
        contador_feminino += 1

if contador_masculino > 0:
    media_idade_masculino = idade_masculino_total / contador_masculino
else:
    media_idade_masculino = 0

if contador_feminino > 0:
    media_peso_feminino = peso_feminino_total / contador_feminino
else:
    media_peso_feminino = 0

media_altura = altura_total / total_funcionarios if total_funcionarios > 0 else 0
media_peso = peso_total / total_funcionarios if total_funcionarios > 0 else 0
media_idade = idade_total / total_funcionarios if total_funcionarios > 0 else 0


print("Média de idade dos funcionários do sexo masculino: {:.2f}".format(media_idade_masculino))
print("Média de peso dos funcionários do sexo feminino: {:.2f} kg".format(media_peso_feminino))
print("Média de altura: {:.2f} m".format(media_altura))
print("Média de peso: {:.2f} kg".format(media_peso))
print("Média de idade: {:.2f} anos".format(media_idade))
print("Total de funcionários do sexo masculino: {}".format(contador_masculino))
print("Total de funcionários do sexo feminino: {}".format(contador_feminino))