from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        
    def apresentacao(self):
        return f"Oi... Meu nome é {self.nome} 😭😭"

    def boas_vindas(self):
        return 'Certeza que você quer falar comigo? Sou inútil...'    
    
    def executa_comando(self,cmd):
        if cmd == "1":
            return "Dia ta lindo pra escutar Radiohead..."
        elif cmd=="2":
            return f"Ninguém lembra meu nome mesmo... É {self.nome} 😫"
        elif cmd=="3":
            return "Não nascer, é muito melhor..."
        elif cmd=="4" or cmd=="-1":
            return self.despedida()
        
    def despedida(self):
        self.sair = True
        return f"Você não quer falar mais comigo ...? 😭😭😭😭"
