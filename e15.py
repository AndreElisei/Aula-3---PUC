import random as r

def gera_lista():
    contadores = [0] * 13
    for _ in range(100000):
        numero = r.randint(0, 1600)
        if 0 <= numero <= 12:
            contadores[numero] += 1
    return contadores

def exibe_elemento(lista):
  for (i, el) in enumerate(lista):
    print(f'{i:2.0f}. {el*'*'}')
  return

# Programa principal
contadores = gera_lista()
exibe_elemento(contadores)
