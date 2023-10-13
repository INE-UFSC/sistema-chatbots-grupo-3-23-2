from Bots.Bot import Bot
from Bots.BotFelizinho import BotFelizinho
from Bots.BotGago import BotGago
from Bots.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.JanelaComandos import JanelaComandos
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
                if values['bot_selecionado'] != '':
                    bot_escolhido = None
                    for bot in self.__bots:
                        if bot.nome == values['bot_selecionado']:
                            bot_escolhido = bot
                    self.__tela.fim()
                    self.janela_conversa(bot_escolhido)
                else:
                    resultado = "Nenhum campo selecionado"
            
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
            elif event == "Ver comandos":
                self.janela_comandos(bot)
            elif event == 'Enviar':
                if values["codigo"] == '':
                    resultado = "Você deve preencher todos os campos"
                else:
                    if self.__isnumber(values["codigo"]):

                        lista = []
                        for comando in bot.comandos:
                            lista.append(comando.id)
                        if not int(values["codigo"]) in lista:
                            resultado = "Código não reconhecido!"
                        else:
                            for comando in bot.comandos:
                                if int(values["codigo"]) == comando.id:
                                    resultado = comando.get_resposta_random()
                    else:
                        valor = 0
                        for comando in bot.comandos:
                            if values["codigo"].lower() == comando.mensagem.lower():
                                resultado = comando.get_resposta_random()
                                valor += 1
                        if valor == 0:
                            resultado = "Comando não identificado!"
            
            if resultado != '':
                dados = str(resultado)
                self.__tela.mostra_resultado(dados)

        self.__tela.fim()
    
    def janela_comandos(self, bot):
        tela_comandos = JanelaComandos(self, bot)
        tela_comandos.tela_comandos()

        # Loop de eventos
        rodando = True
        while rodando:
            event, values = tela_comandos.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False

        tela_comandos.fim()

    def __isnumber(self, value):
        try:
            int(value)
        except ValueError:
            return False
        return True

