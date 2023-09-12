from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots= []
        for bot in lista_bots:
            if isinstance(bot, Bot):
                self.__lista_bots.append(bot)
        self.__bot = None
    
    def boas_vindas(self):
        print(f"Olá, esse é o Sistema de chatbots da empresa {self.__empresa}")

    def mostra_menu(self):
        print("Os chat bots disponíveis no momento são: ")
        for i in range(len(self.__lista_bots)):
            print(f"{i} - Bot: {self.__lista_bots[i].nome} - Mensagem de apresentação: {self.__lista_bots[i].apresentacao()}")
        ##mostra o menu de escolha de bots
    
    def escolhe_bot(self):
        num_escolhido = int(input("Digite o número do chat bot desejado: "))
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        self.__bot = self.__lista_bots[num_escolhido]
        print(f"--> {self.__bot.nome} diz: {self.__bot.boas_vindas()}")


    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        while True:
            self.mostra_comandos_bot()
            comando = int(input("Digite o comando desejado (ou -1 para fechar): "))
            if comando == -1:
                self.__bot.despedida()
                break
            else:
                print(self.__bot.executa_comando(comando))



        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.le_envia_comando()
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
