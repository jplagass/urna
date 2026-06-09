from estacionamento import Estacionamento


class Interface():
    def __init__(self):
        self._estac = Estacionamento()
        pass
    
    
    def _menu_mostrar_vagas(self):
        while True:
            self._estac.estacionamento_board()
            o = int(input("""escolha uma vaga para especionar ou aperte 0 para voltar pro menu: """))
            
            match o:
                case n if 1 <= n <= 6:
                    self._estac.take_placa(o)
                case 0:
                    break
                case _:
                    print("Vaga invalida")
        
    def _menu_estacionar_carro(self):
        self._estac.estacionamento_board()

        o = int(input("Escolha uma vaga para estacionar: "))
        
        match o:
            case n if 1 <= n <= 6:
                self._estac.add_vaga(o)
            case _:
                print("Vaga invalida")
        
        
    
    def _menu_sair_carro(self):
        self._estac.estacionamento_board()

        o = int(input("Escolha uma carro para sair com a vaga: "))
        
        match o:
            case n if 1 <= n <= 6:
                self._estac.del_vaga(o)
            case _:
                print("Vaga invalida")
    
    
    
    
    
    def menu_principal(self):
        while True:
            print("""
***MENU***
 1-MOSTRA VAGAS
 2-ESTACIONAR CARRO
 3-SAIR CARRO""")
            o = int(input("Escolha uma opcao: "))
            
            match o:
                case 1:
                    self._menu_mostrar_vagas()
                case 2:
                    self._menu_estacionar_carro()
                case 3:
                    self._menu_sair_carro()
                case _:
                    print("opção invalida")