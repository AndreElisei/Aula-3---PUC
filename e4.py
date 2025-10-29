def retorna_maior_str(lista):
  maior = ''
  for i in lista:
    if len(i) > len(maior):
      maior = i
  return print(maior)

lista = ['cenoura', 'batata', 'beterraba', 'couve','agrião']
retorna_maior_str(lista)