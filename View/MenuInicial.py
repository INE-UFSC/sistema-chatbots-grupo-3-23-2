import PySimpleGUI as sg 
from Bots.Bot import Bot
# View do padrão MVC
class MenuInicial():
    def __init__(self, controlador, bots=[]):
        self.__bots = bots
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Escolha de bots", self.__container ,font=("Helvetica", 16))

    def tela_menu(self):

        self.__container = [
         [sg.Text('Escolha uma das opções de bots que estão disponíveis para interação')]
        ]

        for i, bot in enumerate(self.__bots):
            self.__container.append([sg.Text(f"{i} - {bot.nome}")])
            
        self.__container.append([sg.InputText(key='codigo')])
        self.__container.append([sg.Button('OK')])
        self.__container.append([sg.Text(key='resultado')])
        self.__window = sg.Window("Escolha de bots", self.__container ,font=("Helvetica", 16))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
