import math as m

def retorna_menor(lista):
  menor = m.inf
  for el in lista:
    if type (el) == list:
      ret = retorna_menor(el)
      if ret < menor:
        menor = ret
    else:
      if el < menor:
        menor = el
  return menor
    
  
lista = [109, [9.9, [-5, -10]], [345.67, -171], 123]
retorna_menor(lista)
