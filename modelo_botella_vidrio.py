from modelo_botella import Botella

class BotellaVidrio(Botella):
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados, color):
        super().__init__(material, capacidad, forma, diseno, tapa, grabados)
        self.color = color
        self.fragil = True
        self.peso = capacidad / 3  # peso aproximado
    
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
        colores_transparentes = ["transparente", "claro", "cristal"]
        if self.color.lower() in colores_transparentes:
            print("Vidrio transparente - se ve el contenido")
        else:
            print("Vidrio color", self.color, "- poco transparente")
    
    def transporte(self, lugar):
        if self.contenido > 0:
            print("Transportando botella de vidrio a", lugar)
            print("Peso:", self.peso, "gramos")
        else:
            print("La botella esta vacia")
    
    def compatibilidad_bebidas_calientes_frias(self, bebida, temperatura):
        if temperatura == "caliente":
            print("SI es compatible con", bebida, "caliente")
        else:
            print("SI es compatible con", bebida, "fria")
    
    def mostrar_info(self):
        super().mostrar_info()
        print("Color del vidrio:", self.color)
        print("Peso:", self.peso, "gramos")
        print("Fragil: Si")
