#outra forma (gabarito)
import math as m

def retorna_maior(lista):
  maior = -m.inf
  for i in lista:
    if i > maior:
      maior = i
  return print(maior)

lista = [15, 56, 54, 421, 23, -43, 4214, 23]
retorna_maior(lista)