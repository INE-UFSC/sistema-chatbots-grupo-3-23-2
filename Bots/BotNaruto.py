from Bots.Bot import Bot
from Bots.Comando import Comando

class BotNaruto(Bot):
    def __init__(self, nome, urlJSON):
        super().__init__(nome, urlJSON)
        """self.comandos = [Comando(0, "Rasengan", ["AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA RASENGAAAAAAAAAANNNN!"]), Comando(1, "Motivacional", ["O Naruto pode ser um pouco duro às vezes, talvez você não saiba disso, mas o Naruto também cresceu sem pai. Na verdade ele nunca conheceu nenhum de seus pais, e nunca teve nenhum amigo em nossa aldeia."]),
                         Comando(2, "Comida preferida", ["Minha comida preferida é o Ichiraku Ramen. Não tem nada melhor do que um prato quente de ramen depois de um dia de treinamento ou uma batalha intensa."]), Comando(3, "Adeus", [self.despedida()])]
"""
    def apresentacao(self):
        return 'Eu sou Naruto Uzumaki, o ninja número um da Vila da Folha, e o meu sonho é me tornar o Hokage, é isso aí dattebayo!'
    
    def boas_vindas(self):
        return 'Seja bem-vindo! Estou animado para ter você aqui comigo. Vamos juntos em busca dos nossos sonhos e se tornar hokages!'
    
    def despedida(self):
        return 'Até a próxima, pessoal! Nunca desistam dos seus sonhos no mundo ninja, DATTEBAYO!'
