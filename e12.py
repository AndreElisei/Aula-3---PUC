def soma_elementos_v2(lista):
  soma = 0
  for el in lista:
    if type(el) == list:
      soma = soma + soma_elementos_v2(el)
    elif type(el) == float:
      soma = soma + el
    elif type(el) == int:
      soma = soma + el
  return soma

lista = ['Python', 2, [2, True, [1, 8]], 8, [-3.14159, [3, 'Colab', [6, 9]]]]
soma_elementos_v2(lista)