import time
import numpy
import random

class Env():
    def __init__(self):
        self.altura = 5
        self.largura = 16
        self.posX = 5
        self.posY = 2
        self.alvoX = 0
        self.alvoY = random.randrange(1, self.altura-2)
        self.alvobonusX = self.largura-1
        self.alvobonusY = random.randrange(1, self.altura-2)
        self.escolhas = [0, 1, 2, 3]
        self.posicao_atualQtd = self.altura*self.largura
        self.escolhaQtd = len(self.escolhas)

    def reset(self):
        self.posX = 5;
        self.posY = 2;
        self.fim = False;
        self.fim_melhor = False
        return 37, 0, False, False;

    # take escolha
    def mover(self, escolha):
        if escolha==0: # left
            self.posX = self.posX-1 if self.posX>0 else self.posX;
        if escolha==1: # right
            self.posX = self.posX+1 if self.posX<self.largura-1 else self.posX;
        if escolha==2: # up
            self.posY = self.posY-1 if self.posY>0 else self.posY;
        if escolha==3: # down
            self.posY = self.posY+1 if self.posY<self.altura-1 else self.posY;

        
        
        fim = (self.posX==self.alvoX and self.posY==self.alvoY)
        fim_melhor = (self.posX==self.alvobonusX and self.posY==self.alvobonusY)

        # proxima posição da IA, baseado no mapeamento de X e Y para cada posição na grade
        proxima_posicao = self.largura*self.posY + self.posX;

        #print ("proxima posicao: ", proxima_posicao)
        #time.sleep(0.1)

        recompensa = 1 if fim else 0;
        recompensa = 100 if fim_melhor else 0;
        return proxima_posicao, recompensa, fim, fim_melhor;

    # return a random escolha
    def randomescolha(self):
        return numpy.random.choice(self.escolhas);

    def mostrar_mapa(self):
        for i in range(self.altura):
            for j in range(self.largura):
                if self.posY==i and self.posX==j:
                    print("Q ", end='');
                elif self.alvoY==i and self.alvoX==j:
                    print("A ", end='');
                elif self.alvobonusY==i and self.alvobonusX==j:
                    print("B ", end='');
                else:
                    print("_ ", end='');
            print("");
