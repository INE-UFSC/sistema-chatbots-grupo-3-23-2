import PySimpleGUI as sg 
from Model.Bot import Bot


class JanelaComandos():
    def __init__(self, controlador, bot):
        self.__bot = bot
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Janela de comandos", self.__container, font=("Helvetica", 16))

    def tela_comandos(self):
        self.__container = [
         [sg.Text(f'Código e palavras-chave dos comandos do bot {self.__bot.nome} :')],
        ]

        texto = ''
        for comando in self.__bot.comandos:
            texto += f"Código: {comando.id} - {comando.mensagem} \n"
        
        self.__container.append([sg.Column([[sg.Multiline(texto, size=(30, 16), disabled=True, key='scrollable_text', autoscroll=True)],], scrollable=True)])
        #self.__container.append([sg.Text(f"Código: {comando.id} - {comando.mensagem}")])

        self.__window = sg.Window("Janela de conversa", self.__container ,font=("Helvetica", 16))

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
