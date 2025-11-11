from modelo_animal import Animal

class Pato(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, especie):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.especie = especie
        self.tipo = "Ave acuatica"
        self.puede_volar = True
    
    def moverse(self):
        if self.energia > 10:
            self.energia = self.energia - 10
            self.hambre = self.hambre + 7
            print(self.nombre, "puede:")
            print("- Nadar")
            print("- Volar")
            print("- Caminar")
            print("Energia:", self.energia, "%")
        else:
            print(self.nombre, "esta descansando")
    
    def comunicacion(self):
        print(self.nombre, "hace: Cuac cuac")
    
    def reproduccion(self):
        if self.edad >= 1:
            print(self.nombre, "puede reproducirse")
            print("Pone huevos en nidos cerca del agua")
            print("Incubacion: 28 dias")
        else:
            print(self.nombre, "es muy joven")
    
    def alimentarse(self):
        comida = "plantas acuaticas, insectos y peces pequeños"
        if self.hambre > 0:
            self.hambre = self.hambre - 20
            if self.hambre < 0:
                self.hambre = 0
            self.energia = self.energia + 15
            if self.energia > 100:
                self.energia = 100
            print(self.nombre, "esta comiendo", comida)
            print("Busca comida bajo el agua")
        else:
            print(self.nombre, "no tiene hambre")
    
    def adaptacion(self):
        print("Adaptaciones de", self.nombre + ":")
        print("- Plumas impermeables")
        print("- Patas palmeadas para nadar")
        print("- Pico plano para filtrar agua")
        print("- Alas para volar")
    
    def instintos(self):
        print("Instintos del pato:")
        print("- Migrar en invierno")
        print("- Nadar en grupo")
        print("- Proteger a las crias")
    
    def interaccion_social(self):
        print(self.nombre, "vive en grupos")
        print("Nada con otros patos")
        print("Migra en bandadas")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Especie:", self.especie)
        print("Tipo:", self.tipo)
        print("Puede volar:", "Si" if self.puede_volar else "No")
