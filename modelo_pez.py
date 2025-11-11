from modelo_animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, especie):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie
        self.tipo = "Pez"
        self.profundidad_max = 100
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 8
            self.hambre = self.hambre + 5
            print(self.nombre, "esta nadando")
            print("Profundidad maxima:", self.profundidad_max, "metros")
            print("Energia:", self.energia, "%")
        else:
            print(self.nombre, "esta quieto en el agua")
    
    def comunicacion(self):
        print(self.nombre, "hace: Glub glub (burbujas)")
        print("Se comunica con movimientos")
    
    def reproduccion(self):
        if self.edad >= 1:
            print(self.nombre, "puede reproducirse")
            print("Pone huevos en el agua")
        else:
            print(self.nombre, "es muy joven")
    
    def alimentarse(self):
        comida = "algas, plancton y pequeños invertebrados"
        if self.hambre > 0:
            self.hambre = self.hambre - 20
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 15
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta comiendo", comida)
        else:
            print(self.nombre, "no tiene hambre")
    
    def adaptacion(self):
        print("Adaptaciones de", self.nombre + ":")
        print("- Branquias para respirar bajo el agua")
        print("- Aletas para nadar")
        print("- Escamas protectoras")
        print("- Linea lateral para detectar movimiento")
    
    def instintos(self):
        print("Instintos del pez:")
        print("- Nadar en grupo (cardumen)")
        print("- Buscar alimento")
        print("- Huir de depredadores")
    
    def interaccion_social(self):
        print(self.nombre, "nada en cardumen")
        print("Se protegen en grupo")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Especie:", self.especie)
        print("Tipo:", self.tipo)
        print("Profundidad maxima:", self.profundidad_max, "metros")