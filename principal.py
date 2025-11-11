from modelo_botella import Botella
from modelo_botella_plastica import BotellaPlastica
from modelo_botella_vidrio import BotellaVidrio
from modelo_base_datos import BaseDatosBotellas

def menu():
    print("\n=== Sistema de Botellas ===")
    print("1. Agregar botella plastica")
    print("2. Agregar botella de vidrio")
    print("3. Ver todas las botellas")
    print("4. Ver estadisticas")
    print("5. Buscar botella por ID")
    print("6. Operaciones con botella")
    print("7. Ejemplo completo")
    print("0. Salir")

def ejemplo_completo():
    print("\n=== EJEMPLO COMPLETO ===\n")
    
    bd = BaseDatosBotellas()
    
    print("--- Botella Plastica 1 ---")
    botella1 = BotellaPlastica("Plastico", 500, "Cilindrica", "Azul", "Rosca", "Logo", "Agua Cristal")
    botella1.cierre_hermetico("abrir")
    botella1.contener_liquidos(450, "agua")
    botella1.transporte("casa")
    bd.agregar(botella1)
    
    print("\n--- Botella de Vidrio 1 ---")
    botella2 = BotellaVidrio("Vidrio", 750, "Elegante", "Premium", "Corcho", "Grabado", "Verde")
    botella2.cierre_hermetico("abrir")
    botella2.contener_liquidos(700, "vino")
    botella2.compatibilidad_bebidas_calientes_frias("vino", "fria")
    bd.agregar(botella2)
    
    print("\n--- Botella Plastica 2 ---")
    botella3 = BotellaPlastica("Plastico", 1000, "Grande", "Transparente", "Deportiva", "Logo", "H2O")
    botella3.cierre_hermetico("abrir")
    botella3.contener_liquidos(1000, "agua")
    botella3.verificar_transparencia()
    bd.agregar(botella3)
    
    print("\n--- Botella de Vidrio 2 ---")
    botella4 = BotellaVidrio("Vidrio", 500, "Redonda", "Simple", "Tapa", "Sin grabados", "Transparente")
    botella4.cierre_hermetico("abrir")
    botella4.contener_liquidos(400, "jugo")
    bd.agregar(botella4)
    
    print("\n--- Reutilizacion ---")
    botella1.reutilizacion()
    botella2.reutilizacion()
    botella1.reutilizacion()
    
    bd.listar()
    bd.estadisticas()
    
    print("\n=== FIN DEL EJEMPLO ===")

def operaciones_con_botella(bd):
    print("\n--- Operaciones con Botella ---")
    id = int(input("ID de la botella: "))
    botella = bd.buscar(id)
    
    if botella == None:
        print("No se encontro la botella")
        return
    
    print("\nBotella encontrada - ID:", id)
    print("\nQue deseas hacer?")
    print("1. Abrir botella")
    print("2. Cerrar botella")
    print("3. Llenar botella")
    print("4. Vaciar botella")
    print("5. Transportar botella")
    print("6. Reutilizar botella")
    print("7. Ver informacion completa")
    print("8. Verificar compatibilidad")
    print("9. Ver contenido")
    
    opcion = input("\nElige: ")
    
    if opcion == "1":
        botella.abrir()
    elif opcion == "2":
        botella.cerrar()
    elif opcion == "3":
        cantidad = int(input("Cantidad (ml): "))
        liquido = input("Tipo de liquido: ")
        botella.llenar(cantidad, liquido)
    elif opcion == "4":
        botella.vaciar()
    elif opcion == "5":
        lugar = input("Lugar de destino: ")
        botella.transportar(lugar)
    elif opcion == "6":
        botella.reutilizar()
    elif opcion == "7":
        botella.mostrar_info()
    elif opcion == "8":
        bebida = input("Bebida: ")
        temp = input("Temperatura (caliente/fria): ")
        botella.compatibilidad(bebida, temp)
    elif opcion == "9":
        if hasattr(botella, 'verificar_contenido'):
            botella.verificar_contenido()
        else:
            print("Contenido actual:", botella.contenido, "ml")
    else:
        print("Opcion no valida")

bd = BaseDatosBotellas()

while True:
    menu()
    opcion = input("\nElige una opcion: ")
    
    if opcion == "1":
        print("\n--- Agregar Botella Plastica ---")
        marca = input("Marca: ")
        capacidad = int(input("Capacidad (ml): "))
        botella = BotellaPlastica("Plastico PET", capacidad, "Cilindrica", "Transparente", "Rosca", "Logo", marca)
        bd.agregar(botella)
        
    elif opcion == "2":
        print("\n--- Agregar Botella de Vidrio ---")
        color = input("Color: ")
        capacidad = int(input("Capacidad (ml): "))
        botella = BotellaVidrio("Vidrio", capacidad, "Elegante", "Premium", "Corcho", "Grabado", color)
        bd.agregar(botella)
        
    elif opcion == "3":
        bd.listar()
        
    elif opcion == "4":
        bd.estadisticas()
        
    elif opcion == "5":
        id = int(input("ID de la botella: "))
        botella = bd.buscar(id)
        if botella != None:
            print("\nBotella encontrada:")
            botella.mostrar_info()
        else:
            print("No se encontro la botella")
            
    elif opcion == "6":
        operaciones_con_botella(bd)
        
    elif opcion == "7":
        ejemplo_completo()
        
    elif opcion == "0":
        print("Adios!")
        break
        
    else:
        print("Opcion no valida")