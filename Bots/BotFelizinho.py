from Bots.Bot import Bot
from Bots.Comando import Comando

class BotFelizinho(Bot):
    def __init__(self,nome, urlJSON):
        super().__init__(nome, urlJSON)
        self.comandos = [Comando(0, "Bom dia", ["Bom dia, flor do dia!"]), Comando(1, "Mensagem motivacional", ["Acredite em si mesmo e em seu potencial ilimitado. Você é mais capaz do que imagina!"]),
                         Comando(2, "Elogios", ["Seu esforço e dedicação são realmente admiráveis. Continue assim!"]), Comando(3,"Despedida", [self.despedida()])]

    def apresentacao(self):
        return ("Olá! Eu sou o Risobótico e estou disposto a alegrar o seu dia!")
        
    def boas_vindas(self):
        return ("Que bom que você me escolheu! Vamos ter uma conversa muito agradável!") 

    def despedida(self):
        return ("É uma pena que você já vai embora :( , foi um prazer ter animado você!")