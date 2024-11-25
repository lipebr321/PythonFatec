#  1 - Faça um programa que calcule a divisão entre dois números.

n1 = float(input("Informe o primeiro numero : "))
n2 = float(input("Informe o segundo numero : "))

divisao = n1/n2

print("O resultado é : " , divisao)


#  2 - Faça um programa que calcule o resto da divisão entre dois números inteiros.

n1 = int(input("Informe o primeiro numero inteiro : "))
n2 = int(input("Informe o segundo numero inteiro : "))

resto = n1%n2

print("O resultado é : " , resto)


#  3 - Faça um programa que calcule a divisão, o resto da divisão e a divisão "inteira" entre dois números inteiros.

n1 = float(input("Informe a nota do primeiro numero : "))
n2 = float(input("Informe a nota do segundo numero : "))

divisao = n1/n2
resto = n1%n2
inteiro = n1//n2

print("O resultado da divisao é : " , divisao, "O redto é : ", resto, "O inteiro é : ", inteiro)


#  4 - Faça um programa para informar se uma pessoa é maior de idade.

idade = int(input("Informe a idade : "))

if (idade >= 18):
    print("Maior de idade ")
    
else:
    print("Menor de idade ")


#  5 - Faça um programa que informe se um ano é bissexto  (regra geral: todo ano bissexto é divisível por 4).

ano = int(input("Informe o ano : "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0: 
     print("Ano bissexto. ") 

else: 
    print("Não é um ano bissexto.")


#  6 - Faça um programa que informe se um número e divisível por 10.

n1 = float(input("Informe o ano : "))

if (n1 % 10 == 0 ):
     print("Numero divisivelpor 10. ") 

else: 
    print("Não é divisivel por 10.")

#  7 - Faça um programa que informe se um número é múltiplo de 5.

n1 = float(input("Informe o numero : "))

if (n1 % 5 == 0 ):
     print("Numero multiplo de 5. ") 

else: 
    print("Não é multiplo de 5.")
    

#  8 - Faça um programa que informe se um número é par ou ímpar.

n1 = float(input("Informe o numero : "))

if (n1 % 2 == 0 ):
     print("Numero par. ") 

else: 
    print("Numero impar.")
    

#  9 - Faça um programa que leia o nome e a idade de duas pessoas e mostre a soma das idades.

n1 = int(input("Informe a primeira idade : "))
n2 = int(input("Informe a segunda idade : "))

soma = n1+n2


print ("A soma das idades é : " soma)

#  10 - Elabore um programa que leia dois valores, calcule e apresente a divisão do maior pelo menor.

n1 = float(input("Informe o primeiro numero : "))
n2 = float(input("Informe o segundo numero : "))

result = n1 / n2
result2 = n2 / n1
 
if (n1 > n2 ):
   
     print(result) 

else: 
   
    print( result2)
    

#  11 - Faça um programa para receber um valor e escrever se é “positivo” ou “negativo” (considere o valor zero como positivo).

n1 = float(input("Informe o numero : "))

if (n1 > 0):
    print("Positivo ")
    
else:
    print("negativo ")

#  12 - Faça um programa que receba dois números e apresente o menor.

n1 = float(input("Informe o numero : "))
n2 = float(input("Informe o numero : "))

if (n1 > n2):
    print(n1)
    
else:
    print(n2)

