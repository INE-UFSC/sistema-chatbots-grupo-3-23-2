#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotGago import BotGago
from Bots.BotFeliz import BotFeliz
from Bots.BotNaruto import BotNaruto

###construa a lista de bots disponíveis aqui
lista_bots = [BotFeliz("Lucian"), BotGago("Elio"), BotNaruto("Naruto")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
