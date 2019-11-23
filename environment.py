import time
import numpy

class Env():
    def __init__(self):
        self.altura = 5
        self.largura = 9
        self.posX = 1
        self.posY = self.altura-2
        self.alvoX = self.largura-2
        self.alvoY = self.altura-2
        self.escolhas = [0, 1, 2, 3]
        self.posicao_atualQtd = self.altura*self.largura
        self.escolhaQtd = len(self.escolhas)

    def reset(self):
        self.posX = 1;
        self.posY = self.altura-2;
        self.fim = False;
        return 0, 0, False;

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

        fim = self.posX==self.alvoX and self.posY==self.alvoY;


        # proxima posição da IA, baseado no mapeamento de X e Y para cada posição na grade
        proxima_posicao = self.largura*self.posY + self.posX;

        #print ("proxima posicao: ", proxima_posicao)
        #time.sleep(0.1)

        recompensa = 1 if fim else 0;
        return proxima_posicao, recompensa, fim;

    # return a random escolha
    def randomescolha(self):
        return numpy.random.choice(self.escolhas);

    def mostrar_mapa(self):
        for i in range(self.altura):
            for j in range(self.largura):
                if self.posY==i and self.posX==j:
                    print("1 ", end='');
                elif self.alvoY==i and self.alvoX==j:
                    print("2 ", end='');
                else:
                    print("0 ", end='');
            print("");
