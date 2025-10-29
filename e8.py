def soma_elementos(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma

def media_elementos(lista):
  soma = soma_elementos(lista)
  #n_elementos = len(lista)
  #ou:
  n_elementos = 0
  for i in lista:
    n_elementos += 1
  return print(soma/n_elementos)

lista =  [4, 3, 7, 2]
media_elementos(lista)