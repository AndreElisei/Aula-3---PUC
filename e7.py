def media_elementos(lista):
  soma = 0
  #n_elementos = len(lista)
  #ou:
  n_elementos = 0
  for i in lista:
    soma += i
    n_elementos += 1
  return print(soma/n_elementos)

lista =  [4, 3, 7, 2]
media_elementos(lista)