# 1 

 consumo = int(input("Digite o consumo de água em m³: ")) 

 

valor_conta = 7 

 

if consumo <= 10: 

    valor_conta = 7 

elif consumo <= 30: 

    valor_conta += (consumo - 10) * 1 

elif consumo <= 100: 

    valor_conta += (30 - 10) * 1       

    valor_conta += (consumo - 30) * 2   

else: 

    valor_conta += (30 - 10) * 1      

    valor_conta += (100 - 30) * 2       

    valor_conta += (consumo - 100) * 5  

 

print(f"O valor da conta de água é: R$ {valor_conta:.2f}") 

 

# 2  

 

 

gasolina = float(input("Digite o valor do L da gasolina")) 

etanol = float (input("Digite o valor do L do etanol")) 

valor_final = etanol / gasolina 

if valor_final>= 0.7: 

    print("Vale a pena colocar gasonila") 

else: 

    print("Vale a pena colocar etanol") 