#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotGago import BotGago
from Bots.BotFelizinho import BotFelizinho
from Bots.BotNaruto import BotNaruto

###construa a lista de bots disponíveis aqui
lista_bots = [BotFelizinho("Lucian"), BotNaruto("Naruto"), BotGago("Elio")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
