import PySimpleGUI as sg 
from Model.Bot import Bot


class JanelaAdicionarResposta():
    def __init__(self, controlador, comando, bot):
        self.__bot = bot
        self.__comando = comando
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Adicionar respostas", self.__container, font=("Helvetica", 16))

    def tela(self):
        self.__container = [
         [sg.Text(f'Comando {self.__comando.mensagem}:')],
         [sg.Text(f'Digite a resposta do comando:')],
         [sg.Multiline('', size=(30, 16), key='resposta', autoscroll=True)],
         [sg.Button("Adicionar"), sg.Button("Voltar")],
         [sg.Text(key='resultado')]
        ]

        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def le_eventos(self):
        return self.__window.read()

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').update(resultado)

    def fim(self):
        self.__window.close()
