meses_trabalhados = int(input('Digite a quantidade de meses trabalhados --> '))
solicitacao = int(input('Digite 1 para a primeira solicitação do benefício, Digite 2 para a segunda solicitação do benefício, Digite 3 para a terceira solicitação do benefício --> '))
mes1 = float(input('Digite o valor do último salário recebido --> '))
mes2 = float(input('Digite o valor do salário anterior a esse recebido --> '))
mes3 = float(input('Digite o valor do salário anterior a esse recebido --> '))

media = (mes1 + mes2 + mes3) / 3
salario_minimo = 1412.00
faixa1 = 2041.39
faixa2 = 3402.65

if media <= faixa1:
    parcela = media * 0.8 
elif media > faixa2 and  media <= faixa2:
    parcela = media * 0.5 + 1633.02
elif media > faixa2:
    parcela = 2313.74 
else:
    parcela = 2824.24


if solicitacao == 1 and meses_trabalhados >= 12:
    if meses_trabalhados >= 12 and meses_trabalhados < 24:
        num_parcelas = 4
    else:
        num_parcelas = 5
elif solicitacao == 2 and meses_trabalhados >= 9:
    num_parcelas = 4 
elif solicitacao == 3 and meses_trabalhados >= 6:
    num_parcelas = 3  
else:
    num_parcelas = 0

if num_parcelas > 0 and media > salario_minimo: 
    print('Você tem direito a', num_parcelas, 'parcelas de R$', parcela)
else:
    print('Você não tem direito ao benefício.')






