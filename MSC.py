import random
import os

matriz = []

def main():
    print("hello")
    print(gerar_matriz(2, 2))
    gerar_grupo_de_animais()

def gerar_matriz (n_linhas, n_colunas):

    for i in range(n_linhas):
        matriz.append( [0] * n_colunas )

    return matriz
    
def gerar_grupo_de_animais():
    x = input("x1")
    y = input("y1")

    matriz[0][0] = x
    matriz[0][1] = y

    x = input("x2")
    y = input("y2")

    matriz[1][0] = x
    matriz[1][1] = y

    print(matriz)


main()
