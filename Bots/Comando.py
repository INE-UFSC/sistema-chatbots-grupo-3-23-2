
class Comando():

    def __init__(self, descricao: str, resposta: str):
        self.__descricao = descricao
        self.__resposta = resposta

    @property
    def descricao(self):
        return self.__descricao 
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @property
    def resposta(self):
        return self.__resposta 
    
    @resposta.setter
    def resposta(self, resposta):
        self.__resposta = resposta
