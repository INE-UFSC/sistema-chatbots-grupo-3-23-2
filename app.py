#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotGago import BotGago
from Bots.BotFelizinho import BotFelizinho
from Bots.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.MenuInicial import MenuInicial
from Control.ControladorBots import ControladorBots


control = ControladorBots([BotFelizinho("Lucian", "lucian.pkl"), BotNaruto("Naruto", "naruto.pkl"), BotGago("Elio", "elio.pkl")])

control.inicia()

