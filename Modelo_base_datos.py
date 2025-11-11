from Modelo_vehiculo import Vehiculo
from Modelo_auto import Auto
from Modelo_camioneta import Camioneta
from Modelo_camion import Camion

class BaseDatosVehiculos:
    def __init__(self):
        self.lista_vehiculos = []
        self.numero_id = 1
    
    def agregar(self, vehiculo):
        vehiculo.id = self.numero_id
        self.lista_vehiculos.append(vehiculo)
        self.numero_id = self.numero_id + 1
        print("Vehiculo agregado con ID:", vehiculo.id)
    
    def buscar(self, id):
        for vehiculo in self.lista_vehiculos:
            if vehiculo.id == id:
                return vehiculo
        return None
    
    def contar_encendidos(self):
        contador = 0
        for vehiculo in self.lista_vehiculos:
            if vehiculo.encendido == True:
                contador = contador + 1
        return contador
    
    def contar_en_movimiento(self):
        contador = 0
        for vehiculo in self.lista_vehiculos:
            if vehiculo.velocidad > 0:
                contador = contador + 1
        return contador
    
    def listar(self):
        print("\n=== Lista de Vehiculos ===")
        for vehiculo in self.lista_vehiculos:
            print("\nID:", vehiculo.id)
            print("Modelo:", vehiculo.modelo)
            print("Color:", vehiculo.color)
            print("Motor:", vehiculo.motor)
            print("Velocidad:", vehiculo.velocidad, "km/h")
            if hasattr(vehiculo, 'marca'):
                print("Marca:", vehiculo.marca)
            if hasattr(vehiculo, 'tipo'):
                print("Tipo:", vehiculo.tipo)
    
    def estadisticas(self):
        total = len(self.lista_vehiculos)
        encendidos = self.contar_encendidos()
        en_movimiento = self.contar_en_movimiento()
        
        print("\n=== Estadisticas ===")
        print("Total de vehiculos:", total)
        print("Vehiculos encendidos:", encendidos)
        print("Vehiculos en movimiento:", en_movimiento)
        print("Vehiculos detenidos:", total - en_movimiento)
