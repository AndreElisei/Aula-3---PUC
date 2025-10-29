def compara_elementos(lista1, lista2):
  if len(lista1) != len(lista2):
    return False
  for item in lista1:
    if item not in lista2:
      return False
  return True

lista1 = [12, True, -1, 'Iguais?', 1]
lista2 = [True, -1, 'Iguais?', 12]
compara_elementos(lista1, lista2)