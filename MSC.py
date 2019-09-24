import random
import os
import time

matriz = []
direcao = (random.randrange(0, 3)) #0:norte 1:leste 2:sul 3:oeste


def main():
    pi = random.randrange(2, 5)
    pj = random.randrange(2, 12)
    live = 1

    gerar_mapa(7, 14)
    gerar_paredes(7, 14)
    snake(pi, pj)
    prey(random.randrange(2, 5), random.randrange(2, 12))
    while live == 1:
        pi, pj, live = move(pi, pj, live)
    defeat()

def gerar_mapa (n_linhas, n_colunas):

    for i in range(n_linhas):
        matriz.append( [0] * n_colunas )

    return matriz

def snake(x, y):
    matriz[x][y] = 2
    
    mostrar(7, 14)

def prey(x, y):
    matriz[x][y] = 3
    
    mostrar(7, 14)

def gerar_paredes(n_linhas, n_colunas):

    for i in range (n_colunas):
        matriz[0][i] = 1                    #parede superior
        matriz[n_linhas - 1][i] = 1         #parede inferior

    for i in range (n_linhas - 2):
        matriz[i + 1][0] = 1                #parede esquerda
        matriz[i + 1][n_colunas - 1] = 1    #parede direita

    mostrar(7, 14)

def move(pit,pjt, live):
    r = random.randrange(0, 2)

    matriz[pit][pjt] = 0
    
    if r == 1:

        if direcao == 0:
            pjt += -1
        elif direcao == 1:
            pit += -1
        elif direcao == 2:
            pjt += 1
        else:
            pit += 1

    elif r == 2:

        if direcao == 0:
            pjt += 1
        elif direcao == 1:
            pit += 1
        elif direcao == 2:
            pjt += -1
        else:
            pit += -1

    else:

        if direcao == 0:
            pit += -1
        elif direcao == 1:
            pjt += 1
        elif direcao == 2:
            pit += 1
        else:
            pjt += -1

    if matriz[pit][pjt] == 1:
        live = 0

    matriz[pit][pjt] = 2
    mostrar(7, 14)

    return pit, pjt, live

def mostrar(linhas, colunas):

    for i in range(linhas):
        print("\n")
        for j in range(colunas):
          print(matriz[i][j], "  ", end = '')
  
    print(" ")
    time.sleep(2)
    clear()

def defeat():
    print(" derrota")


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

main()
