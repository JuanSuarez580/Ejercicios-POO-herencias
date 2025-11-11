from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, raza):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.raza = raza
        self.tipo = "Mamifero"
        self.velocidad_max = 70
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 15
            self.hambre = self.hambre + 10
            print(self.nombre, "esta galopando")
            print("Velocidad maxima:", self.velocidad_max, "km/h")
            print("Energia:", self.energia, "%")
        else:
            print(self.nombre, "esta cansado")
    
    def comunicacion(self):
        print(self.nombre, "hace: Hiiiiii (relincha)")
    
    def reproduccion(self):
        if self.edad >= 3:
            print(self.nombre, "puede reproducirse")
            print("Gestacion: 11 meses")
        else:
            print(self.nombre, "es muy joven para reproducirse")
    
    def alimentarse(self):
        comida = "pasto y heno"
        if self.hambre > 0:
            self.hambre = self.hambre - 25
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 20
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta comiendo", comida)
        else:
            print(self.nombre, "no tiene hambre")
    
    def adaptacion(self):
        print("Adaptaciones de", self.nombre + ":")
        print("- Patas fuertes para correr")
        print("- Dientes para masticar pasto")
        print("- Orejas moviles")
    
    def instintos(self):
        print("Instintos del caballo:")
        print("- Huir del peligro")
        print("- Vivir en manada")
        print("- Buscar alimento")
    
    def interaccion_social(self):
        print(self.nombre, "interactua con otros caballos")
        print("Vive en manada")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Raza:", self.raza)
        print("Tipo:", self.tipo)
        print("Velocidad maxima:", self.velocidad_max, "km/h")