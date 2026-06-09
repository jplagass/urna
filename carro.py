import sqlite3 as sql
import os

class Carro():
    def __init__(self):
        self._path = (r"C:\PYTHON PROJETO\ESTACIONAMENTO\estac.bd")
        self._placa = ""
        self._modelo = ""
        
    @property
    def placa(self):
        return self._placa
    @property
    def modelo(self):
        return self._modelo
    
    @placa.setter
    def placa (self,x):
        self._placa = x
    @modelo.setter
    def modelo (self,x):
        self._modelo = x
        
    
    def inicBD(self):
        
        conn = None
        conn = sql.connect(self._path)
        cursor = conn.cursor()
            
        cursor.execute('CREATE TABLE IF NOT EXISTS "CARROS" ("placa" TEXT NOT NULL,"modelo" TEXT,PRIMARY KEY("placa"));')
            
                   
        conn.commit()
        conn.close()
        
    def add_car(self):
        i = False
        conn = sql.connect(self._path)
        cursor = conn.cursor()  
        placa = input("Adcione o numero da placa do seu carro aqui: ")
        
        cursor.execute("SELECT * FROM CARROS")
        qtd = cursor.fetchall()
        
        for a, _ in qtd:
            if a == placa:
                i = True
                print("este carro ja esta na nossa lista")
                pass
            
        
        if i == False:    
            modelo = input("Adcione o modelo do seu carro aqui: ")
            cursor.execute('INSERT INTO CARROS (placa, modelo) VALUES (?, ?)', (placa, modelo,))
        conn.commit()
        conn.close()
        
        return placa
    
    
    def select_car (self, x):
        conn = sql.connect(self._path)
        cursor = conn.cursor()  
        cursor.execute("SELECT * FROM CARROS")
        lista = cursor.fetchall()
        conn.commit()
        conn.close()
        
        for a, b in lista:
            if a == x:
                return b
            
    def inspect_car(self, v, p):
        conn = sql.connect(self._path)
        cursor = conn.cursor()  
        cursor.execute("SELECT * FROM CARROS")
        lista_car = cursor.fetchall()
        conn.commit()
        conn.close()
        
        for a, b in lista_car:
            if a == p:
                placa = a
                modelo = b
                vaga = v
        
        print(f"""
****INSPECIONAR CARRO****

MODELO:{modelo}

PLACA:{placa}

VAGA OCUPADA: {vaga}°

************************""")