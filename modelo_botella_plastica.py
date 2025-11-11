from modelo_botella import Botella

class BotellaPlastica(Botella):
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados, marca):
        super().__init__(material, capacidad, forma, diseno, tapa, grabados)
        self.marca = marca
        self.tipo = "PET"
    
    def contener_liquidos(self, cantidad, liquido):
        if self.cerrado == False:
            if cantidad <= self.capacidad:
                self.contenido = cantidad
                print("Se llenó con", cantidad, "ml de", liquido)
            else:
                print("Error: No cabe tanto")
        else:
            print("Error: Primero abre la botella")
    
    def verificar_transparencia(self):
        print("La botella tiene", self.contenido, "ml")
        porcentaje = (self.contenido * 100) / self.capacidad
        print("Esta llena al", porcentaje, "%")
    
    def transporte(self, lugar):
        if self.contenido > 0:
            print("Transportando botella a", lugar)
        else:
            print("La botella esta vacia")
    
    def compatibilidad_bebidas_calientes_frias(self, bebida, temperatura):
        if temperatura == "caliente":
            print("NO es compatible con bebidas calientes")
        else:
            print("SI es compatible con", bebida, "fria")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Marca:", self.marca)
        print("Tipo de plastico:", self.tipo)
