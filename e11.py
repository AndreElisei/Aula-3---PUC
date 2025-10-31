def soma_elementos_v1(lista):
  soma = 0
  for el in lista:
    if type(el) == list:
      soma = soma + soma_elementos_v1(el)
    else:
      soma = soma + el
  return soma

lista = [2, [2, [1, 8]], 8, [-3.14159, [3, [6, 9]]]]
soma_elementos_v1(lista)