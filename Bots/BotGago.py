from Bots.Bot import Bot
from Bots.Comando import Comando

class BotGago(Bot):
    def __init__(self, nome, urlJSON):
        super().__init__(nome, urlJSON)
        self.comandos = [Comando(0, "Bom dia", ["Bo-bo-bom dia!"]), Comando(1, "Preciso de um conselho", ["Se um estra-tra-tra-tranho o-ofe-fe-ferecer drogas, a-a-aceite. Drogas são caras!"]),
                        Comando(2, "Previsão do tempo", ["Vai cho-chover ca-ca-canivetes"]), Comando(3, "Adeus", [self.despedida()])]

    def apresentacao(self):
        return 'O-o-olá, me-meu nome-me-me-me-me é Gaguinho, espe-pe-pe-ro po-de-der aju-ju-ju-ju-ju-ju-dar!'
        
    def boas_vindas(self):
        return 'Obriga-do-do-do-do-do por me es-co-co-co-lher!'

    def despedida(self):
        return 'Po-po-por hoje-je é só, pe-pe-pe-pessoal!'
