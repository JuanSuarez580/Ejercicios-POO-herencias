from modelo_animal import Animal

class Escarabajo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, especie):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie
        self.tipo = "Insecto"
        self.tiene_alas = True
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 5
            self.hambre = self.hambre + 5
            if self.tiene_alas:
                print(self.nombre, "esta volando y caminando")
            else:
                print(self.nombre, "esta caminando")
            print("Energia:", self.energia, "%")
        else:
            print(self.nombre, "esta descansando")
    
    def comunicacion(self):
        print(self.nombre, "hace: Zzzz (sonido de alas)")
        print("Se comunica con feromonas")
    
    def reproduccion(self):
        if self.edad >= 1:
            print(self.nombre, "puede reproducirse")
            print("Pone huevos")
            print("Pasa por metamorfosis: huevo, larva, pupa, adulto")
        else:
            print(self.nombre, "aun es larva")
    
    def alimentarse(self):
        comida = "materia organica en descomposicion"
        if self.hambre > 0:
            self.hambre = self.hambre - 15
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 10
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta comiendo", comida)
        else:
            print(self.nombre, "no tiene hambre")
    
    def adaptacion(self):
        print("Adaptaciones de", self.nombre + ":")
        print("- Exoesqueleto duro")
        print("- Alas protegidas bajo elitros")
        print("- Patas fuertes")
        print("- Antenas sensoriales")
    
    def instintos(self):
        print("Instintos del escarabajo:")
        print("- Buscar materia organica")
        print("- Hacer bolas de estiercol")
        print("- Proteger huevos")
    
    def interaccion_social(self):
        print(self.nombre, "trabaja en solitario")
        print("Se junta solo para reproducirse")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Especie:", self.especie)
        print("Tipo:", self.tipo)
        print("Tiene alas:", "Si" if self.tiene_alas else "No")