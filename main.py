from interface import Interface
from estacionamento import Estacionamento
from carro import Carro

i = Interface()
c = Carro()

i._estac.inicBD()
c.inicBD()

i.menu_principal()