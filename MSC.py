import random
import os

def main():
    print("hello")
    print(gerar_matriz(2, 2))

def gerar_matriz (n_linhas, n_colunas):
    matriz = []

    for _ in range(n_linhas):
        matriz.append( [0] * n_colunas )

    return matriz
    
def gerar_animais():
    x = input("x")
    y = input("y")

main()
