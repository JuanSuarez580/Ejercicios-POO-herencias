from Modelo_vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, marca):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.marca = marca
        self.tipo = "Camion de Carga"
        self.carga_maxima = 5000
        self.carga_actual = 0
    
    def sistema_direccion(self, direccion):
        if self.encendido == True:
            print("Camion girando hacia la", direccion)
            print("Sistema de direccion hidraulica activa")
        else:
            print("Error: El camion esta apagado")
    
    def climatizacion(self, accion):
        if self.encendido == True:
            if accion == "encender":
                print("Climatizacion del camion encendida")
            elif accion == "apagar":
                print("Climatizacion apagada")
        else:
            print("Error: Arranca el camion primero")
    
    def tipo_seguridad(self):
        print("Sistemas de seguridad del camion:")
        print("- Frenos de aire")
        print("- Sistema ABS")
        print("- Luces de emergencia")
        print("- Espejos laterales grandes")
        print("- Cinturones de seguridad")
    
    def sistema_ventanas(self, ventana, accion):
        print("Ventana", ventana, "del camion", accion)
    
    def sistema_espejo(self, accion):
        print("Espejos laterales grandes", accion)
    
    def cargar(self, peso):
        if self.carga_actual + peso <= self.carga_maxima:
            self.carga_actual = self.carga_actual + peso
            print("Cargando", peso, "kg")
            print("Carga actual:", self.carga_actual, "kg")
        else:
            print("Error: Peso maximo es", self.carga_maxima, "kg")
            print("Ya tienes", self.carga_actual, "kg cargados")
    
    def descargar(self, peso):
        if self.carga_actual >= peso:
            self.carga_actual = self.carga_actual - peso
            print("Descargando", peso, "kg")
            print("Carga restante:", self.carga_actual, "kg")
        else:
            print("Error: Solo tienes", self.carga_actual, "kg cargados")
    
    def verificar_carga(self):
        porcentaje = (self.carga_actual * 100) / self.carga_maxima
        print("Carga actual:", self.carga_actual, "kg")
        print("Capacidad maxima:", self.carga_maxima, "kg")
        print("Porcentaje de carga:", porcentaje, "%")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Marca:", self.marca)
        print("Tipo:", self.tipo)
        print("Carga maxima:", self.carga_maxima, "kg")
        print("Carga actual:", self.carga_actual, "kg")
