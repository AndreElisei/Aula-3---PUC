def busca_aluno(lista_alunos, aluno, nota):
  for (i, el) in enumerate(lista_alunos):
    if el[0] == aluno:
      el[1] = nota
      return print(f'Alterado, lista nova: \n{lista_alunos}')
  return print('Aluno não encontrado')

lista = [['Mickey', 8.7], ['Pateta', 6.5], ['Minnie', 9.9], ['Pato Donald', 7.2]]
aluno = input('Informe o nome do aluno para alterar sua nota: ')
nota = int(input('Informe a nova nota do aluno: '))
busca_aluno(lista, aluno, nota)