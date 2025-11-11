class SerVivo:
    def __init__(self, nombre, edad, habitat):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.vivo = True
        self.energia = 100
    
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad, "años")
        print("Habitat:", self.habitat)
        print("Energia:", self.energia, "%")
        if self.vivo:
            print("Estado: Vivo")
        else:
            print("Estado: No vivo")


class Animal(SerVivo):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        super().__init__(nombre, edad, habitat)
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color
        self.hambre = 0
        self.sueño = 0
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 10
            self.hambre = self.hambre + 5
            print(self.nombre, "se esta moviendo")
            print("Energia restante:", self.energia, "%")
        else:
            print(self.nombre, "esta muy cansado para moverse")
    
    def comunicacion(self, sonido):
        print(self.nombre, "hace:", sonido)
    
    def alimentarse(self, comida):
        if self.hambre > 0:
            self.hambre = self.hambre - 20
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 15
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta comiendo", comida)
            print("Hambre:", self.hambre, "%")
        else:
            print(self.nombre, "no tiene hambre")
    
    def descanso(self):
        self.energia = self.energia + 30
        if self.energia > 100:
            self.energia = 100
        print(self.nombre, "esta descansando")
        print("Energia:", self.energia, "%")
    
    def sueño(self):
        self.sueño = 0
        self.energia = 100
        print(self.nombre, "esta durmiendo")
        print("Energia recuperada al 100%")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Dieta:", self.dieta)
        print("Tamaño:", self.tamaño)
        print("Color:", self.color)
        print("Hambre:", self.hambre, "%")
        print("Sueño:", self.sueño, "%")