#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotGago import BotGago
from Bots.BotFelizinho import BotFelizinho
from Bots.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.MenuInicial import MenuInicial
from Control.ControladorBots import ControladorBots


control = ControladorBots([BotFelizinho("Lucian", "a"), BotNaruto("Naruto", "a"), BotGago("Elio", "a")])

control.inicia()



















"""
bota = [BotGago("Ei", "aaa"), BotGago("NA", "aaa")]
j1 = MenuInicial("A", bota)
a = j1.tela_menu()

# Loop principal de eventos
while True:
    event, values = j1.le_eventos()
    if event == 'OK':
        break

# Feche a janela
j1.fim()


###construa a lista de bots disponíveis aqui
lista_bots = [BotFelizinho("Lucian"), BotNaruto("Naruto"), BotGago("Elio")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
"""