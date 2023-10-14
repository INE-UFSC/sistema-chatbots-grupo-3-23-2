##implemente as seguintes classes
from Bots.Comando import Comando
from Bots.ComandoDAO import ComandoDAO
from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, urlJSON):
        self.__urlJSON = urlJSON
        self.__nome = nome
        self.__comandos = ComandoDAO(urlJSON)

    @property
    def nome(self):
        return self.__nome 
    
    @property
    def comandos(self):
        return list(self.__comandos.get_all())

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
        comandos = self.__comandos.get_all()
        comandosString = ''
        for i in range(len(comandos)):
            comandosString += f"{i} - {comandos[i].mensagem} \n"
        return comandosString
    
    def adicionar_resposta(self, id, texto):
        comando = self.__comandos.get(id)
        comando.addResposta(texto)
        self.__comandos.remove(id)
        self.__comandos.add(id, comando)
    
    def adicionar_comando(self, id, mensagem):
        self.__comandos.add(id, Comando(id, mensagem, []))

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass