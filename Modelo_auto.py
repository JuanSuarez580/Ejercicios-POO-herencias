from Modelo_vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, marca):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.marca = marca
        self.tipo = "Automovil"
        self.luces = False
        self.aire = False
    
    def sistema_direccion(self, direccion):
        if self.encendido == True:
            print("Girando hacia la", direccion)
        else:
            print("Error: El auto esta apagado")
    
    def climatizacion(self, accion):
        if self.encendido == True:
            if accion == "encender":
                self.aire = True
                print("Aire acondicionado encendido")
            elif accion == "apagar":
                self.aire = False
                print("Aire acondicionado apagado")
        else:
            print("Error: Arranca el auto primero")
    
    def luces_auto(self, accion):
        if accion == "encender":
            self.luces = True
            print("Luces encendidas")
        elif accion == "apagar":
            self.luces = False
            print("Luces apagadas")
    
    def sistema_ventanas(self, ventana, accion):
        print("Ventana", ventana, accion)
    
    def sistema_espejo(self, accion):
        print("Espejos", accion)
    
    def tipo_seguridad(self):
        print("Cuenta con:")
        print("- Airbags")
        print("- Frenos ABS")
        print("- Cinturones de seguridad")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Marca:", self.marca)
        print("Tipo:", self.tipo)
        print("Luces:", "Encendidas" if self.luces else "Apagadas")
        print("Aire acondicionado:", "Encendido" if self.aire else "Apagado")
