# main.py
# se agrego el examen 
from utils.gastos import *
from utils.reportes import *
from utils.proyeccion import *

def main():
    while True:
        print("\n==== GESTIÓN DE GASTOS ====")
        print("1. Registrar Gasto")
        print("2. Listar Gastos")
        print("3. Generar Reporte")
        print("4. Proyección de Gasto")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            menu_listar_gastos()
        elif opcion == "3":
            generar_reporte()
        elif opcion == "4":
            dias_futuros = input("Ingresa el número de días para la proyección: ")
            proyeccion_gasto(dias_futuros)  # Pasar el valor a la función
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida.")

            
if __name__ == "__main__":
    main()

# Algo que agregar 
# otra cosa 

