#Este é um projeto simples que calcula a média nacional das temperaturas ao longo dos meses e identifica quais meses tiveram temperaturas acima dessa média
# Esse projeto pode ser utilizado como exemplo para entender o uso de listas, loops e condicionais em Python.
meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]


media_nacional = sum(temperaturas)/len(temperaturas)
print(f'A média nacional é de {media_nacional:.1f} graus.')
meses_acima = []
for i, qtde in enumerate(meses):
    #print(meses[i], temperaturas[i])
    if temperaturas[i] > media_nacional:
        meses_acima.append(qtde)
#print(meses_acima)
print(f'Os meses com a temperatura acima da média foram: {meses_acima}')