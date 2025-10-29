# Programa para retornar o maior valor da lista e seu índice

def retorna_maior(lista):
    if not lista:
        raise ValueError('A lista está vazia')
    
    maior_valor = lista[0]
    indice_maior = 0

    for i in range(1, len(lista)):
        if lista[i] > maior_valor:
            maior_valor = lista[i]
            indice_maior = i

    return maior_valor, indice_maior

lista = [15, 56, 54, 421, 23, -43, 4214, 23]
maior, indice = retorna_maior(lista)

print(f'Maior valor: {maior}, encontrado no índice: {indice}')