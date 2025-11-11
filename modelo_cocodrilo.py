from modelo_animal import Animal

class Cocodrilo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, especie):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie
        self.tipo = "Reptil"
        self.fuerza_mordida = 3700
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 10
            self.hambre = self.hambre + 8
            print(self.nombre, "se arrastra y nada")
            print("Puede nadar a 35 km/h")
            print("Energia:", self.energia, "%")
        else:
            print(self.nombre, "esta descansando")
    
    def comunicacion(self):
        print(self.nombre, "hace: Grrrrr (gruñido de cocodrilo)")
    
    def reproduccion(self):
        if self.edad >= 10:
            print(self.nombre, "puede reproducirse")
            print("Pone huevos en nidos")
            print("Incubacion: 80-90 dias")
        else:
            print(self.nombre, "es muy joven")
    
    def alimentarse(self):
        comida = "peces, aves y mamiferos"
        if self.hambre > 0:
            self.hambre = self.hambre - 30
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 25
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta cazando y comiendo", comida)
            print("Fuerza de mordida:", self.fuerza_mordida, "PSI")
        else:
            print(self.nombre, "no tiene hambre")
    
    def adaptacion(self):
        print("Adaptaciones de", self.nombre + ":")
        print("- Piel escamosa y dura")
        print("- Mandibulas poderosas")
        print("- Puede estar bajo el agua mucho tiempo")
        print("- Cola fuerte para nadar")
    
    def instintos(self):
        print("Instintos del cocodrilo:")
        print("- Cazar por emboscada")
        print("- Permanecer inmovil")
        print("- Termorregulacion al sol")
    
    def interaccion_social(self):
        print(self.nombre, "es mayormente solitario")
        print("Se junta solo para reproducirse")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Especie:", self.especie)
        print("Tipo:", self.tipo)
        print("Fuerza de mordida:", self.fuerza_mordida, "PSI")