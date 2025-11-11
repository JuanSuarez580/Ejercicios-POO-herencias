class Transporte:
    def __init__(self, modelo, color, motor):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.encendido = False
        self.velocidad = 0
    
    def mostrar_info(self):
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Motor:", self.motor)
        print("Velocidad actual:", self.velocidad, "km/h")
        if self.encendido:
            print("Estado: Encendido")
        else:
            print("Estado: Apagado")


class Vehiculo(Transporte):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor)
        self.puertas = puertas
        self.pasajeros = pasajeros
        self.combustible = combustible
    
    def arrancar(self):
        if self.encendido == False:
            self.encendido = True
            print("Vehiculo arrancado")
        else:
            print("Ya esta encendido")
    
    def apagar(self):
        if self.encendido == True:
            self.encendido = False
            self.velocidad = 0
            print("Vehiculo apagado")
        else:
            print("Ya esta apagado")
    
    def acelerar(self, cantidad):
        if self.encendido == True:
            self.velocidad = self.velocidad + cantidad
            print("Acelerando... Velocidad:", self.velocidad, "km/h")
        else:
            print("Error: Primero arranca el vehiculo")
    
    def frenar(self, cantidad):
        if self.velocidad > 0:
            self.velocidad = self.velocidad - cantidad
            if self.velocidad < 0:
                self.velocidad = 0
            print("Frenando... Velocidad:", self.velocidad, "km/h")
        else:
            print("El vehiculo ya esta detenido")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Numero de puertas:", self.puertas)
        print("Capacidad de pasajeros:", self.pasajeros)
        print("Tipo de combustible:", self.combustible)
