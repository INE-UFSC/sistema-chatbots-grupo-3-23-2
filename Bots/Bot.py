##implemente as seguintes classes
from Bots.Comando import Comando
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, urlJSON):
        self.__urlJSON = urlJSON
        self.__nome = nome
        self.__comandos = []

    @property
    def nome(self):
        return self.__nome 
    
    @property
    def comandos(self):
        return self.__comandos

    @property
    def urlJSON(self):
        return self.__urlJSON 
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos
    
    @urlJSON.setter
    def urlJSON(self, urlJSON):
        self.__urlJSON = urlJSON

    def mostra_comandos(self):
        comandos = ""
        for i in range(len(self.__comandos)):
            comandos += f"{i} - {self.__comandos[i].mensagem} \n"
        return comandos

    def executa_comando(self,cmd):
        return self.comandos[cmd].get_resposta_random()
    
    def adicionar_resposta(self, id, texto):
        for comando in self.__comandos:
            if comando.id == id:
                comando.addResposta(texto)
    
    def adicionar_comando(self, id, mensagem):
        self.__comandos.append(Comando(id, mensagem, []))

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass