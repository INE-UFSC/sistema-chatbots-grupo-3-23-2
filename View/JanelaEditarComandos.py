import PySimpleGUI as sg 
from Model.Bot import Bot


# View do padrão MVC
class JanelaEditarComandos():
    def __init__(self, controlador, bot):
        self.__bot = bot
        self.__controlador = controlador
        self.__container = []
        self.__window = sg.Window("Editar comandos", self.__container ,font=("Helvetica", 16))

    def tela(self):

        comandos = []
        for comando in self.__bot.comandos:
            comandos.append(comando.mensagem)
            
        if len(comandos)==0:
            comandos.append("")
        default_bot_index = 0  # Defina o índice do primeiro bot como padrão (0 neste caso)

        self.__container = [
            [sg.Text(f'Escolha um dos comandos disponíveis do bot {self.__bot.nome}')],
            [sg.Text('Selecione um comando:')],
            [sg.Combo(comandos, default_value=comandos[default_bot_index], key='comando_selecionado', readonly=True)],
            [sg.Button('Adicionar resposta'), sg.Button('Adicionar comando'), sg.Button('Voltar')],
            [sg.Text(key='resultado')]
        ]

        self.__window = sg.Window("Editar Comandos", self.__container ,font=("Helvetica", 16))

    def mostra_resultado(self, resultado): 
        self.__window.Element('resultado').update(resultado)

    def le_eventos(self):
        return self.__window.read()

    def fim(self):
        self.__window.close()
