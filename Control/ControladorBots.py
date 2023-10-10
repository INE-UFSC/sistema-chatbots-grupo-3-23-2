from Bots.Bot import Bot
from Bots.BotFelizinho import BotFelizinho
from Bots.BotGago import BotGago
from Bots.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.MenuInicial import MenuInicial
import PySimpleGUI as sg 

class ControladorBots:
    def __init__(self, bots):
        self.__tela = None
        self.__bots = bots #lista de objetos bots

    def inicia(self):
        self.__tela = MenuInicial(self, self.__bots)
        self.__tela.tela_menu()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'OK':
                if values["codigo"] == '':
                    resultado = "Você deve preencher todos os campos"
                elif not self.__isnumber(values["codigo"]):
                    resultado = "O código deve ser um valor inteiro"
                elif int(values["codigo"]) < 0 or int(values["codigo"]) > len(self.__bots)-1:
                    resultado = "Digite o código de um bot!"
                else:
                    self.__tela.fim()
                    self.janela_conversa(self.__bots[int(values["codigo"])])
            
            if resultado != '':
                dados = str(resultado)
                self.__tela.mostra_resultado(dados)

        self.__tela.fim()
    
    def janela_conversa(self, bot):
        self.__tela = JanelaConversa(self, bot)
        self.__tela.tela_conversa()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == "Voltar":
                self.__tela.fim()
                self.inicia()
            elif event == 'OK':
                if values["codigo"] == '':
                    resultado = "Você deve preencher todos os campos"
                elif not self.__isnumber(values["codigo"]):
                    resultado = "O código deve ser um valor inteiro"
                else:
                    lista = []
                    for comando in bot.comandos:
                        lista.append(comando.id)
                    if not int(values["codigo"]) in lista:
                        resultado = "Digite o código de um comando"
                    else:
                        for comando in bot.comandos:
                            if int(values["codigo"]) == comando.id:
                                resultado = comando.get_resposta_random()
            
            if resultado != '':
                dados = str(resultado)
                self.__tela.mostra_resultado(dados)

        self.__tela.fim()

    def __isnumber(self, value):
        try:
            int(value)
        except ValueError:
            return False
        return True

