from environment import Env
import time
import os
import numpy

max_gen = 100

#Valores para a equação de Bellman 
#Q[s, a] = Q[s, a] + alpha*(R + gamma*Max[Q(s’, A)] - Q[s, a])
alpha = 1
gamma = 0.5
epsilon = 0.5

env = Env()

# Valores aleatorios para cada posição*ação
qtable = numpy.random.rand(env.posicao_atualQtd, env.escolhaQtd).tolist()
#print (qtable)
#time.sleep(50)


for i in range(max_gen):
    posicao_atual, recompensa, fim = env.reset()
    movimentos = 0

    while not fim:
        os.system('clear')
        print("Geração", i+1)
        env.mostrar_mapa()
        time.sleep(0.1)

        movimentos += 1

        # ações aleatorias para explorar, baseado em um valor aleatorio, se menor que epsilon
        if numpy.random.uniform() < epsilon:
            escolha = env.randomescolha()
        # escolha baseada na Qtable
        else:
            escolha = qtable[posicao_atual].index(max(qtable[posicao_atual]))

        # ação decidida acima
        proxima_posicao, recompensa, fim = env.mover(escolha)

        #modificando os valores com a equação de Bellman
        qtable[posicao_atual][escolha] = alpha*(recompensa + gamma * max(qtable[proxima_posicao]))

        #atualização da posicao_atual
        posicao_atual = proxima_posicao

    #diminuindo a aleatoriedade das ações ao longo das gerações
    epsilon -= 0.01

    print( movimentos, "movimentos")
    time.sleep(1)
