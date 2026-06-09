import os
import random
import sqlite3 as sql
from carro import Carro
class Estacionamento():
    def __init__(self):
        self.car_emogi = ["🚗  ","🚙  ", "🏎️   ", "🚓  " ]
        self.c = Carro()
        self._vagas = []
        base_path = os.path.dirname(os.path.abspath(__file__))
        self._path = os.path.join(base_path, "estac.bd")
    
    @property
    def vagas(self):
        return self._vagas
    @vagas.setter
    def vagas(self,vagas):
        self._vagas = vagas
    
    
    
    def inicBD(self):
        
        conn = None
        
        conn = sql.connect(self._path)
        cursor = conn.cursor()
            
        cursor.execute('CREATE TABLE IF NOT EXISTS "ESTACIONAMENTO" ("vaga" INTEGER NOT NULL,"placa" TEXT,PRIMARY KEY("vaga" AUTOINCREMENT));')
        
        cursor.execute("SELECT * FROM ESTACIONAMENTO")
        qtd = cursor.fetchone()
        
        if qtd == None:
            for _ in range(6):
                cursor.execute('INSERT INTO ESTACIONAMENTO(placa) VALUES(NULL)')
               
        
        cursor.execute('SELECT * FROM ESTACIONAMENTO')
        self.vagas = cursor.fetchall()
          
        conn.commit()
        conn.close()
        
        
    def updBD (self):
        conn = None
        conn = sql.connect(self._path)
        cursor = conn.cursor()
        
        for a , b in self.vagas:
            cursor.execute('UPDATE ESTACIONAMENTO SET placa = ? WHERE vaga = ?', (b, a))
        
        conn.commit()
        conn.close()
        
    def estacionamento_board(self):
        lista_vagas=[""] * 6
        a = "    "
        
        for x in range(6):
            if self._vagas[x][1] == None:
               lista_vagas[x] = a
            else:
                lista_vagas[x] = random.choice(self.car_emogi)
                
                
            
       
        print(F"""      
                          ____________________
                        /|                   /|
                       / |                  / |
                      /  |                 /  |
             ________|   |_________________|  |____________
                     |   /     /     /     |  /  
                     |  / {lista_vagas[0]}/ {lista_vagas[1]}/ {lista_vagas[2]}/| / 
                     | /  1  /  2  /  3  / |/
             *********                     *********     
              
              
             *********                     *********
                     * |  4  |  5  |  6  | *
                     * | {lista_vagas[3]}| {lista_vagas[4]}| {lista_vagas[5]}| *
                     * |     |     |     | * 
                     ***********************""")
    def exist_car(self, x):
        for _ , b in self._vagas:
            if x == b:
                return False
        
        return True
            
        
        
    def add_vaga(self,vaga):
        placa = self.c.add_car()
        x = self.exist_car(placa)
        lista_vagas = []
        
        for a , b in self._vagas:
            if x == True:
                if a == vaga:
                    if b == None: 
                        lista_vagas.append((a, placa))
                    else:
                        print("Essa vaga ja foi ocupada")
                        
                else:
                    lista_vagas.append((a, b))
            else:
                print("esse carro ja esta em uma vaga")
                break
                
        self.vagas = lista_vagas
        
        self.updBD()    
    
    
        
    def del_vaga(self,vaga):
        lista_vagas = []
        for a , b in self._vagas:
            if a == vaga:
                if b != None: 
                    car = self.c.select_car(b)       
                    print(f" o {car} de placa {b} saiu da vaga")
                    lista_vagas.append((a, None))
                else:
                   print("Essa vaga ja esta vazia")
                    
            else:
                lista_vagas.append((a, b))
                
        self.vagas = lista_vagas
        
        self.updBD()
        
    def take_placa(self,v):
        
        for i in range(6):
            if self._vagas[i][0] == v:
                p = self._vagas[i][1]
                
        if p == None:
            print("essa vaga esta vazia")
        else:
            self.c.inspect_car(v, p)
        
          
    