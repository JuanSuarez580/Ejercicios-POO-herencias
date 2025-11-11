from Modelo_vehiculo import Vehiculo

class Camioneta(Vehiculo):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible, marca):
        super().__init__(modelo, color, motor, puertas, pasajeros, combustible)
        self.marca = marca
        self.tipo = "Camioneta"
        self.traccion = "4x4"
        self.carga_maxima = 800
    
    def sistema_direccion(self, direccion):
        if self.encendido == True:
            print("Camioneta girando hacia la", direccion)
            print("Sistema de direccion asistida activo")
        else:
            print("Error: La camioneta esta apagada")
    
    def climatizacion(self, accion):
        if self.encendido == True:
            if accion == "encender":
                print("Sistema de climatizacion encendido")
                print("Temperatura regulada para todos los pasajeros")
            elif accion == "apagar":
                print("Climatizacion apagada")
        else:
            print("Error: Arranca la camioneta primero")
    
    def tipo_seguridad(self):
        print("Sistemas de seguridad:")
        print("- Airbags frontales y laterales")
        print("- Control de estabilidad")
        print("- Frenos ABS")
        print("- Barras de proteccion")
    
    def sistema_ventanas(self, ventana, accion):
        print("Ventana", ventana, "electricas", accion)
    
    def sistema_espejo(self, accion):
        print("Espejos electricos", accion)
    
    def cargar(self, peso):
        if peso <= self.carga_maxima:
            print("Cargando", peso, "kg en la camioneta")
        else:
            print("Error: Peso maximo es", self.carga_maxima, "kg")
    
    def modo_traccion(self, modo):
        if modo == "4x4":
            print("Modo 4x4 activado - Para todo terreno")
        elif modo == "4x2":
            print("Modo 4x2 activado - Para ciudad")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Marca:", self.marca)
        print("Tipo:", self.tipo)
        print("Traccion:", self.traccion)
        print("Carga maxima:", self.carga_maxima, "kg")
