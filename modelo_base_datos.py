from modelo_botella import Botella
from modelo_botella_plastica import BotellaPlastica
from modelo_botella_vidrio import BotellaVidrio

class BaseDatosBotellas:
    def __init__(self):
        self.lista_botellas = []
        self.numero_id = 1
    
    def agregar(self, botella):
        botella.id = self.numero_id
        self.lista_botellas.append(botella)
        self.numero_id = self.numero_id + 1
        print("Botella agregada con ID:", botella.id)
    
    def buscar(self, id):
        for botella in self.lista_botellas:
            if botella.id == id:
                return botella
        return None
    
    def contar_vacias(self):
        contador = 0
        for botella in self.lista_botellas:
            if botella.contenido == 0:
                contador = contador + 1
        return contador
    
    def contar_llenas(self):
        contador = 0
        for botella in self.lista_botellas:
            if botella.contenido >= botella.capacidad:
                contador = contador + 1
        return contador
    
    def listar(self):
        print("\n=== Lista de Botellas ===")
        for botella in self.lista_botellas:
            print("\nID:", botella.id)
            print("Material:", botella.material)
            print("Capacidad:", botella.capacidad, "ml")
            print("Contenido:", botella.contenido, "ml")
            if hasattr(botella, 'marca'):
                print("Marca:", botella.marca)
            if hasattr(botella, 'color'):
                print("Color:", botella.color)
    
    def estadisticas(self):
        total = len(self.lista_botellas)
        vacias = self.contar_vacias()
        llenas = self.contar_llenas()
        
        print("\n=== Estadisticas ===")
        print("Total de botellas:", total)
        print("Botellas vacias:", vacias)
        print("Botellas llenas:", llenas)
