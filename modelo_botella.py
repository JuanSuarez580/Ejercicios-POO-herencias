class Contenedor:
    def __init__(self, material, capacidad, forma, diseno):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.contenido = 0
        self.cerrado = True
    
    def mostrar_info(self):
        print("Material:", self.material)
        print("Capacidad:", self.capacidad, "ml")
        print("Forma:", self.forma)
        print("Diseño:", self.diseno)
        print("Contenido actual:", self.contenido, "ml")
        if self.cerrado:
            print("Estado: Cerrado")
        else:
            print("Estado: Abierto")


class Botella(Contenedor):
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        super().__init__(material, capacidad, forma, diseno)
        self.tapa = tapa
        self.grabados = grabados
        self.reutilizaciones = 0
    
    def cierre_hermetico(self, accion):
        if accion == "abrir":
            self.cerrado = False
            print("Botella abierta")
        elif accion == "cerrar":
            self.cerrado = True
            print("Botella cerrada")
    
    def contener_liquidos(self, cantidad):
        if self.cerrado == False:
            if cantidad <= self.capacidad:
                self.contenido = cantidad
                print("Se llenó la botella con", cantidad, "ml")
            else:
                print("Error: Cantidad muy grande")
        else:
            print("Error: La botella está cerrada")
    
    def facilitar_vertido(self):
        if self.cerrado == False:
            self.contenido = 0
            print("Botella vaciada")
        else:
            print("Error: La botella está cerrada")
    
    def reutilizacion(self):
        self.contenido = 0
        self.reutilizaciones = self.reutilizaciones + 1
        print("Botella reutilizada", self.reutilizaciones, "veces")
    
    def transporte(self, lugar):
        if self.contenido > 0:
            print("Transportando botella a", lugar)
        else:
            print("La botella esta vacia")
    
    def manejo(self, accion):
        acciones = ["agarrar", "colocar", "llevar", "guardar"]
        if accion in acciones:
            print("Accion", accion, "realizada")
        else:
            print("Accion no valida")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Tapa:", self.tapa)
        print("Grabados:", self.grabados)
        print("Veces reutilizada:", self.reutilizaciones)
