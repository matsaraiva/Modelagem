from environment import Env
import time
import os
import numpy

max_gen = 200
resultados = []

#Valores para a equação de Bellman 
#Q[s, a] = Q[s, a] + alpha*(R + gamma*Max[Q(s’, A)] - Q[s, a])
alpha = 1 #taxa de aprendizando
gamma = 0.9 #importancia para recompensas maiores   #0.1/0.9
epsilon = 0.7 #define a frequencia de exploração    #0.55/0.7

env = Env()

# Valores aleatorios para cada posição*ação
qtable = numpy.random.rand(env.posicao_atualQtd, env.escolhaQtd).tolist()
#print (qtable)
#time.sleep(50)


for i in range(max_gen):
    posicao_atual, recompensa, fim, fim_melhor = env.reset()
    movimentos = 0

    while not (fim or fim_melhor):
        os.system('clear')
        print("Geração", i+1)
        env.mostrar_mapa()
        time.sleep(0.02)

        movimentos += 1

        # ações aleatorias para explorar, baseado em um valor aleatorio, se menor que epsilon
        if numpy.random.uniform(0, 1) < epsilon:
            escolha = env.randomescolha()
        # escolha baseada na Qtable(escolhe o maior valor na grade de escolhas)
        else:
            escolha = qtable[posicao_atual].index(max(qtable[posicao_atual])) 
            #print (max(qtable[posicao_atual]))
            #print (qtable[posicao_atual])
            #print (escolha)
            #time.sleep(50)

        # ação decidida acima
        proxima_posicao, recompensa, fim, fim_melhor = env.mover(escolha)

        #modificando os valores com a equação de Bellman
        qtable[posicao_atual][escolha] = alpha*(recompensa + gamma * max(qtable[proxima_posicao]))

        #atualização da posicao_atual
        #print (proxima_posicao)
        #time.sleep(10)
        posicao_atual = proxima_posicao

    #diminuindo a aleatoriedade das ações ao longo das gerações
    if epsilon >= 0.01:
        epsilon -= epsilon*0.02

    #print (epsilon)
    #diminuindo a taxa de aprendizado ao longo das gerações
    #alpha -= 0.005*alpha

    if fim:
        print("Completou com ", movimentos, "movimentos\n Resultado: Menor recompensa")
        resultados.append("A")
    else:
        print("Completou com ", movimentos, "movimentos\n Resultado: Maior recompensa")
        resultados.append("B")
    
    print(resultados)
    time.sleep(1)
