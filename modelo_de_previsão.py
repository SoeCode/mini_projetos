precos_imoveis = [2.17,1.54,1.45,1.94,2.37,2.3,1.79,1.8,2.25,1.37,2.4,1.72,2,1.69,1.63,2.01,2.25,1.61,1.02,1.19,1.86,2.15,2.03,1.61,1.52,1.56,1.69,1.47,1.09,2.47,1.62,2.15,1.81,2.49,2.08,1.02,1.68,1.53,1.2,1.29,1.88,1.92,2.14,1.95,2.48,2.44,1.41,1.98,1.89,1.69,1.95,1.42,1.57,2.32,1.23,1.43,1.35,1.49,2.39,2.37,1.3,2.25,1.5,1.35,2.06,1.05,1.7,2.29,2.44,2.09,1.81,2.04,2.45,1.42,2.09,2.19,2.09,1,2.23,1.39,2,1.29,1.55,1.67,2.06,1.89,2.07,2.39,1.93,1.51,1.73,1.66,1.18,1.13,1.69,2.48,1.26,1.75, 1.51, 1.73]
tamanho_imoveis = [207,148,130,203,257,228,160,194,232,147,222,165,184,175,147,217,214,171,86,111,180,211,210,168,156,154,179,163,99,246,162,205,195,263,198,121,149,140,122,119,197,210,218,202,258,256,135,203,173,152,197,145,154,252,141,141,151,133,232,229,134,215,155,138,186,120,152,213,256,219,200,210,238,140,224,233,222,120,233,151,185,111,149,186,194,194,222,223,185,157,154,164,129,128,169,240,136,191, 157, 154]
def definir_valor(preco, tamanho, fator=0.1):
    '''Separa em listas de análises, definidas em treino e teste;
    
    Parameteres:
    arg1 = uma lista com os preços
    arg2 = lista de tamanhos
    arg3 = fator escolhido para ser treino | já predefinido como 10% da lista para teste
    
    Returns:
    lista tratada de acordo com o fator, separadas em treino e teste.
    
    '''
    if len(preco) == len(tamanho):
        i = int((1-fator) * len(tamanho))
        lista_preco_treino = preco[:i]
        lista_preco_teste = preco[i:]
        lista_tamanho_treino = tamanho[:i]
        lista_tamanho_teste = tamanho[i:]
        return lista_preco_treino, lista_preco_teste, lista_tamanho_treino, lista_tamanho_teste
    else:
        print('preço dos imoveis e tamanho dos imoveis tem números diferentes.')
        return

    
imoveis_treino, imoveis_teste, tamanho_treino, tamanho_teste = definir_valor(precos_imoveis, tamanho_imoveis, 0.07)

print(imoveis_treino, imoveis_teste)
print(tamanho_treino, tamanho_teste)