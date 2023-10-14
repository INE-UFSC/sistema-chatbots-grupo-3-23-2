import PySimpleGUI as sg 
from Bots.Bot import Bot


class JanelaAdicionarComando():
    def __init__(self, controlador, bot):
        self.__bot = bot
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Adicionar comandos", self.__container, font=("Helvetica", 16))

    def tela(self):
        self.__container = [
         [sg.Text(f'Adicionar comando ao bot {self.__bot.nome}:')],
         [sg.Text('Código: '), sg.InputText(key='codigo')], 
         [sg.Text('Mensagem: '), sg.InputText(key='mensagem')], 
         [sg.Button("Adicionar"), sg.Button("Voltar")],
         [sg.Text(key='resultado')]
        ]

        self.__window = sg.Window("Adicionar comandos", self.__container ,font=("Helvetica", 16))

    def le_eventos(self):
        return self.__window.read()

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').update(resultado)

    def fim(self):
        self.__window.close()
