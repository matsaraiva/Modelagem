import random
import os

matriz = []

def main():
    gerar_mapa(4, 4)
    gerar_paredes()
    snake(1, 1)
    prey(2, 2)
    move()
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

def gerar_paredes():

    matriz[0][0] = 1
    matriz[0][1] = 1
    matriz[0][2] = 1
    matriz[0][3] = 1

    matriz[1][0] = 1
    matriz[1][3] = 1

    matriz[2][0] = 1
    matriz[2][3] = 1

    matriz[3][0] = 1
    matriz[3][1] = 1
    matriz[3][2] = 1
    matriz[3][3] = 1

    mostrar(4, 4)

def move():
    r = random.randrange(0, 3)
    
    if r == 1:
        matriz[1][1] = 0
        matriz[1][0] = 2
    elif r == 2:
        matriz[1][1] = 0
        matriz[1][2] = 2
    else:
        matriz[1][1] = 0
        matriz[0][1] = 2

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
