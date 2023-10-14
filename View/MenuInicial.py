import PySimpleGUI as sg 
from Bots.Bot import Bot

class MenuInicial():
    def __init__(self, controlador, bots=[]):
        self.__bots = bots
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Escolha de bots", self.__container, font=("Helvetica", 16))

    def tela_menu(self):
        bot_nomes = []
        for bot in self.__bots:
            if not bot.nome in bot_nomes:
                bot_nomes.append(bot.nome)
            else:
                print(f"Já existe um bot com o nome {bot.nome}")
        if len(bot_nomes)==0:
            bot_nomes.append("")
        default_bot_index = 0  # Defina o índice do primeiro bot como padrão (0 neste caso)

        self.__container = [
            [sg.Text('Escolha um dos bots disponíveis para interação')],
            [sg.Text('Selecione um bot:')],
            [sg.Combo(bot_nomes, default_value=bot_nomes[default_bot_index], key='bot_selecionado', readonly=True)],
            [sg.Button('Conversar'), sg.Button('Editar comandos')],
            [sg.Text(key='resultado')]
        ]

        self.__window = sg.Window("Escolha de bots", self.__container, font=("Helvetica", 16))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').Update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
