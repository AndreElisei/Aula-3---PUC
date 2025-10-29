def retorna_maior_indice_str(lista):
  maior = ''
  indice_maior = 0

  for(indice, el) in enumerate(lista):
    if len(el) > len(maior):
      maior = el
      indice_maior = indice
  return print(f'A maior palavra é: {maior}, que tem o índice: {indice_maior}')

lista = ['cenoura', 'batata', 'beterraba', 'couve','agrião']
retorna_maior_indice_str(lista)