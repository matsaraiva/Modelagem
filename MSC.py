import random
import os

matriz = []

def main():
    print("hello")
    print(gerar_mapa(4, 4))
    gerar_paredes()
    snake(1, 1)
    prey(2, 2)
    move()

def gerar_mapa (n_linhas, n_colunas):

    for i in range(n_linhas):
        matriz.append( [0] * n_colunas )

    return matriz

def snake(x, y):
    matriz[x][y] = 2
    
    print(matriz)

def prey(x, y):
    matriz[x][y] = 3
    
    print(matriz)

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

    print(matriz)

def move():
    r = random.randrange(0, 3)
    
    if r == 1:
        matriz[1][1] = 0
        matriz[1][0] = 2
    elif r == 2:
        matriz[1][1] = 0
        matriz[1][2] = 2
    else
        matriz[1][1] = 0
        matriz[0][1] = 2

    print(matriz)

main()
