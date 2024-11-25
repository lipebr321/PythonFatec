#  0. Faça um programa para calcular e exibir a tabuada de um número qualquer (esse número deverá ser fornecido pelo usuário).

entrada = int(input('Digite um numero para ver a tabuada de 0 a 10 dele -->  '))


#calculo da tabuada 

print('-' * 12)
print('{} X {:2} = {}'.format(entrada, 1, entrada*1) )
print('{} X {:2} = {}'.format(entrada, 2, entrada*2) )
print('{} X {:2} = {}'.format(entrada, 3, entrada*3) )
print('{} X {:2} = {}'.format(entrada, 4, entrada*4) )
print('{} X {:2} = {}'.format(entrada, 5, entrada*5) )
print('{} X {:2} = {}'.format(entrada, 6, entrada*6) )
print('{} X {:2} = {}'.format(entrada, 7, entrada*7) )
print('{} X {:2} = {}'.format(entrada, 8, entrada*8) )
print('{} X {:2} = {}'.format(entrada, 9, entrada*9) )
print('{} X {:2} = {}'.format(entrada, 10, entrada*10) )
print('-' * 12)


#  1. Faça um programa para exibir na tela a palavra “programa” cem vezes.

print('-' * 15)
for i in range(1, 101): 
    print("programa")
print('-' * 15)


#  2. Faça um programa para exibir todos os números (de 1 a 100).

print('-' * 15)
for i in range(1, 101):  
    print(0 + i)
print('-' * 15)

#  3. Faça um programa para exibir todos os números (de 1 a N), onde N é um número fornecido pelo usuário.

entrada = int(input('Digite um numero -->  '))

print('-' * 15)
for i in range(0, entrada): 
    print(1 + i)
print('-' * 15)

#  4. Faça um programa para exibir todos os números ímpares (de 1 a N), onde N é um número fornecido pelo usuário.

entrada = int(input('Digite um numero -->  '))

print('-' * 15)
for i in range(1, entrada, 2):
    print(i)
print('-' * 15)

#  5. Faça um programa para exibir todos os números do intervalo [-100 e 400].

print('-' * 15)
for i in range(-100, 401):  
    print(0 + i)
print('-' * 15)

#  6. Faça um programa para exibir todos os números impares do intervalo [ 2 a 5000 ] em ordem decrescente.

print('-' * 15)
numbers = list(range(3, 5001, 2))
for i in sorted(numbers, reverse=True):
    print(i)
print('-' * 15)


# 7. Faça um programa para exibir uma sequência de valores em ordem crescente. O programa deverá solicitar o primeiro valor, o último valor e o intervalo padrão entre eles; a seguir deverá exibir os valores.

entrada1 = int(input('Digite o numero inicial -->  '))
entrada2 = int(input('Digite o numero final -->  '))
entrada3 = int(input('Digite o intervalo -->  '))

print('-' * 15)
for i in range(entrada1, entrada2 , entrada3):
    print(i)
print('-' * 15)


#  8. Escreva um programa que receba a idade de dez pessoas, calcule e imprima a quantidade de pessoas maiores de idade (idade >= 18 anos).

idades = [
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  ')),
    int(input('Digite a idade -->  '))
]

maiores_18 = sum(1 for idade in idades if idade > 18)

print(f"Quantidade de idades maiores que 18: {maiores_18}")

#  9. Faça um programa que leia a idade de todos os alunos de uma turma de quarenta alunos, calcule e apresente:
- A soma das idades de todos os alunos;
- A média de idade dos alunos.

idades = []
total_idades = 0

for i in range(40):
    idade = int(input(f'Digite a idade {i+1} --> '))
    idades.append(idade)
    total_idades += idade

media = total_idades / len(idades)

print(f"Soma total das idades: {total_idades}")
print(f"Média das idades: {media:.2f}")


#  10. Faça um programa que leia cem valores e no final, informe o maior e o menor valor digitado.

numeros = []

for i in range(100):
    numero = int(input(f'Digite o número {i+1}: '))
    numeros.append(numero)


maior_numero = menor_numero = numeros[0]


for numero in numeros[1:]:
    if numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero

# Imprime o resultado
print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')