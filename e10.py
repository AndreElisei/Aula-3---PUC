def soma_elementos(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma

def sumariza_qtd(listao):
  for (i, lista) in listao:
    print (f'Item:{i}\t quantidade: {soma_elementos(lista)}')
  
listao = [['Detergente', [8, 7, 9, 2, 10]], ['Sabonete', [7, 2, 6, 5, 8, 1]], ['Escova', [9, 9, 10, 0, 9, 1]]]
sumariza_qtd(listao)