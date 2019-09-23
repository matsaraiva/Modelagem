import random
import os

matriz = []
direcao = (random.randrange(0, 3)) #0:norte 1:leste 2:sul 3:oeste
print("direcao: ", direcao)

pi = 1
pj = 1

def main():
    gerar_mapa(4, 4)
    gerar_paredes(4, 4)
    snake(1, 1)
    prey(2, 2)
    move(pi, pj)
    mostrar(4, 4)

def gerar_mapa (n_linhas, n_colunas):

    for i in range(n_linhas):
        matriz.append( [0] * n_colunas )

    return matriz

def snake(x, y):
    matriz[x][y] = 2
    
    mostrar(4, 4)

def prey(x, y):
    matriz[x][y] = 3
    
    mostrar(4, 4)

def gerar_paredes(n_linhas, n_colunas):

    for i in range (n_colunas):
        matriz[0][i] = 1                #parede superior
        matriz[n_linhas - 1][i] = 1         #parede inferior

    for i in range (n_linhas - 2):
        matriz[i + 1][0] = 1            #parede esquerda
        matriz[i + 1][n_colunas - 1] = 1    #parede direita

    mostrar(4, 4)

def move(pi,pj):
    r = random.randrange(0, 2)

    matriz[pi][pj] = 0
    
    if r == 1:

        if direcao == 0:
            pj += -1
        elif direcao == 1:
            pi += -1
        elif direcao == 2:
            pj += 1
        else:
            pi += 1

        matriz[pi][pj] = 2

    elif r == 2:

        if direcao == 0:
            pj += 1
        elif direcao == 1:
            pi += 1
        elif direcao == 2:
            pj += -1
        else:
            pi += -1

        matriz[pi][pj] = 2

    else:

        if direcao == 0:
            pi += -1
        elif direcao == 1:
            pj += 1
        elif direcao == 2:
            pi += 1
        else:
            pj += -1

        matriz[pi][pj] = 2

    mostrar(4, 4)

def mostrar(linhas, colunas):

    for i in range(linhas):
        print("\n")
        for j in range(colunas):
          print(matriz[i][j], "  ", end = '')
  
    input("\nAperte enter para continuar")
    clear()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

main()
