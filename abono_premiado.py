#Formas de cálculos:
#Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; 

#Outputs:
#1- O salário de cada funcionário, juntamente com o valor do abono;
#2- O número total de funcionário processados;
#3- O valor total a ser gasto com o pagamento do abono;
#4- O número de funcionário que receberá o valor mínimo de 100 reais;
#5 - O maior valor pago como abono;

lista_salarios = [695, 175, 240, 1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
abonos = []
maior_500 = []

taxa_fixa = 100
valor_minimo = 0
qt_colaboradores = len(lista_salarios)

for qtde in lista_salarios:
    if qtde >= 500:
        maior_500.append(qtde)
        novo_salario = qtde*1.20
        abonos.append(novo_salario - qtde)
    else:
        abonos.append(taxa_fixa)
        valor_minimo +=1
        
maior_abono = max(abonos)

print('Salário - Abono')
for i,qtde in enumerate(lista_salarios):
    print(f' { qtde:.1f} - {abonos[i]:.1f}')
print(f'Foram processados {qt_colaboradores} colaboradores.')
print(f'Total gasto com abono: R${sum(abonos)}')
print(f'Valor mínimo pago a {valor_minimo} colaboradores')
print(f'Maior valor pago de abono foi R${maior_abono}.')