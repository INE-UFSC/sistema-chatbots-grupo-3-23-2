from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        
    def apresentacao(self):
        return f'Grrrrrr. Meu nome é {self.nome} e eu te odeio!'

    def boas_vindas(self):
        return 'Eu não posso acreditar que você me escolheu, GRRRRRR!'    
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return "Bom dia? Só se for pra você! Péssimo dia pra mim!"
        elif cmd=="2":
            return f"É sério que você quer que eu repita? É {self.nome}!!!"
        elif cmd=="3":
            return "Não tenho filho desse tamanho."
        elif cmd=="4" or cmd=="-1":
            return self.despedida()
        
    def despedida(self):
        return f"FINALMENTE, é o dia mais feliz da minha vida. ADEUS!"
