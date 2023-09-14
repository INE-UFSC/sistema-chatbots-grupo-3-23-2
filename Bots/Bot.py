##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

    @property
    def nome(self):
        return self.__nome 
    
    @property
    def comandos(self):
        return self.__comandos 
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def mostra_comandos(self):
        comandos = ""
        for i in range(len(self.__comandos)):
            comandos += f"{i} - {self.__comandos[i].descricao} \n"
        return comandos

    def executa_comando(self,cmd):
        return self.comandos[cmd].resposta

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass