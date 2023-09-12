#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotGago import BotGago
from Bots.BotFelizinho import BotFelizinho
from Bots.BotFeliz import BotFeliz
from Bots.BotNaruto import BotNaruto
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotFelizinho("Lucian"), BotNaruto("Naruto"), BotTriste("Felipão"), BotGago("Gagui"), BotZangado("Dunga"), BotFeliz("José Aldo")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
