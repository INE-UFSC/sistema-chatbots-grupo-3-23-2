import PySimpleGUI as sg 
from Model.Bot import Bot


# View do padrão MVC
class JanelaConversa():
    def __init__(self, controlador, bot):
        self.__bot = bot
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def tela_conversa(self):

        self.__container = [
         [sg.Button('Ver comandos'), sg.Button('Voltar')],
         [sg.Text('Digite o código ou a descrição do comando e clique em enviar:')],
         [sg.InputText(key='codigo'), sg.Button('Enviar')], 
         [sg.Multiline('', size=(50, 10), disabled=True, key='resultado', autoscroll=True)]
        ]

        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
