from Modelo_vehiculo import Vehiculo
from Modelo_auto import Auto
from Modelo_camioneta import Camioneta
from Modelo_camion import Camion
from Modelo_base_datos import BaseDatosVehiculos

def menu():
    print("\n=== Sistema de Vehiculos ===")
    print("1. Agregar auto")
    print("2. Agregar camioneta")
    print("3. Agregar camion")
    print("4. Ver todos los vehiculos")
    print("5. Ver estadisticas")
    print("6. Buscar vehiculo por ID")
    print("7. Operaciones con vehiculo")
    print("8. Ejemplo completo")
    print("0. Salir")

def ejemplo_completo():
    print("\n=== EJEMPLO COMPLETO ===\n")
    
    bd = BaseDatosVehiculos()
    
    print("--- Auto Deportivo ---")
    auto1 = Auto("Z4", "Azul metalico", "2.0L Turbo", 2, 2, "Gasolina", "BMW")
    auto1.arrancar()
    auto1.acelerar(120)
    auto1.sistema_direccion("derecha")
    auto1.luces_auto("encender")
    auto1.climatizacion("encender")
    bd.agregar(auto1)
    
    print("\n--- Camioneta Van ---")
    camioneta1 = Camioneta("Hiace", "Blanco", "2.7L", 4, 12, "Gasolina", "Toyota")
    camioneta1.arrancar()
    camioneta1.acelerar(80)
    camioneta1.sistema_direccion("izquierda")
    camioneta1.cargar(600)
    bd.agregar(camioneta1)
    
    print("\n--- Camion de Carga ---")
    camion1 = Camion("Dyna", "Blanco", "4.0L Diesel", 2, 3, "Diesel", "Toyota")
    camion1.arrancar()
    camion1.acelerar(60)
    camion1.cargar(4000)
    camion1.verificar_carga()
    bd.agregar(camion1)
    
    bd.listar()
    bd.estadisticas()
    
    print("\n=== FIN DEL EJEMPLO ===")

def operaciones_con_vehiculo(bd):
    print("\n--- Operaciones con Vehiculo ---")
    id = int(input("ID del vehiculo: "))
    vehiculo = bd.buscar(id)
    
    if vehiculo == None:
        print("No se encontro el vehiculo")
        return
    
    print("\nVehiculo encontrado - ID:", id)
    print("\nQue deseas hacer?")
    print("1. Arrancar")
    print("2. Apagar")
    print("3. Acelerar")
    print("4. Frenar")
    print("5. Sistema de direccion")
    print("6. Climatizacion")
    print("7. Luces")
    print("8. Ventanas")
    print("9. Espejos")
    print("10. Ver tipo de seguridad")
    print("11. Cargar (para camiones)")
    print("12. Descargar (para camiones)")
    print("13. Verificar carga (para camiones)")
    print("14. Ver informacion completa")
    
    opcion = input("\nElige: ")
    
    if opcion == "1":
        vehiculo.arrancar()
    elif opcion == "2":
        vehiculo.apagar()
    elif opcion == "3":
        cantidad = int(input("Cuanto acelerar (km/h): "))
        vehiculo.acelerar(cantidad)
    elif opcion == "4":
        cantidad = int(input("Cuanto frenar (km/h): "))
        vehiculo.frenar(cantidad)
    elif opcion == "5":
        direccion = input("Direccion (derecha/izquierda): ")
        vehiculo.sistema_direccion(direccion)
    elif opcion == "6":
        accion = input("Accion (encender/apagar): ")
        vehiculo.climatizacion(accion)
    elif opcion == "7":
        if hasattr(vehiculo, 'luces_auto'):
            accion = input("Accion (encender/apagar): ")
            vehiculo.luces_auto(accion)
        else:
            print("Este vehiculo no tiene ese sistema")
    elif opcion == "8":
        ventana = input("Que ventana: ")
        accion = input("Accion (subir/bajar): ")
        vehiculo.sistema_ventanas(ventana, accion)
    elif opcion == "9":
        accion = input("Accion (ajustar/plegar): ")
        vehiculo.sistema_espejo(accion)
    elif opcion == "10":
        vehiculo.tipo_seguridad()
    elif opcion == "11":
        if hasattr(vehiculo, 'cargar'):
            peso = int(input("Peso a cargar (kg): "))
            vehiculo.cargar(peso)
        else:
            print("Este vehiculo no puede cargar")
    elif opcion == "12":
        if hasattr(vehiculo, 'descargar'):
            peso = int(input("Peso a descargar (kg): "))
            vehiculo.descargar(peso)
        else:
            print("Este vehiculo no tiene carga")
    elif opcion == "13":
        if hasattr(vehiculo, 'verificar_carga'):
            vehiculo.verificar_carga()
        else:
            print("Este vehiculo no maneja carga")
    elif opcion == "14":
        vehiculo.mostrar_info()
    else:
        print("Opcion no valida")

bd = BaseDatosVehiculos()

while True:
    menu()
    opcion = input("\nElige una opcion: ")
    
    if opcion == "1":
        print("\n--- Agregar Auto ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        motor = input("Motor: ")
        puertas = int(input("Numero de puertas: "))
        pasajeros = int(input("Capacidad de pasajeros: "))
        combustible = input("Tipo de combustible: ")
        auto = Auto(modelo, color, motor, puertas, pasajeros, combustible, marca)
        bd.agregar(auto)
        
    elif opcion == "2":
        print("\n--- Agregar Camioneta ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        motor = input("Motor: ")
        puertas = int(input("Numero de puertas: "))
        pasajeros = int(input("Capacidad de pasajeros: "))
        combustible = input("Tipo de combustible: ")
        camioneta = Camioneta(modelo, color, motor, puertas, pasajeros, combustible, marca)
        bd.agregar(camioneta)
        
    elif opcion == "3":
        print("\n--- Agregar Camion ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        motor = input("Motor: ")
        puertas = int(input("Numero de puertas: "))
        pasajeros = int(input("Capacidad de pasajeros: "))
        combustible = input("Tipo de combustible: ")
        camion = Camion(modelo, color, motor, puertas, pasajeros, combustible, marca)
        bd.agregar(camion)
        
    elif opcion == "4":
        bd.listar()
        
    elif opcion == "5":
        bd.estadisticas()
        
    elif opcion == "6":
        id = int(input("ID del vehiculo: "))
        vehiculo = bd.buscar(id)
        if vehiculo != None:
            print("\nVehiculo encontrado:")
            vehiculo.mostrar_info()
        else:
            print("No se encontro el vehiculo")
            
    elif opcion == "7":
        operaciones_con_vehiculo(bd)
        
    elif opcion == "8":
        ejemplo_completo()
        
    elif opcion == "0":
        print("Adios!")
        break
        
    else:
        print("Opcion no valida")