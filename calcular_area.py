def descobrir_area():
    """
    Solicita ao usuário o tamanho da área a ser pintada e retorna o valor inserido.

    Returns:
        int: Tamanho da área a ser pintada.
    """
    area = int(input("Tamanho da área para pintar: "))
    return area


def total_litros(area):
    """
    Calcula a quantidade de litros de tinta necessária com base na área fornecida.

    Args:
        area (int): Tamanho da área a ser pintada.

    Returns:
        float: Quantidade de litros de tinta necessária.
    """
    litros = area / 6
    return litros


def calcular_latas(litros):
    """
    Calcula a quantidade de latas e galões de tinta necessários com base na quantidade de litros.

    Args:
        litros (float): Quantidade de litros de tinta necessária.

    Returns:
        tuple: Número de latas, número de galões e litros restantes.
    """
    latas = int(litros / 18)
    litros_faltam = litros % 18
    galoes = 0

    if litros_faltam > 0:
        if litros_faltam % 3.6 > 0:
            galoes = int(litros_faltam / 3.6) + 1
        else:
            galoes = int(litros_faltam / 3.6)

    return latas, galoes, litros_faltam


def calcular_preco(latas, galoes):
    """
    Calcula o preço total com base na quantidade de latas e galões de tinta.

    Args:
        latas (int): Número de latas de tinta.
        galoes (int): Número de galões de tinta.

    Returns:
        tuple: Preço das latas, preço dos galões e preço total.
    """
    preco_lata = latas * 80
    preco_galoes = galoes * 25
    preco_final = preco_lata + preco_galoes
    return preco_lata, preco_galoes, preco_final


area = descobrir_area()
litros = total_litros(area)
latas, galoes, litros_faltam = calcular_latas(litros)
preco_lata, preco_galoes, preco_final = calcular_preco(latas, galoes)

print(f'Vai precisar de {latas} latas e {galoes} galões.')
print(f'Vai gastar um total de R$ {preco_final:.2f}.')