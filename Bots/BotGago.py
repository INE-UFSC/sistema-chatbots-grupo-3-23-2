from Bots.Bot import Bot
from Bots.Comando import Comando

class BotGago(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.comandos = [Comando("Bom dia", "Bo-bo-bom dia!"), Comando("Preciso de um conselho", "Se um estra-tra-tra-tranho o-ofe-fe-ferecer drogas, a-a-aceite. Drogas são caras!"),
                        Comando("Previsão do tempo", "Vai cho-chover ca-ca-canivetes"), Comando("Adeus", self.despedida())]

    def apresentacao(self):
        return 'O-o-olá, me-meu nome-me-me-me-me é Gaguinho, espe-pe-pe-ro po-de-der aju-ju-ju-ju-ju-ju-dar!'
        
    def boas_vindas(self):
        return 'Obriga-do-do-do-do-do por me es-co-co-co-lher!'

    def despedida(self):
        return 'Po-po-por hoje-je é só, pe-pe-pe-pessoal!'
