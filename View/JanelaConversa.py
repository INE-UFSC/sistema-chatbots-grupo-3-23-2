import PySimpleGUI as sg 
from Bots.Bot import Bot
from Bots.BotGago import BotGago


# View do padrão MVC
class JanelaConversa():
    def __init__(self, controlador, bot):
        self.__bot = bot
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def tela_conversa(self):

        self.__container = [
         [sg.Text('Digite o código da ação desejada e clique em OK:')],
        ]
        
        for comando in self.__bot.comandos:
            self.__container.append([sg.Text(f"Código: {comando.id} - {comando.mensagem}")])

        self.__container.append([sg.InputText(key='codigo')])
        self.__container.append([sg.Button('OK'), sg.Button('Voltar')])
        self.__container.append([sg.Text(key='resultado')])

        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
