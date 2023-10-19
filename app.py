#encoding: utf-8
from Model.BotGago import BotGago
from Model.BotFelizinho import BotFelizinho
from Model.BotNaruto import BotNaruto
from View.JanelaConversa import JanelaConversa
from View.MenuInicial import MenuInicial
from Control.ControladorBots import ControladorBots


control = ControladorBots([BotFelizinho("Lucian", "lucian.pkl"), BotNaruto("Naruto", "naruto.pkl"), BotGago("Elio", "elio.pkl")])

control.inicia()