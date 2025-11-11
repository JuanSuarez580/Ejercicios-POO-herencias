from modelo_animal import Animal
from modelo_caballo import Caballo
from modelo_cocodrilo import Cocodrilo
from modelo_pez import Pez
from modelo_escarabajo import Escarabajo
from modelo_pato import Pato
from modelo_base_datos import BaseDatosAnimales

def menu():
    print("\n=== Sistema de Animales ===")
    print("1. Agregar caballo")
    print("2. Agregar cocodrilo")
    print("3. Agregar pez")
    print("4. Agregar escarabajo")
    print("5. Agregar pato")
    print("6. Ver todos los animales")
    print("7. Ver estadisticas")
    print("8. Buscar animal por ID")
    print("9. Operaciones con animal")
    print("10. Ejemplo completo")
    print("0. Salir")

def ejemplo_completo():
    print("\n=== EJEMPLO COMPLETO ===\n")
    
    bd = BaseDatosAnimales()
    
    print("--- Caballo ---")
    caballo = Caballo("Spirit", 5, "Pradera", "Herbivoro", "Grande", "Marron", "Mustang")
    caballo.moverse()
    caballo.comunicacion()
    caballo.alimentarse()
    caballo.reproduccion()
    bd.agregar(caballo)
    
    print("\n--- Cocodrilo ---")
    cocodrilo = Cocodrilo("Nilo", 15, "Rio y pantano", "Carnivoro", "Muy grande", "Verde oscuro", "Cocodrilo del Nilo")
    cocodrilo.moverse()
    cocodrilo.comunicacion()
    cocodrilo.alimentarse()
    cocodrilo.adaptacion()
    bd.agregar(cocodrilo)
    
    print("\n--- Pez ---")
    pez = Pez("Nemo", 2, "Arrecife", "Omnivoro", "Pequeño", "Naranja", "Pez payaso")
    pez.moverse()
    pez.comunicacion()
    pez.alimentarse()
    pez.interaccion_social()
    bd.agregar(pez)
    
    print("\n--- Escarabajo ---")
    escarabajo = Escarabajo("Hercules", 1, "Bosque", "Detritofago", "Mediano", "Negro", "Rinoceronte")
    escarabajo.moverse()
    escarabajo.comunicacion()
    escarabajo.reproduccion()
    bd.agregar(escarabajo)
    
    print("\n--- Pato ---")
    pato = Pato("Donald", 3, "Lago", "Omnivoro", "Mediano", "Blanco y verde", "Pato real")
    pato.moverse()
    pato.comunicacion()
    pato.alimentarse()
    pato.adaptacion()
    bd.agregar(pato)
    
    bd.listar()
    bd.estadisticas()
    
    print("\n=== FIN DEL EJEMPLO ===")

def operaciones_con_animal(bd):
    print("\n--- Operaciones con Animal ---")
    id = int(input("ID del animal: "))
    animal = bd.buscar(id)
    
    if animal == None:
        print("No se encontro el animal")
        return
    
    print("\nAnimal encontrado - ID:", id, "-", animal.nombre)
    print("\nQue deseas hacer?")
    print("1. Moverse")
    print("2. Comunicacion")
    print("3. Alimentarse")
    print("4. Reproduccion")
    print("5. Adaptacion")
    print("6. Instintos")
    print("7. Descanso")
    print("8. Sueño")
    print("9. Interaccion social")
    print("10. Ver informacion completa")
    
    opcion = input("\nElige: ")
    
    if opcion == "1":
        animal.moverse()
    elif opcion == "2":
        animal.comunicacion()
    elif opcion == "3":
        animal.alimentarse()
    elif opcion == "4":
        animal.reproduccion()
    elif opcion == "5":
        animal.adaptacion()
    elif opcion == "6":
        animal.instintos()
    elif opcion == "7":
        animal.descanso()
    elif opcion == "8":
        animal.sueño()
    elif opcion == "9":
        animal.interaccion_social()
    elif opcion == "10":
        animal.mostrar_info()
    else:
        print("Opcion no valida")

bd = BaseDatosAnimales()

while True:
    menu()
    opcion = input("\nElige una opcion: ")
    
    if opcion == "1":
        print("\n--- Agregar Caballo ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habitat = input("Habitat: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")
        raza = input("Raza: ")
        caballo = Caballo(nombre, edad, habitat, "Herbivoro", tamaño, color, raza)
        bd.agregar(caballo)
        
    elif opcion == "2":
        print("\n--- Agregar Cocodrilo ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habitat = input("Habitat: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")
        especie = input("Especie: ")
        cocodrilo = Cocodrilo(nombre, edad, habitat, "Carnivoro", tamaño, color, especie)
        bd.agregar(cocodrilo)
        
    elif opcion == "3":
        print("\n--- Agregar Pez ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habitat = input("Habitat: ")
        dieta = input("Dieta: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")
        especie = input("Especie: ")
        pez = Pez(nombre, edad, habitat, dieta, tamaño, color, especie)
        bd.agregar(pez)
        
    elif opcion == "4":
        print("\n--- Agregar Escarabajo ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habitat = input("Habitat: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")
        especie = input("Especie: ")
        escarabajo = Escarabajo(nombre, edad, habitat, "Detritofago", tamaño, color, especie)
        bd.agregar(escarabajo)
        
    elif opcion == "5":
        print("\n--- Agregar Pato ---")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habitat = input("Habitat: ")
        dieta = input("Dieta: ")
        tamaño = input("Tamaño: ")
        color = input("Color: ")
        especie = input("Especie: ")
        pato = Pato(nombre, edad, habitat, dieta, tamaño, color, especie)
        bd.agregar(pato)
        
    elif opcion == "6":
        bd.listar()
        
    elif opcion == "7":
        bd.estadisticas()
        
    elif opcion == "8":
        id = int(input("ID del animal: "))
        animal = bd.buscar(id)
        if animal != None:
            print("\nAnimal encontrado:")
            animal.mostrar_info()
        else:
            print("No se encontro el animal")
            
    elif opcion == "9":
        operaciones_con_animal(bd)
        
    elif opcion == "10":
        ejemplo_completo()
        
    elif opcion == "0":
        print("Adios!")
        break
        
    else:
        print("Opcion no valida")