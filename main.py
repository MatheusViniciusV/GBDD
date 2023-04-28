import sys
sys.path.insert(1, './src')
from GUIInicio import *
from BancoDeDados import *

bancodedados = BancoDeDados()
inicio = GUIInicio(bancodedados)
inicio.rodar()
