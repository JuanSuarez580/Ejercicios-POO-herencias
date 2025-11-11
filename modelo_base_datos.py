from modelo_animal import Animal
from modelo_caballo import Caballo
from modelo_cocodrilo import Cocodrilo
from modelo_pez import Pez
from modelo_escarabajo import Escarabajo
from modelo_pato import Pato

class BaseDatosAnimales:
    def __init__(self):
        self.lista_animales = []
        self.numero_id = 1
    
    def agregar(self, animal):
        animal.id = self.numero_id
        self.lista_animales.append(animal)
        self.numero_id = self.numero_id + 1
        print("Animal agregado con ID:", animal.id)
    
    def buscar(self, id):
        for animal in self.lista_animales:
            if animal.id == id:
                return animal
        return None
    
    def contar_con_hambre(self):
        contador = 0
        for animal in self.lista_animales:
            if animal.hambre > 50:
                contador = contador + 1
        return contador
    
    def contar_con_energia_baja(self):
        contador = 0
        for animal in self.lista_animales:
            if animal.energia < 30:
                contador = contador + 1
        return contador
    
    def listar(self):
        print("\n=== Lista de Animales ===")
        for animal in self.lista_animales:
            print("\nID:", animal.id)
            print("Nombre:", animal.nombre)
            print("Edad:", animal.edad, "años")
            print("Habitat:", animal.habitat)
            print("Dieta:", animal.dieta)
            print("Energia:", animal.energia, "%")
            if hasattr(animal, 'tipo'):
                print("Tipo:", animal.tipo)
    
    def estadisticas(self):
        total = len(self.lista_animales)
        con_hambre = self.contar_con_hambre()
        energia_baja = self.contar_con_energia_baja()
        
        print("\n=== Estadisticas ===")
        print("Total de animales:", total)
        print("Animales con mucha hambre:", con_hambre)
        print("Animales con energia baja:", energia_baja)