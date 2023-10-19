import random


class Comando():

    def __init__(self, id: int, mensagem: str, respostas=[]):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas
        
    @property
    def mensagem(self):
        return self.__mensagem 
    
    @mensagem.setter
    def mensagem(self, mensagem):
        self.__mensagem = mensagem
    
    @property
    def respostas(self):
        return self.__respostas 
    
    @respostas.setter
    def respostas(self, respostas):
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self, id):
        self.__id = id  

    def get_resposta_random(self):
        try:
            numero_aleatorio = random.randint(0, len(self.__respostas)-1)
            return self.__respostas[numero_aleatorio]
        except:
            return "Sem resposta para o comando :("
    
    def addResposta(self, resposta):
        self.__respostas.append(resposta)
    

