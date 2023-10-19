from Model.Bot import Bot
from Model.BotFelizinho import BotFelizinho
from Model.BotGago import BotGago
from Model.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.JanelaComandos import JanelaComandos
from View.JanelaEditarComandos import JanelaEditarComandos
from View.JanelaAdicionarResposta import JanelaAdicionarResposta
from View.JanelaAdicionarComando import JanelaAdicionarComando
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
            elif event == 'Editar comandos':
                if values['bot_selecionado'] != '':
                    bot_escolhido = None
                    for bot in self.__bots:
                        if bot.nome == values['bot_selecionado']:
                            bot_escolhido = bot
                    self.__tela.fim()
                    self.janela_editar_comandos(bot_escolhido)
                else:
                    resultado = "Nenhum campo selecionado"
            elif event == 'Conversar':
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

    def janela_editar_comandos(self, bot):
        self.__tela = JanelaEditarComandos(self, bot)
        self.__tela.tela()

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
            elif event == 'Adicionar comando':
                self.__tela.fim()
                self.janela_adicionar_comando(bot)
            elif event == 'Adicionar resposta':
                if values['comando_selecionado'] != '':
                    comando_escolhido = None
                    for comando in bot.comandos:
                        if comando.mensagem == values['comando_selecionado']:
                            comando_escolhido = comando
                    self.__tela.fim()
                    self.janela_adicionar_respostas(comando_escolhido, bot)
                else:
                    resultado = 'Nenhum campo selecionado!'
            
            if resultado != '':
                dados = str(resultado)
                self.__tela.mostra_resultado(dados)

        self.__tela.fim()

    
    def janela_adicionar_respostas(self, comando, bot):
        self.__tela = JanelaAdicionarResposta(self,comando,  bot)
        self.__tela.tela()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == "Voltar":
                self.__tela.fim()
                self.janela_editar_comandos(bot)
            elif event == 'Adicionar':
                if values["resposta"] == '':
                    resultado = "Você deve preencher todos os campos"
                else:
                    bot.adicionar_resposta(comando.id, values["resposta"])
                    self.__tela.fim()
                    self.janela_editar_comandos(bot)
            
            if resultado != '':
                dados = str(resultado)
                self.__tela.mostra_resultado(dados)

        self.__tela.fim()
    
    def janela_adicionar_comando(self, bot):
        self.__tela = JanelaAdicionarComando(self, bot)
        self.__tela.tela()

        # Loop de eventos
        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__tela.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == "Voltar":
                self.__tela.fim()
                self.janela_editar_comandos(bot)
            elif event == 'Adicionar':
                if values["codigo"]=='' or values["mensagem"]== '':
                    resultado = "Você deve preencher todos os campos"
                elif not (self.__isnumber(values["codigo"])):
                    resultado = "Código deve ser um inteiro"
                else:
                    flag = True
                    for comando_bot in bot.comandos:
                        if comando_bot.id == int(values['codigo']) or comando_bot.mensagem == values['mensagem']:
                            flag = False
                    if not flag:
                        resultado = "Este comando já existe!"
                    else:
                        bot.adicionar_comando(values["codigo"], values["mensagem"])
                        self.__tela.fim()
                        self.janela_editar_comandos(bot)
            
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

