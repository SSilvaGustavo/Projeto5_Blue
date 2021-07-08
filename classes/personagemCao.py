from classes.relogio import Relogio
from sys import exit
from fases.fases import fase1
from classes.carrocinha import Carrocinha

def gameOver():
    print('Game Over!')
    reiniciar = input('Gostaria de jogar novamente (s/n)? ')
    if reiniciar == 's':
        relogio = Relogio()
        nome = input('Digite o nome do seu cãozinho: '). title()
        personagem = Personagem(nome)
        fase1(relogio, personagem)
    else:
        print('Obrigado por jogar!')
        exit()

class Personagem:                 
    def __init__(self, nome):
        self.__nome = nome
        self.__humor = 50
        self.__fome = 50
        self.__frio = 50
        self.__energia = 50
        self.__lugar = 'terreno baldio'

    def __str__(self):          #altera os atributos confome necessidade, sendo valores positivos ou negativos#
        return f'''

        Status {self.__nome}:
        ==============================
        |{("Humor - " + str(self.__humor) + "%").center(28)}|   
        |{("Fome - " + str(self.__fome) + "%").center(28)}|   
        |{("Frio - " + str(self.__frio) + "%").center(28)}|  
        |{("Energia - " + str(self.__energia) + "%").center(28)}|  
        ==============================   
        '''

    def muda_humor(self,humor_novo):
        self.__humor += humor_novo
        if self.__humor >= 100:
            self.__humor = 100
        elif self.__humor <= 0:
            print('Humor chegou a Zero.')
            gameOver()

    
    def muda_fome(self,fome_nova):
        self.__fome += fome_nova
        if self.__fome >= 100:
            self.__fome = 100
        elif self.__fome <= 0:
            print('Fome chegou a Zero.')
            gameOver()

    def muda_frio(self,frio_novo):
        self.__frio += frio_novo
        if self.__frio >= 100:
            self.__frio = 100
        elif self.__frio <= 0:
            print('Frio chegou a Zero.')
            gameOver()


    def muda_energia(self,nova_energia):
        self.__energia += nova_energia
        if self.__energia >= 100:
            self.__energia = 100
        elif self.__energia <= 0:
            print('Energia chegou a Zero.')
            gameOver()

    def muda_lugar(self,novo_lugar):
       self.__lugar = novo_lugar 

    @property
    def nome(self):
        return self.__nome

    @property
    def lugar(self):
        return self.__lugar

    def atualizacao_frio(self,relogio,frio = -5):
        if relogio.noite_fria():
            self.muda_frio (frio)
        else:
            self.muda_frio(frio * -1)