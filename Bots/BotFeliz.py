from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self.comandos = {"1" : 'Bom dia, flor do dia!', "2": 'Acredite em si mesmo e em seu potencial ilimitado. Você é mais capaz do que imagina!', "3": 'Seu esforço e dedicação são realmente admiráveis. Continue assim!', "4": self.despedida() }

    def apresentacao(self):
        return ("Olá! Eu sou o Risobótico e estou disposto a alegrar o seu dia!")

    def mostra_comandos(self):
        return("1 - Bom dia\n2 - Mensagem motivacional\n3 - Elogios\n4 - Despedida")



    
    def executa_comando(self,cmd):
        return self.comandos[cmd]
        



    def boas_vindas(self):
    
        return ("Que bom que você me escolheu! Vamos ter uma conversa muito agradável!") 



    def despedida(self):
        return ("É uma pena que você já vai embora :( , foi um prazer ter animado você!")